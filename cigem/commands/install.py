from pathlib import Path

import click


@click.command(help="Install")
@click.option(
    "--path", type=click.Path(True), default=Path("."), help="Paths to the Package"
)
def install(path: Path):
    pass
