from pydantic import BaseModel, ConfigDict, Field
from typing import List, Optional


class _BaseModel(BaseModel):
    model_config = ConfigDict(
        protected_namespaces=(),
        extra="allow"
    )


class DatabricksFile(_BaseModel):
    include: Optional[List[str]] = Field(default_factory=list)
