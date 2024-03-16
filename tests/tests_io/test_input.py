import unittest
import pandas as pd
from app.io.input import read_file, read_file_pandas


class TestInput(unittest.TestCase):
    def test_read_file(self):
        self.assertEqual(read_file("./test_data/test.txt"), "Test file content")

    def test_read_file_does_not_exist(self):
        with self.assertRaises(FileNotFoundError):
            read_file("./test_data/does_not_exist.txt")

    def test_read_file_empty(self):
        self.assertEqual(read_file("./test_data/empty.txt"), "")

    def test_read_file_pandas(self):
        self.assertEqual(read_file_pandas("./test_data/test.csv").shape, (2, 3))
        self.assertEqual(read_file_pandas("./test_data/test.csv").iloc[0, 0], 1)
        self.assertEqual(read_file_pandas("./test_data/test.csv").iloc[0, 1], "Test1")

    def test_read_file_pandas_does_not_exist(self):
        with self.assertRaises(FileNotFoundError):
            read_file_pandas("./test_data/does_not_exist.csv")

    def test_read_file_pandas_empty(self):
        with self.assertRaises(pd.errors.EmptyDataError):
            read_file_pandas("./test_data/empty.csv")
