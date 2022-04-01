from pathlib import Path

import click


@click.command(help="Build")
@click.option(
    "--path", type=click.Path(True), default=Path("."), help="Path to the Package"
)
def build(path):
    pass
