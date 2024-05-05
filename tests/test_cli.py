import subprocess


def test_main():
    assert subprocess.check_output(["databricks_bundle_validator_cli", "hello", "--name", "Ivan Pina"], text=True) == "Hello Ivan Pina!\n"
