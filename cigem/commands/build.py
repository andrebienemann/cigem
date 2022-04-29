from pathlib import Path

import click

from cigem.core.rendering import render_extension_module
from cigem.core.system import call_build, call_rm
from cigem.model.package import Package


@click.command(help="Build")
@click.option(
    "--path",
    required=False,
    type=click.Path(True),
    help="Path to the Package",
    default=Path("."),
)
def build(path):
    package = Package.make_package(path)

    for module in package.modules:
        content = render_extension_module(module)
        path.joinpath(f"{module.name}.c").write_text(content)

    call_build(path)

    call_rm(path.joinpath("tmp"))
