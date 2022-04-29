from pathlib import Path

import click

from cigem.core.rendering import render_setup_script
from cigem.core.system import call_mkdir, call_touch


@click.command(help="Create")
@click.option(
    "--name",
    type=str,
    required=True,
    help="The name of the Python package to be created",
)
@click.option(
    "--path",
    required=False,
    type=click.Path(True),
    help="Paths to the Package",
    default=Path("."),
)
def create(name, path):

    project = path.joinpath(name)
    call_mkdir(project)

    module = project.joinpath(name)
    call_mkdir(module)

    init = module.joinpath("__init__.py")
    call_touch(init)

    setup = project.joinpath("setup.py")
    content = render_setup_script(name)
    setup.write_text(content)
