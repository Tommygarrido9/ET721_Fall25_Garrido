"""
Tommy Garrido
Lab 9, file operations (testfile)
Oct 15, 2025
"""

import unittest
import os
from file_operations import *

class TestFileOperations(unittest.TestCase):
    def setUp(self):
        # Set up temporary test file name before each test
        self.file_name = "testfile.txt"
        self.msg = "Tommy Garrido"

    def tearDown(self):
        # remove the test file after each test
        if os.path.exists(self.file_name):
            os.remove(self.file_name)

    def test_write_file(self):
        # test writing text to a file
        msg = "Tommy Garrido"
        with open(self.file_name, "w") as f:
            f.write(msg)

        # verify file exits and content matches
        self.assertTrue(os.path.exists(self.file_name))
        with open(self.file_name, "r") as f:
            result = f.read()

        self.assertEqual(result,msg)

    def test_read_file(self):
        # test reading text from a file
        expected_content = "Read me!"
        with open(self.file_name, "w") as f:
            f.write(expected_content)
        with open(self.file_name, "r") as f:
            data = f.read()
        
        self.assertEqual(data, expected_content)

    def test_append_file(self):
        # test appending text to an existing file
        initial_content = "Line one"
        append_content = "\nLine two"

        with open(self.file_name, "w") as f:
            f.write(initial_content)

        with open(self.file_name, "a") as f:
            f.write(append_content)

        with open(self.file_name, "r") as f:
            final_data = f.read()
        
        self.assertEqual(final_data, initial_content + append_content)

    def test_email_read(self):
        content = "ncarter@yahoo.com\naparker@gmail.com\ncpeterson@hotmail.com"
        with open(self.file_name, "w") as f:
            f.write(content)
        file_test1 = email_read(self.file_name, "@gmail")
        file_test2 = email_read(self.file_name, "@hotmail")
        file_test3 = email_read(self.file_name, "@yahoo")

        self.assertEqual(file_test1, 1)
        self.assertEqual(file_test2, 1)
        self.assertEqual(file_test3, 1)

# run the unit tests automatically when the fileis ran
if __name__ == "__main__":
    unittest.main()