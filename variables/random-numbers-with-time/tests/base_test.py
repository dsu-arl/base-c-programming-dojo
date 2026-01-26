import os
import sys
import unittest
from tempfile import NamedTemporaryFile

# Add the challenge directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from paceCParser.parser import parse_file, retrieve_function_body


class BaseTestValidator(unittest.TestCase):
    """Base test class for C file verification tests.

    Provides helper methods for creating temporary C files and
    running verification checks against them.
    """

    def create_temp_c_file(self, c_code: str) -> str:
        """Create a temporary C file with the given code.

        Args:
            c_code: The C source code to write to the file.

        Returns:
            The path to the temporary file.
        """
        temp_file = NamedTemporaryFile(
            mode="w", suffix=".c", encoding="utf-8", delete=False
        )
        temp_file.write(c_code)
        temp_file.close()

        self.addCleanup(lambda: os.unlink(temp_file.name))

        return temp_file.name

    def parse_c_file(self, filepath: str):
        """Parse a C file and return its contents.

        Args:
            filepath: Path to the C file.

        Returns:
            The parsed file contents.
        """
        return parse_file(filepath)

    def get_main_function_contents(self, filepath: str):
        """Get the contents of the main function from a C file.

        Args:
            filepath: Path to the C file.

        Returns:
            The parsed contents of the main function.
        """
        file_contents = parse_file(filepath)
        main_function = {
            "function_name": "main",
            "return_type": "int",
            "parameters": [],
        }
        return retrieve_function_body(file_contents, **main_function)
