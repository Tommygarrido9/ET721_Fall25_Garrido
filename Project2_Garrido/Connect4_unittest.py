import unittest
import os
from main import *

class TestMain(unittest.TestCase):
    def setUp(self):
        self.game = Connect4()

    def test_Horizontal_Win_X(self):
        for i in range(4):
            self.game.board[5][i] = 'X'
        self.assertTrue(self.game.check_win('X'))
        self.assertFalse(self.game.check_win('O'))
    
    def test_Horizontal_Win_O(self):   
        for i in range(4):
            self.game.board[5][i] = 'O'
        self.assertFalse(self.game.check_win('X'))
        self.assertTrue(self.game.check_win('O'))

    def test_Vertical_Win_X(self):
        for i in range(4):
            self.game.board[5-i][0] = 'X'
        self.assertTrue(self.game.check_win('X'))
        self.assertFalse(self.game.check_win('O'))
    
    def test_Vertical_Win_O(self):
        for i in range(4):
            self.game.board[5-i][0] = 'O'
        self.assertFalse(self.game.check_win('X'))
        self.assertTrue(self.game.check_win('O'))

    def test_Upright_Diagonal_Win_X(self):
        for i in range(4):
            self.game.board[i][i] = 'X'
        self.assertTrue(self.game.check_win('X'))
        self.assertFalse(self.game.check_win('O'))

    def test_Upright_Diagonal_Win_O(self):
        for i in range(4):
            self.game.board[i][i] = 'O'
        self.assertFalse(self.game.check_win('X'))
        self.assertTrue(self.game.check_win('O'))

    def test_Downright_Diagonal_Win_X(self):
        for i in range(4):
            self.game.board[5-i][i] = 'X' 
        self.assertTrue(self.game.check_win('X'))
        self.assertFalse(self.game.check_win('O'))
    
    def test_Downright_Diagonal_Win_O(self):
        for i in range(4):
            self.game.board[5-i][i] = 'O' 
        self.assertFalse(self.game.check_win('X'))
        self.assertTrue(self.game.check_win('O'))


    def test_No_Win(self):
        self.game.board[5][0] = 'X'
        self.game.board[5][1] = 'O'
        self.game.board[5][2] = 'X'
        self.game.board[5][3] = 'O'
        self.assertFalse(self.game.check_win('X'))
        self.assertFalse(self.game.check_win('O'))

if __name__ == "__main__":
    unittest.main()

"""
All of my tests that I ran have all come back OK. There were a few errors in the code, for example, I accidentally placed the assert statements
inside of the for loop which caused some errors. I also had an error where I set both statements for X and O to assertTrue which lead to an error
where the test could not determine which one was supposed to be the winner. I fixed this by changing the statements around depending 
on the unittest for which player wins.
"""
        