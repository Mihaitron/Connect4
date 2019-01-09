from termcolor import colored
import random

class ServiceGame(object):

    def __init__(self, validatorGame, repositoryGame):

        self.__validatorGame = validatorGame
        self.__repositoryGame = repositoryGame

    def getPinsNumbers(self, move):

        return self.__repositoryGame.getPinsNumbers()[ord(move) - ord("a")]

    def __closeToWin(self, player, list, index):
        if list[index] == player and list[index + 1] == player and list[index + 2] == player and list[index + 3] == "Z":
            return True
        elif list[index] == player and list[index + 1] == player and list[index + 2] == "Z" and list[index + 3] == player:
            return True
        elif list[index] == player and list[index + 1] == "Z" and list[index + 2] == player and list[index + 3] == player:
            return True
        elif list[index] == "Z" and list[index + 1] == player and list[index + 2] == player and list[index + 3] == player:
            return True
        return False

    def __fourInRow(self, player, board):

        for row in board:
            for element in range(len(row) - 3):
                if row[element] == player and row[element + 1] == player and row[element + 2] == player and row[element + 3] == player:
                    return True
        return False

    def __fourInDiagonal(self, player):

        board = self.__repositoryGame.getBoard()
        board = [[board[collumn][row] for collumn in range(len(board))] for row in range(len(board[0]))]

        for i in range(len(board) - 3):
            for j in range(len(board[0]) - 3):
                if board[i][j] == player and board[i + 1][j + 1] == player and board[i + 2][j + 2] == player and board[i + 3][j + 3] == player:
                    return True

        for i in range(len(board) - 1, 2, -1):
            for j in range(len(board[0]) - 3):
                if board[i][j] == player and board[i - 1][j + 1] == player and board[i - 2][j + 2] == player and board[i - 3][j + 3] == player:
                    return True
        return False

    def __checkRow(self, player):

        board = self.__repositoryGame.getBoard()
        board = [[board[collumn][row] for collumn in range(len(board))] for row in range(len(board[0]))]

        choices = []

        for row in board:
            for index in range(len(row) - 3):
                if self.__closeToWin(player, row, index):
                    if row[index] == "Z":
                        choices += chr(ord("a") + index)
                    elif row[index + 1] == "Z":
                        choices += chr(ord("a") + index + 1)
                    elif row[index + 2] == "Z":
                        choices += chr(ord("a") + index + 2)
                    elif row[index + 3] == "Z":
                        choices += chr(ord("a") + index + 3)

        return choices

    def __checkCollumn(self, player):

        board = self.__repositoryGame.getBoard()

        choices = []

        for index1 in range(len(board)):
            for index2 in range(len(board[index1]) - 3):
                if self.__closeToWin(player, board[index1], index2):
                    choices += chr(ord("a") + index1)

        return choices

    def __checkDiagonal(self, player):

        board = self.__repositoryGame.getBoard()
        board = [[board[collumn][row] for collumn in range(len(board))] for row in range(len(board[0]))]

        choices = []

        for i in range(len(board) - 3):
            for j in range(len(board[0]) - 3):
                checks = [board[i][j], board[i+1][j+1], board[i+2][j+2], board[i+3][j+3]]
                if self.__closeToWin(player, checks, 0):
                    choices += chr(ord("a") + i)

        for i in range(len(board) - 1, 2, -1):
            for j in range(len(board[0]) - 3):
                checks = [board[i][j], board[i - 1][j + 1], board[i - 2][j + 2], board[i - 3][j + 3]]
                if self.__closeToWin(player, checks, 0):
                    choices += chr(ord("a") + len(board) - i + 2)

        return choices

    def __canBlock(self):
        pass

    def __possibleChoices(self):

        choices = []

        choices += self.__checkRow("X")
        choices += self.__checkCollumn("X")
        '''
        choices += self.__checkDiagonal("X")
        '''
        choices += self.__checkRow("Y")
        choices += self.__checkCollumn("Y")
        '''
        choices += self.__checkDiagonal("Y")
        '''


        if len(choices) == 0:
            choices = ["a", "b", "c", "d", "e", "f", "g"]
        print(choices)
        return choices

    def isGameOver(self):
        board1 = self.__repositoryGame.getBoard()
        board2 = [[board1[collumn][row] for collumn in range(len(board1))] for row in range(len(board1[0]))]

        if self.__fourInRow("X", board1) or self.__fourInRow("X", board2) or self.__fourInDiagonal("X"):
            return 1
        elif self.__fourInRow("Y", board1) or self.__fourInRow("Y", board2) or self.__fourInDiagonal("Y"):
            return 2
        return 0

    def placeSymbol(self, symbol, destination):

        index = 5
        collumn = self.__repositoryGame.getCollumn(destination)
        while collumn[index] != "Z" and index >= 0:
            index -= 1
        collumn[index] = symbol
        self.__repositoryGame.setCollumn(destination, collumn)
        self.__repositoryGame.setPinsNumber(destination, self.__repositoryGame.getPinsNumbers()[ord(destination) - ord("a")] + 1)

    def aiPlay(self):
        choices = self.__possibleChoices()
        self.placeSymbol("Y", random.choice(choices))

    def wipeBoard(self):

        board = self.__repositoryGame.getBoard()
        pinsNumbers = [0, 0, 0, 0, 0, 0, 0]


        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = "Z"

        self.__repositoryGame.setBoard(board)
        self.__repositoryGame.setPinsNumbers(pinsNumbers)

    def printBoard(self):
        collumns = "abcdefg"
        board = self.__repositoryGame.getBoard()
        board = [[board[collumn][row] for collumn in range(len(board))] for row in range(len(board[0]))]
        print(colored(collumns, "yellow"))
        for collumn in range(len(board)):
            for row in range(len(board[0])):
                if board[collumn][row] == "X":
                    print(colored(board[collumn][row], "red"), end="")
                elif board[collumn][row] == "Y":
                    print(colored(board[collumn][row], "blue"), end="")
                else:
                    print(colored(board[collumn][row], "white"), end="")
            print()
