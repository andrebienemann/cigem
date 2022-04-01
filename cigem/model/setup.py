import re
from pathlib import Path


class Setup:
    """
    A container class for a setup script
    """

    re_package_name = re.compile(r"name=\"([a-z]*)\"")
    re_setup_function = re.compile(r"setup\(((?:.*|\n)*)\)")

    def __init__(self, package_name: str, setup_script: str, setup_function):
        """
        Parameters
        package_name: the name of the package
        setup_script: the content of the setup script
        setup_function: the setup function inside of the setup script
        """

        self.package_name = package_name
        self.setup_script = setup_script
        self.setup_function = setup_function

    @classmethod
    def make_setup(cls, path: Path):
        """
        Mekes a setup

        Parameters
        path: the path to the root of the package
        """

        setup_script = path.joinpath("setup.py").read_text()

        setup_function_matches = cls.re_setup_function.findall(setup_script)
        if not setup_function_matches:
            raise Exception
        setup_function = setup_function_matches[0]

        package_name_matches = cls.re_package_name.findall(setup_function)
        if not package_name_matches:
            raise Exception
        package_name = package_name_matches[0]

        return cls(package_name, setup_script, setup_function)
