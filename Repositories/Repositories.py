class RepositoryGame(object):

    def __init__(self):
        self.__board = [
                        ["Z", "Z", "Z", "Z", "Z", "Z"],
                        ["Z", "Z", "Z", "Z", "Z", "Z"],
                        ["Z", "Z", "Z", "Z", "Z", "Z"],
                        ["Z", "Z", "Z", "Z", "Z", "Z"],
                        ["Z", "Z", "Z", "Z", "Z", "Z"],
                        ["Z", "Z", "Z", "Z", "Z", "Z"],
                        ["Z", "Z", "Z", "Z", "Z", "Z"]
                       ]
        self.__pinsNumbers = [0, 0, 0, 0, 0, 0, 0]

    def getBoard(self):
        return self.__board

    def getCollumn(self, destination):
        return self.__board[ord(destination) - ord("a")]

    def getPinsNumbers(self):
        return self.__pinsNumbers

    def setPinsNumbers(self, newPinsNumbers):
        self.__pinsNumbers = newPinsNumbers

    def setPinsNumber(self, pin, newNumber):
        self.__pinsNumbers[ord(pin) - ord("a")] = newNumber

    def setBoard(self, board):
        self.__board = board

    def setCollumn(self, destination, collumn):
        self.__board[ord(destination) - ord("a")] = collumn