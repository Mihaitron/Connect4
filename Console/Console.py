from Validators.Validators import ValidatorGame
import random

class Console(object):

    def __init__(self, serviceGame):

        self.__serviceGame = serviceGame

        self.__menuCommands = {
                                "start": self.__uiGame,
                                "help": self.__uiHelp
                              }

    def __uiPrintBoard(self):
        self.__serviceGame.printBoard()

    def __uiGame(self):

        actions = ["a", "b", "c", "d", "e", "f", "g"]
        self.__serviceGame.wipeBoard()

        while True:
            self.__uiPrintBoard()
            action = input(">")
            if action == "exit":
                return
            if action in actions:
                if ValidatorGame().validateMove(self.__serviceGame.getPinsNumbers(action)):
                    self.__serviceGame.placeSymbol("X", action)
                    if self.__serviceGame.isGameOver() == 1:
                        break
                    self.__serviceGame.aiPlay()
                    if self.__serviceGame.isGameOver() == 2:
                        break
                else:
                    print("Invalid action!")
            else:
                print("Invalid collumn!")

        self.__uiPrintBoard()

        if self.__serviceGame.isGameOver() == 1:
            print("YOU WIN!")
        else:
            print("YOU LOSE!")


    def __uiHelp(self):
        print('Your objective is to connect 4 "x" in a row (vertically, horizontally or diagonally) by inputing the collumn you want to drop your symbol on. The computer will try to beat you to it.')

    def run(self):
        while True:
            command = input(">")
            if command == "exit":
                return
            elif command in self.__menuCommands:
                    self.__menuCommands[command]()
            else:
                print("Unrecognized command!")