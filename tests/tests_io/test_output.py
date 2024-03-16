import unittest
import os
from app.io.output import write_file


class TestOutput(unittest.TestCase):
    def test_write_file(self):
        write_file("./test_data/test_output.txt", "Test file content")
        with open("./test_data/test_output.txt", "r") as file:
            self.assertEqual(file.read(), "Test file content")

    def tearDown(self):
        os.remove("./test_data/test_output.txt")
