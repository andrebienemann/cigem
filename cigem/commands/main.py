import click

from cigem.commands.add import add
from cigem.commands.build import build
from cigem.commands.create import create
from cigem.commands.install import install
from cigem.commands.test import test


@click.group()
def main():
    pass


main.add_command(add)
main.add_command(build)
main.add_command(create)
main.add_command(install)
main.add_command(test)


if __name__ == "__main__":
    main()
