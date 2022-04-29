from pathlib import Path

import click

from cigem.core.system import call_mkdir, call_touch
from cigem.model.setup import Setup


@click.group(help="Add")
@click.option(
    "--path",
    required=False,
    type=click.Path(True),
    help="Paths to the Package",
    default=Path("."),
)
@click.pass_context
def add(ctx, path):
    ctx.ensure_object(dict)
    ctx.obj["PATH"] = path


@add.command()
@click.option(
    "--name",
    required=True,
    type=str,
    help="The name of the module",
)
@click.pass_context
def module(ctx, name):
    path = ctx.obj["PATH"]
    setup = Setup.make_setup(path)
    package_name = setup.package_name

    module_path = path.joinpath(package_name).joinpath(name)
    header_path = module_path.joinpath("__init__.h")
    stub_path = module_path.joinpath("__init__.pyi")

    call_mkdir(module_path)
    call_touch(header_path)
    call_touch(stub_path)


@add.command()
@click.option(
    "--name",
    required=True,
    type=str,
    help="The name of the function",
)
@click.option(
    "--module",
    required=True,
    type=str,
    help="The name of the module",
)
@click.pass_context
def function(ctx, name, module):
    path = ctx.obj["PATH"]
    setup = Setup.make_setup(path)
    package_name = setup.package_name

    module_path = path.joinpath(package_name).joinpath(module)
    function_path = module_path.joinpath(name)
    header_path = function_path.joinpath(f"{name}.h")
    source_path = function_path.joinpath(f"{name}.c")

    call_mkdir(function_path)
    call_touch(header_path)
    call_touch(source_path)
