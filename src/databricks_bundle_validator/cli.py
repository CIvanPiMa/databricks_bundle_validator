"""
Module containing the CLI app of the library
"""

import os
from pathlib import Path

import click

from . import inject


@click.group()
def cli():
    pass


@cli.command(name="inject")
@click.option("--search-path", default=os.getcwd(), type=click.Path(exists=True, file_okay=False, resolve_path=True))
@click.option("--dry-run", is_flag=True, default=False)
def inject_cmd(search_path: Path, dry_run: bool):
    """
    Add required values into the Databricks asset bundle files.

    `attributes`:

    - `search_path`: `Path`
        - [OPTIONAL]: Path to search the main Databricks Asset Bundle file. If none given use the current working directory.
    - `dry_run`: `bool`
        - [OPTIONAL]: Only generate a report of changes to be done.
    """
    inject.main(search_path=search_path, dry_run=dry_run)


if __name__ == "__main__":
    cli()
