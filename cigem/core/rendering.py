import os

from jinja2 import Environment, FileSystemLoader

templates_path = os.path.join(os.path.dirname(__file__), "../templates")
environment = Environment(loader=FileSystemLoader(templates_path))


def render_extension_module(module):
    """
    Renders wrapper code for an extension module

    Parameters
    module: the module to be rendered
    """

    extension_module_template = environment.get_template("extension_module.j2")

    return extension_module_template.render({"module": module})


def render_setup_script(package):
    """
    Renders a setup script

    Parameters
    package: the package to be created
    """

    new_setup_script_template = environment.get_template("new_setup_script.j2")

    return new_setup_script_template.render({"package": package})
