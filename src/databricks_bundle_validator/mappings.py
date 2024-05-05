from typing import List, Literal, Optional

from pydantic import BaseModel, ConfigDict, Field, ValidationInfo, field_validator, model_validator


class _BaseModel(BaseModel):
    model_config = ConfigDict(protected_namespaces=(), extra="allow")


class _Permission(_BaseModel):
    level: Literal["CAN_VIEW", "CAN_MANAGE", "CAN_RUN"]
    user_name: Optional[str] = Field(default=None)
    group_name: Optional[str] = Field(default=None)
    service_principal_name: Optional[str] = Field(default=None)

    @model_validator(mode="after")
    def use_one_principal_per_permission(self) -> "_Permission":
        principals = [self.user_name, self.group_name, self.service_principal_name]
        assert (
            sum([bool(principal) for principal in principals]) == 1
        ), f"More than one principal defined, given: {principals=}"
        return self


class DatabricksFile(_BaseModel):
    permissions: Optional[List[_Permission]] = Field(default_factory=list)
    include: List[str] = Field(default_factory=list)

    @field_validator("permissions")
    @classmethod
    def permissions_should_be_empty(cls, value: List[_Permission], info: ValidationInfo):
        assert value is None, f"You can't pass 'permissions', given: {value}"


class MainDatabricksFile(DatabricksFile):
    @model_validator(mode="after")  # type: ignore[misc]
    def fill_authomatic_permissions(self) -> "DatabricksFile":
        self.permissions = [_Permission.model_construct(level="CAN_MANAGE", user_name="me@me.com")]
        return self
