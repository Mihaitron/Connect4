from Repositories.Repositories import RepositoryGame
from Validators.Validators import ValidatorGame
from Services.Services import ServiceGame
import unittest

class Tests(unittest.TestCase):

    def setUp(self):

        self.__repositoryGame = RepositoryGame()
        self.__validatorGame = ValidatorGame()
        self.__serviceGame = ServiceGame(self.__validatorGame, self.__repositoryGame)

    def testGetters(self):

        '''
            Tests the implemented getters
        '''

        board = [
                    ["Z", "Z", "Z", "Z", "Z", "Z"],
                    ["Z", "Z", "Z", "Z", "Z", "Z"],
                    ["Z", "Z", "Z", "Z", "Z", "Z"],
                    ["Z", "Z", "Z", "Z", "Z", "Z"],
                    ["Z", "Z", "Z", "Z", "Z", "Z"],
                    ["Z", "Z", "Z", "Z", "Z", "Z"],
                    ["Z", "Z", "Z", "Z", "Z", "Z"]
                ]
        transpose = [
                        ["Z", "Z", "Z", "Z", "Z", "Z", "Z"],
                        ["Z", "Z", "Z", "Z", "Z", "Z", "Z"],
                        ["Z", "Z", "Z", "Z", "Z", "Z", "Z"],
                        ["Z", "Z", "Z", "Z", "Z", "Z", "Z"],
                        ["Z", "Z", "Z", "Z", "Z", "Z", "Z"],
                        ["Z", "Z", "Z", "Z", "Z", "Z", "Z"],
                    ]
        pinsNumbers = [0, 0, 0, 0, 0, 0, 0]
        collumn = ["Z", "Z", "Z", "Z", "Z", "Z"]

        self.assertEqual(self.__repositoryGame.getBoard(), board)
        self.assertEqual(self.__repositoryGame.getCollumn("a"), collumn)
        self.assertEqual(self.__repositoryGame.getPinsNumbers(), pinsNumbers)
        self.assertEqual(self.__repositoryGame.getTranspose(), transpose)
        self.assertEqual(self.__repositoryGame.getPinsNumber("a"), 0)

    def testSetters(self):

        '''
            Tests the implemented setters
        '''

        newPinsNumbers = [1, 1, 1, 1, 1, 1, 1]
        newBoard = [
                    ["Z", "Z", "Z", "Z", "Z", "X"],
                    ["Z", "Z", "Z", "Z", "Y", "X"],
                    ["Z", "Z", "Z", "Z", "Y", "Y"],
                    ["Z", "Z", "Z", "Z", "Z", "X"],
                    ["Z", "Z", "Z", "Z", "Z", "Z"],
                    ["Z", "Z", "Z", "Z", "Z", "Z"],
                    ["Z", "Z", "Z", "Z", "Z", "Z"]
                    ]
        newCollumn = ["Z", "Z", "Z", "Z", "Z", "Y"]

        self.__repositoryGame.setPinsNumbers(newPinsNumbers)
        self.assertEqual(self.__repositoryGame.getPinsNumbers(), newPinsNumbers)
        self.__repositoryGame.setPinsNumber("a", 3)
        self.assertEqual(self.__repositoryGame.getPinsNumber("a"), 3)
        self.__repositoryGame.setBoard(newBoard)
        self.assertEqual(self.__repositoryGame.getBoard(), newBoard)
        self.__repositoryGame.setCollumn("a", newCollumn)
        self.assertEqual(self.__repositoryGame.getCollumn("a"), newCollumn)

    def testValidators(self):

        '''
            Tests the implemented validators
        '''

        self.assertFalse(self.__validatorGame.validateMove(6))
        self.assertTrue(self.__validatorGame.validateMove(3))

    def testService(self):

        '''
            Tests the service part of the program
        '''

        list = ["Z", "Z", "Z", "X", "X", "X"]
        board = [
                    ["Z", "Z", "X", "X", "X", "X"],
                    ["Z", "Z", "Z", "X", "Z", "Z"],
                    ["Z", "Z", "Z", "X", "Z", "Z"],
                    ["Z", "Z", "Z", "Z", "Z", "X"],
                    ["Z", "Z", "Z", "Z", "X", "Y"],
                    ["Z", "Z", "Z", "Z", "X", "Y"],
                    ["Z", "Z", "Z", "Z", "X", "Y"]
                ]

        self.assertEqual(self.__serviceGame.getPinsNumbers("a"), 0)
        self.assertTrue(self.__serviceGame.closeToWin("X", list, 2))
        self.assertTrue(self.__serviceGame.fourInRow("X", board))
        self.assertFalse(self.__serviceGame.fourInDiagonal("Y"))
        self.assertFalse(self.__serviceGame.checkRow("X"))
        self.assertFalse(self.__serviceGame.checkCollumn("X"))
        self.assertFalse(self.__serviceGame.canBlock(0, ["Z", "Z", "Z", "Z", "X", "Y"]))
        self.assertEqual(self.__serviceGame.possibleChoices(), ["a", "b", "c", "d", "e", "f", "g"])
        self.assertFalse(self.__serviceGame.isGameOver())
