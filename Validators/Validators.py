class ValidatorGame(object):

    def validateMove(self, pinsNumber):

        '''
            Checks if the number of pins is 6
        '''

        if pinsNumber == 6:
            return False
        return True
