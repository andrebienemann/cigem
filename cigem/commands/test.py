from pathlib import Path

import click


@click.command(help="Test")
@click.option(
    "--path", type=click.Path(True), default=Path("."), help="Paths to the Package"
)
def test(path):
    pass
