from Repositories.Repositories import RepositoryGame

class ValidatorGame(object):

    def validateMove(self, pinsNumber):
        if pinsNumber == 6:
            return False
        return True
