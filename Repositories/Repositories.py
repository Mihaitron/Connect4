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

        '''
            Returns the board
        '''

        return self.__board

    def getCollumn(self, destination):

        '''
            Returns a collumn given by it's letter index
        '''

        return self.__board[ord(destination) - ord("a")]

    def getPinsNumbers(self):

        '''
            Returns the number of pins on all the collumns
        '''

        return self.__pinsNumbers

    def getPinsNumber(self, destination):

        '''
            Returns the number of pins on a collumn given by its letter index
        '''

        return self.__pinsNumbers[ord(destination) - ord("a")]

    def getTranspose(self):

        '''
            Returns the transpose of the board matrix
        '''

        return [[self.__board[collumn][row] for collumn in range(len(self.__board))] for row in range(len(self.__board[0]))]

    def setPinsNumbers(self, newPinsNumbers):

        '''
            Sets the number of pins of all the collumns to a new number of pins
        '''

        self.__pinsNumbers = newPinsNumbers

    def setPinsNumber(self, collumn, newNumber):

        '''
            Sets the number of pins of a collumn given by a letter index to a new number
        '''

        self.__pinsNumbers[ord(collumn) - ord("a")] = newNumber

    def setBoard(self, board):

        '''
            Sets the board to a new board
        '''

        self.__board = board

    def setCollumn(self, destination, collumn):

        '''
            Sets a collumn given by its letter index to a new collumn
        '''

        self.__board[ord(destination) - ord("a")] = collumn