from pathlib import Path

import click


@click.command(help="Add")
@click.option(
    "--path", type=click.Path(True), default=Path("."), help="Paths to the Package"
)
def add(path: Path):
    pass
