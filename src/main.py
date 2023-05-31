import pygame
import sys
from Background import Background
from Frame import Frame
from Game import Game
from PlayersField import PlayersField


def main():
    newGame = Game()
    nowBack = Background()
    human = PlayersField(0)
    computer = PlayersField(Background.OFFSET)
    computer.populateGrid()
    human.drawRectangleHuman()
    nowBack.drawWholeBackground(human, computer, "Ваш ход!")
    computerTurn = False
    theEnd = False

    while True:
        if computer.numberOfEnemyShipsKilled == 10 and not theEnd:
            result = Frame()
            result.printResult("ПОРАЖЕНИЕ!")
            theEnd = True
            nowBack.drawWholeBackground(human, computer, False)
            pygame.display.update()

        elif human.numberOfEnemyShipsKilled == 10 and not theEnd:
            result = Frame()
            result.printResult("ВАША ПОБЕДА!")
            theEnd = True
            nowBack.drawWholeBackground(human, computer, False)
            pygame.display.update()

        elif computerTurn:
            nowBack.drawWholeBackground(human, computer, "Ход противника!")
            pygame.display.update()
            pygame.time.delay(1000)
            if computer.computerNextShot:
                computerTurn = computer.computerShots(newGame, human, computer.computerNextShot, nowBack)
            else:
                computerTurn = computer.computerShots(newGame, human, computer.coordinatesForShots, nowBack)
            if computer:
                nowBack.drawWholeBackground(human, computer, "Ваш ход!")
            pygame.display.update()
        else:
            nowBack.drawWholeBackground(human, computer, "Ваш ход!")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if (Background.leftMargin + Background.OFFSET * Background.cellSize < x < Background.leftMargin + (
                            10 + Background.OFFSET) * Background.cellSize) and (
                            Background.upperMargin < y < Background.upperMargin + 10 * Background.cellSize):
                        firedCell = ((x - Background.leftMargin + Background.cellSize) // (Background.cellSize),
                                     (y - Background.upperMargin + Background.cellSize) // (Background.cellSize))
                        if firedCell in nowBack.coorOfPoints or firedCell in nowBack.coorOfCrosses:
                            continue
                        computerTurn = not newGame.checkingShot(firedCell, human, computer, computerTurn, nowBack)
                    elif ((Background.WIDTH - Background.cellSize * 7) <= x <= (Background.WIDTH - Background.cellSize * 2)) and (Background.cellSize <= y <= (Background.cellSize * 3)):
                        pygame.quit()
                        sys.exit()
                    elif ((Background.cellSize * 2) <= x <= (Background.cellSize * 7)) and (Background.cellSize <= y <= (Background.cellSize * 3)):
                        instruct = Frame()
                        instruct.printInstruction()
                        nowBack.drawWholeBackground(human, computer, "Ваш ход!")
                        pygame.display.update()
            pygame.display.update()


if __name__ == '__main__':
    main()
