from pathlib import Path
from typing import Dict, List

from pydantic import ValidationError
from pydantic_yaml import parse_yaml_file_as, to_yaml_file

from databricks_bundle_validator.crawler import get_extra_databricks_files, get_main_databricks_path
from databricks_bundle_validator.mappings import DatabricksFile, MainDatabricksFile


def main(search_path: Path | str, dry_run: bool = False):
    search_path = Path(search_path) if isinstance(search_path, str) else search_path
    main_databricks_path: Path = get_main_databricks_path(search_path=search_path)
    main_databricks_file: MainDatabricksFile = parse_yaml_file_as(MainDatabricksFile, main_databricks_path)
    extra_databricks_files: List[Path] = get_extra_databricks_files(main_databricks_path, main_databricks_file.include)
    all_databricks_files: Dict[Path, DatabricksFile] = {
        path: parse_yaml_file_as(DatabricksFile, path) for path in extra_databricks_files
    }
    all_databricks_files[main_databricks_path] = main_databricks_file
    if not dry_run:
        overwrite_databricks_files(all_databricks_files)


def overwrite_databricks_files(all_databricks_files: Dict[Path, DatabricksFile]):
    for path, databricks_file in all_databricks_files.items():
        to_yaml_file(path, databricks_file, exclude_none=True)


if __name__ == "__main__":
    import os

    path = f"{os.getcwd()}/_tests/databricks_bundles"
    for dir in [
        "invalid_permissions_file",
        "multiple_files",
        "single_file",
        "use_include",
    ]:
        try:
            main(Path(f"{path}/{dir}"), dry_run=False)
        except AssertionError as e:
            print(e)
        except ValidationError as e:
            print(e)
