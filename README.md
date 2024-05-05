# Databricks Bundle Validator

CLI application to read a [Databricks Asset Bundle](https://docs.databricks.com/en/dev-tools/bundles/index.html) configuration and enforce/overwrite values.

## Installation

```shell
pip install git+https://github.com/CIvanPiMa/databricks_bundle_validator.git
```

## Usage

In a terminal run

```shell
databricks_bundle_validator_cli inject
```

This will:
- Search for a `databricks.y*ml` file in the current working directory.
- Validate it using the `MainDatabricksFile` class defined in the [mappings](src/databricks_bundle_validator/mappings.py) module.
- Search for any extra files defined in the [include](https://docs.databricks.com/en/dev-tools/bundles/settings.html#include) section and validate those using the `DatabricksFile` class.
- Finally, overwrites  the files with the validated/injected values.

> **NOTE**:
> Currently the only validations/injections are performed in the `permissions` section.
