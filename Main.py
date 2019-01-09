from Console.Console import Console
from Services.Services import ServiceGame
from Validators.Validators import ValidatorGame
from Repositories.Repositories import RepositoryGame

repositoryGame = RepositoryGame()
validatorGame = ValidatorGame()
serviceGame = ServiceGame(validatorGame, repositoryGame)
Console = Console(serviceGame)

Console.run()
