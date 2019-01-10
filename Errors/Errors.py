class MoveError(BaseException):

    def __init__(self, error):

        self.__error = error