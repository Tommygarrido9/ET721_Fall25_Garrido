"""
Tommy Garrido
October 8th, 2025
Lab 9, tet input and output data
unit test
"""

import unittest
from unittest.mock import patch
import io
import studentgrade_Garrido

class TestMainFunction(unittest.TestCase):
    # test with valid input with 3 students and three grades
    @patch('builtins.inpuut', side_effect=('3','85','90'))
    # capture the printed output
    @patch('sys.stdout', new_callable=io.StringIO)

    # define a function to test the input and output
    def test_valid_input(self, mock_stdout, mock_input):
        #call the main fucntion from file 'studentgrade_Garrido.py'
        studentgrade_Garrido.main()
        # retrieve the captured output
        output = mock_stdout.getvalue()
        # checkif the printed output contains the expected average
        self.assertIn("The class average is 83.33", output)

    #test with invalid input, then valid
    @patch('builtins.input', side_effect=('-1','0','2','95','80'))
    @patch('sys.stdout', new_callable=io.StringIO)
    
    def test_invalid_and_valid_input(self, mock_stdout, mock_input):
        studentgrade_Garrido.main()
        output = mock_stdout.getvalue()
        self.assertIn("Number of students must be greater than 0. Please try again", output)
        self.assertIn("Invalid input. Enter a grade between 0 and 100", output)
        self.assertIn("The class average is 87.50", output)
    
    # EXERCISE: create a unittest for invalid data type, for example when the user inputs strings.
    @patch('builtins.input', side_effect=('three', '2', '90', '65'))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_type(self, mock_stdout, mock_input):
        studentgrade_Garrido.main()
        output = mock_stdout.getvalue()
        self.assertIn("Invalid input. Please enter a positive integer.", output)
        self.assertIn("Invalid input. Please enter a numerical value.", output)
        self.assertIn("Class average is 77.50", output)
    
    # EXERCISE 2
    @patch('builtins.input', side_effect=['Peter', '2', '90', '100'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_name_instead_of_num(self, mock_stdout, mock_input):
        studentgrade_Garrido.main()
        output = mock_stdout.getvalue()
        self.assertIn("Invalid input. Please enter a positive integer.", output)
        self.assertIn("Invalid input. Please enter a numerical value.", output)
        self.assertIn("The class average is 95,00", output)

    @patch("builtins.input", side_effect=['2', 'Peter', '90', '85'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_name_instead_of_grade(self, mock_stdout, mock_input):
        studentgrade_Garrido.main()
        output = mock_stdout.getvalue()
        self.assertIn("Invalid input. Please enter a numerical value.", output)
        self.assertIn("The class average is 87.50", output)


if __name__ == "__main__":
    unittest.main()
