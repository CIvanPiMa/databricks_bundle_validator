import os
import subprocess

cwd = os.getcwd()
test_assets = os.path.join(cwd, "tests/assets/databricks_bundles")


def test_main():
    result = subprocess.check_output(
        ["databricks_bundle_validator_cli", "inject", "--search-path", f"{test_assets}/single_file", "--dry-run"],
        text=True,
    )
    assert result == ""
