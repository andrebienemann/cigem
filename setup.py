from setuptools import setup


def get_long_description():
    return open("README.md", "r").read()


setup(
    name="cigem",
    version="0.1.0",
    description="Cenventional Interface Generator for Extension Modules",
    long_description=get_long_description(),
    license="MIT",
    author="André Bienemann",
    author_email="andre.bienemann@gmail.com",
    url="https://github.com/andrebienemann/cigem",
    install_requires=["click", "jinja2"],
    packages=["cigem", "cigem/commands", "cigem/core", "cigem/model"],
    entry_points={"console_scripts": ["cigem=cigem:main"]},
    package_data={"": ["templates/*"]},
)
