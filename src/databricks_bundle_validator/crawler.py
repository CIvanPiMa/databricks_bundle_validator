import os
from typing import List
from pathlib import Path


def get_main_databricks_path(search_path: Path) -> Path:
    pattern = "databricks.y*ml"
    files_found = list(search_path.glob(pattern))
    assert len(files_found) == 1, f"There should be only one '{pattern}' file at '{search_path}', files_found={[file.name for file in files_found]}."
    return files_found[0]


def get_extra_databricks_files(main_databricks_path: Path, includes: List[str]) -> List[Path]:

    extra_databricks_files = []
    for pattern in includes:
        extra_databricks_files += list(main_databricks_path.parent.glob(pattern))
    return extra_databricks_files


if __name__ == "__main__":
    cwd = os.getcwd()
    try:
        get_main_databricks_path(Path(f"{cwd}/_tests/databricks_bundles/multiple_files"))
    except AssertionError as e:
        print(e)

    path = Path(f"{cwd}/_tests/databricks_bundles/single_file")
    print(get_main_databricks_path(path))

    path = Path(f"{cwd}/_tests/databricks_bundles/use_include")
    includes = [
        "include.yml",
        "wildcard/include_*.yml",
    ]
    print(get_extra_databricks_files(path, includes))
