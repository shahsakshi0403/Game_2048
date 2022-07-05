from Grid_3       import Grid
from ComputerAI_3 import ComputerAI
from PlayerAI_3   import PlayerAI
from Displayer_3  import Displayer
from random       import randint
from colored import fg
import time


defaultInitialTiles = 2
defaultProbability = 0.9

actionDic = {
    0: "UP",
    1: "DOWN",
    2: "LEFT",
    3: "RIGHT"
}

(PLAYER_TURN, COMPUTER_TURN) = (0, 1)

timeLimit = 0.2
allowance = 0.05

class GameManager:
    def __init__(self, size = 4):
        self.grid = Grid(size)
        self.possibleNewTiles = [2, 4]
        self.probability = defaultProbability
        self.initTiles  = defaultInitialTiles
        self.computerAI = None
        self.playerAI   = None
        self.displayer  = None
        self.over       = False

    def setComputerAI(self, computerAI):
        self.computerAI = computerAI

    def setPlayerAI(self, playerAI):
        self.playerAI = playerAI

    def setDisplayer(self, displayer):
        self.displayer = displayer

    def updateAlarm(self, currTime):
        if currTime - self.prevTime > timeLimit + allowance:
            self.over = True
        else:
            while time.time() - self.prevTime < timeLimit + allowance:
                pass

            self.prevTime = time.time()

    def start(self):
        for i in range(self.initTiles):
            self.insertRandonTile()

        self.displayer.display(self.grid)


        turn = PLAYER_TURN
        maxTile = 0

        self.prevTime = time.time()

        while not self.isGameOver() and not self.over:

            gridCopy = self.grid.clone()

            move = None

            if turn == PLAYER_TURN:
                print((fg(204)),"Computer 2's Turn:", end="")
                move = self.playerAI.getMove(gridCopy)
                print(actionDic[move])


                if move != None and move >= 0 and move < 4:
                    if self.grid.canMove([move]):
                        self.grid.move(move)

                        
                        maxTile = self.grid.getMaxTile()
                    else:
                        print("Invalid PlayerAI Move")
                        self.over = True
                else:
                    print("Invalid PlayerAI Move - 1")
                    self.over = True
            else:
                print((fg(141)),"Computer 1's turn:")
                move = self.computerAI.getMove(gridCopy)

            
                if move and self.grid.canInsert(move):
                    self.grid.setCellValue(move, self.getNewTileValue())
                else:
                    print("Invalid Computer AI Move")
                    self.over = True

            if not self.over:
                self.displayer.display(self.grid)

            
            self.updateAlarm(time.time())

            turn = 1 - turn
        print("Score : ")
        print( maxTile)

    def isGameOver(self):
        return not self.grid.canMove()

    def getNewTileValue(self):
        if randint(0,99) < 100 * self.probability:
            return self.possibleNewTiles[0]
        else:
            return self.possibleNewTiles[1];

    def insertRandonTile(self):
        tileValue = self.getNewTileValue()
        cells = self.grid.getAvailableCells()
        cell = cells[randint(0, len(cells) - 1)]
        self.grid.setCellValue(cell, tileValue)

def main():
    gameManager = GameManager()
    playerAI  	= PlayerAI()
    computerAI  = ComputerAI()
    displayer 	= Displayer()

    gameManager.setDisplayer(displayer)
    gameManager.setPlayerAI(playerAI)
    gameManager.setComputerAI(computerAI)
    gameManager.start()

if __name__ == '__main__':
    main()
