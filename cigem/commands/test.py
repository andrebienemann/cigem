from pathlib import Path

import click

from cigem.core.rendering import render_extension_module
from cigem.core.system import call_build_ext, call_rm, call_unittest
from cigem.model.package import Package


@click.command(help="Test")
@click.option(
    "--path",
    required=False,
    type=click.Path(True),
    help="Paths to the Package",
    default=Path("."),
)
def test(path):
    package = Package.make_package(path)

    for module in package.modules:
        content = render_extension_module(module)
        path.joinpath(f"{module.name}.c").write_text(content)

    call_build_ext(path)

    call_unittest(path)

    call_rm(path.joinpath("tmp"))
