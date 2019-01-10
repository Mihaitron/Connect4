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

        boardTranspose = self.__repositoryGame.getTranspose()

        for i in range(len(boardTranspose) - 3):
            for j in range(len(boardTranspose[0]) - 3):
                if boardTranspose[i][j] == player and boardTranspose[i + 1][j + 1] == player and boardTranspose[i + 2][j + 2] == player and boardTranspose[i + 3][j + 3] == player:
                    return True

        for i in range(len(boardTranspose) - 1, 2, -1):
            for j in range(len(boardTranspose[0]) - 3):
                if boardTranspose[i][j] == player and boardTranspose[i - 1][j + 1] == player and boardTranspose[i - 2][j + 2] == player and boardTranspose[i - 3][j + 3] == player:
                    return True
        return False

    def __getRightCollumn(self, rowIndex1, rowIndex2, rowIndex3, rowIndex4):

        board = self.__repositoryGame.getBoard()

        for index in range(len(board) - 3):
            if board[index][rowIndex1] == "X" and board[index + 1][rowIndex2] == "X" and board[index + 2][rowIndex3] == "X" and board[index + 3][rowIndex4] == "Z":
                return board[index + 3]
            elif board[index][rowIndex1] == "X" and board[index + 1][rowIndex2] == "X" and board[index + 2][rowIndex3] == "Z" and board[index + 3][rowIndex4] == "X":
                return board[index + 2]
            elif board[index][rowIndex1] == "X" and board[index + 1][rowIndex2] == "Z" and board[index + 2][rowIndex3] == "X" and board[index + 3][rowIndex4] == "X":
                return board[index + 1]
            elif board[index][rowIndex1] == "Z" and board[index + 1][rowIndex2] == "X" and board[index + 2][rowIndex3] == "X" and board[index + 3][rowIndex4] == "X":
                return board[index]


    def __checkRow(self, player):

        boardTranspose = self.__repositoryGame.getTranspose()

        choices = []

        for row in boardTranspose:
            for index in range(len(row) - 3):
                if self.__closeToWin(player, row, index):

                    for elementIndex in range(len(boardTranspose)):
                        if boardTranspose[elementIndex] == row:
                            rowIndex = elementIndex
                            break

                    collumn = self.__getRightCollumn(rowIndex, rowIndex, rowIndex, rowIndex)

                    if self.__canBlock(rowIndex, collumn):
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

    def __canBlock(self, rowIndex, collumn):

        index = len(collumn) - 1

        while index > rowIndex:
            if collumn[index] == "Z":
                return False
            index -= 1
        return True

    def __possibleChoices(self):

        choices = []

        choices += self.__checkRow("X")
        choices += self.__checkCollumn("X")
        choices += self.__checkRow("Y")
        choices += self.__checkCollumn("Y")

        if len(choices) == 0:
            choices = ["a", "b", "c", "d", "e", "f", "g"]
        return choices

    def isGameOver(self):

        board = self.__repositoryGame.getBoard()
        boardTranspose = self.__repositoryGame.getTranspose()

        if self.__fourInRow("X", board) or self.__fourInRow("X", boardTranspose) or self.__fourInDiagonal("X"):
            return 1
        elif self.__fourInRow("Y", board) or self.__fourInRow("Y", boardTranspose) or self.__fourInDiagonal("Y"):
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
        boardTranspose = self.__repositoryGame.getTranspose()

        print(colored(collumns, "yellow"))

        for collumn in range(len(boardTranspose)):
            for row in range(len(boardTranspose[0])):
                if boardTranspose[collumn][row] == "X":
                    print(colored(boardTranspose[collumn][row], "red"), end="")
                elif boardTranspose[collumn][row] == "Y":
                    print(colored(boardTranspose[collumn][row], "blue"), end="")
                else:
                    print(colored(boardTranspose[collumn][row], "white"), end="")
            print()
