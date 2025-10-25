import unittest
import os
from main import *

class TestMain(unittest.TestCase):
    def setUp(self):
        self.game = Connect4()

    def test_Horizontal_Win(self):
        for i in range(4):
            self.game.board[5][i] = 'X'
            self.assertTrue(self.game.check_win('X'))
            self.assertTrue(self.game.check_win('O'))
        for i in range(4):
            self.game.board[5][i] = 'O'
            self.assertTrue(self.game.check_win('X'))
            self.assertTrue(self.game.check_win('O'))


    def test_Vertical_win(self):
        for i in range(4):
            self.game.board[5-i][0] = 'X'
            self.assertTrue(self.game.check_win('X'))
            self.assertTrue(self.game.check_win('O'))
        for i in range(4):
            self.game.board[5-i][0] = 'O'
            self.assertTrue(self.game.check_win('X'))
            self.assertTrue(self.game.check_win('O'))

    def test_Upright_Diagonal_win(self):
        for i in range(4):
            self.game.board[i][i] = 'X'
            self.assertTrue(self.game.check_win('X'))
            self.assertTrue(self.game.check_win('O'))
        for i in range(4):
            self.game.board[i][i] = 'O'
            self.assertTrue(self.game.check_win('X'))
            self.assertTrue(self.game.check_win('O'))


    def test_Downright_Diagonal_win(self):
        for i in range(4):
            self.game.board[5-i][i] = 'X' 
            self.assertTrue(self.game.check_win('X'))
            self.assertTrue(self.game.check_win('O'))
        for i in range(4):
            self.game.board[5-i][i] = 'O' 
            self.assertTrue(self.game.check_win('X'))
            self.assertTrue(self.game.check_win('O'))


    def test_No_Win(self):
        self.game.board[5][0] = 'X'
        self.game.board[5][1] = 'O'
        self.game.board[5][2] = 'X'
        self.game.board[5][3] = 'O'
        self.assertFalse(self.game.check_win('X'))
        self.assertFalse(self.game.check_win('O'))


        