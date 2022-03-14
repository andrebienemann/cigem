import os

from jinja2 import Environment, FileSystemLoader

templates_path = os.path.join(os.path.dirname(__file__), "../templates")
environment = Environment(loader=FileSystemLoader(templates_path))

extension_module_template = environment.get_template("extension_module.j2")


def render_extension_module(module):
    return extension_module_template.render({"module": module})
