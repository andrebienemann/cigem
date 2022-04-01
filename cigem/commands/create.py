from pathlib import Path

import click


@click.command(help="Create")
@click.option(
    "--path", type=click.Path(True), default=Path("."), help="Paths to the Package"
)
def create(path):
    pass
