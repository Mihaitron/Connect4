from termcolor import colored
import random

class ServiceGame(object):

    def __init__(self, validatorGame, repositoryGame):

        self.__validatorGame = validatorGame
        self.__repositoryGame = repositoryGame

    def getPinsNumbers(self, move):

        '''
            Returns the number of pins on a collumn
        '''

        return self.__repositoryGame.getPinsNumbers()[ord(move) - ord("a")]

    def closeToWin(self, player, list, index):

        '''
            Returns True if the given list is of the type "XXXZ", "XXZX", "XZXX" or "ZXXX" and False otherwise
        '''

        if list[index] == player and list[index + 1] == player and list[index + 2] == player and list[index + 3] == "Z":
            return True
        elif list[index] == player and list[index + 1] == player and list[index + 2] == "Z" and list[index + 3] == player:
            return True
        elif list[index] == player and list[index + 1] == "Z" and list[index + 2] == player and list[index + 3] == player:
            return True
        elif list[index] == "Z" and list[index + 1] == player and list[index + 2] == player and list[index + 3] == player:
            return True
        return False

    def fourInRow(self, player, board):

        '''
            Checks if there are four pins in a row, for a given player, on the board
        '''

        for row in board:
            for element in range(len(row) - 3):
                if row[element] == player and row[element + 1] == player and row[element + 2] == player and row[element + 3] == player:
                    return True
        return False

    def fourInDiagonal(self, player):

        '''
            Checks if there are four pins on a diagonal, for a given player, on the board
        '''

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

    def getRightCollumn(self, rowIndex):

        '''
            Returns a collumn based on a given row index, provided that, on the row, there is a series like this: "XXXZ", "XXZX", "XZXX" or "ZXXX"
        '''


        board = self.__repositoryGame.getBoard()

        for index in range(len(board) - 3):
            if board[index][rowIndex] == "X" and board[index + 1][rowIndex] == "X" and board[index + 2][rowIndex] == "X" and board[index + 3][rowIndex] == "Z":
                return board[index + 3]
            elif board[index][rowIndex] == "X" and board[index + 1][rowIndex] == "X" and board[index + 2][rowIndex] == "Z" and board[index + 3][rowIndex] == "X":
                return board[index + 2]
            elif board[index][rowIndex] == "X" and board[index + 1][rowIndex] == "Z" and board[index + 2][rowIndex] == "X" and board[index + 3][rowIndex] == "X":
                return board[index + 1]
            elif board[index][rowIndex] == "Z" and board[index + 1][rowIndex] == "X" and board[index + 2][rowIndex] == "X" and board[index + 3][rowIndex] == "X":
                return board[index]


    def checkRow(self, player):

        '''
            Checks to see if a given player is close to winning on a row, then adds a choice for the computer based on the check
        '''

        boardTranspose = self.__repositoryGame.getTranspose()

        choices = []

        for row in boardTranspose:
            for index in range(len(row) - 3):
                if self.closeToWin(player, row, index):
                    print("yes")
                    for elementIndex in range(len(boardTranspose)):
                        if boardTranspose[elementIndex] == row:
                            rowIndex = elementIndex
                            break

                    collumn = self.getRightCollumn(rowIndex)

                    if self.canBlock(rowIndex, collumn):
                        if row[index] == "Z":
                            choices += chr(ord("a") + index)
                        elif row[index + 1] == "Z":
                            choices += chr(ord("a") + index + 1)
                        elif row[index + 2] == "Z":
                            choices += chr(ord("a") + index + 2)
                        elif row[index + 3] == "Z":
                            choices += chr(ord("a") + index + 3)

        return choices

    def checkCollumn(self, player):

        '''
            Checks to see if a given player is close to winning on a collumn, then adds a choice for the computer based on the check
        '''

        board = self.__repositoryGame.getBoard()

        choices = []

        for index1 in range(len(board)):
            for index2 in range(len(board[index1]) - 3):
                if self.closeToWin(player, board[index1], index2):
                    choices += chr(ord("a") + index1)

        return choices

    def canBlock(self, rowIndex, collumn):

        '''
            Checks to see if the computer can block the player's move
        '''

        index = len(collumn) - 1

        while index > rowIndex:
            if collumn[index] == "Z":
                return False
            index -= 1
        return True

    def possibleChoices(self):

        '''
            Makes a choice list from which the computer choses from when making it's moves
        '''

        choices = []

        choices += self.checkRow("X")
        choices += self.checkCollumn("X")
        choices += self.checkCollumn("Y")

        if len(choices) == 0:
            choices = ["a", "b", "c", "d", "e", "f", "g"]
        return choices

    def isGameOver(self):

        '''
            Checks if the game is over
        '''

        board = self.__repositoryGame.getBoard()
        boardTranspose = self.__repositoryGame.getTranspose()

        if self.fourInRow("X", board) or self.fourInRow("X", boardTranspose) or self.fourInDiagonal("X"):
            return 1
        elif self.fourInRow("Y", board) or self.fourInRow("Y", boardTranspose) or self.fourInDiagonal("Y"):
            return 2
        return 0

    def placeSymbol(self, symbol, destination):

        '''
            Places the symbol "X" for the player or "Y" for the computer on a given collumn
        '''

        index = 5
        collumn = self.__repositoryGame.getCollumn(destination)

        while collumn[index] != "Z" and index >= 0:
            index -= 1

        collumn[index] = symbol

        self.__repositoryGame.setCollumn(destination, collumn)
        self.__repositoryGame.setPinsNumber(destination, self.__repositoryGame.getPinsNumbers()[ord(destination) - ord("a")] + 1)

    def aiPlay(self):

        '''
            Places a pin on a ranom choice based on a list of available choices
        '''

        choices = self.possibleChoices()
        self.placeSymbol("Y", random.choice(choices))

    def wipeBoard(self):

        '''
            Resets the board and the number of pins when starting a new game
        '''

        board = self.__repositoryGame.getBoard()
        pinsNumbers = [0, 0, 0, 0, 0, 0, 0]


        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = "Z"

        self.__repositoryGame.setBoard(board)
        self.__repositoryGame.setPinsNumbers(pinsNumbers)

    def printBoard(self):

        '''
            Prints the board
        '''

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
