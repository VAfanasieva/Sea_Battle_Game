import random
import pygame
import sys
from src.button import Button
from src.background import Background
from src.frame import Frame



class PlayersField():
    computerNextShot = []

    def __init__(self, offset):
        self.offset = offset
        self.numberOfEnemyShipsKilled = 0
        self.opponenOffset = (offset - Background.OFFSET) * (-1)
        self.coorOwnShips = []      # координаты собсвенных кораблей
        self.shipsKilled = []       # координаты убитых кораблей
        self.coorLiveCell = []      # координаты живых клеток
        self.damagedCells = [[], [], [], [], [], [], [], [], [], []]    #кординаты раненых кораблей
        self.coordinatesFree = [(x, y) for x in range(1 + self.offset, 11 + self.offset) for y in range(1, 11)]     # свободные ячейки
        self.coordinatesForShots = [(x, y) for x in range(1 + self.opponenOffset, 11 + self.opponenOffset) for y in range(1, 11)]       # координаты доступные для выстрелов

    def createShipComputer(self, numderOfCell, coordinatesFree):
        """создает корабль, клетки которого записаны в виде кордежа"""
        if not coordinatesFree:
            return []
        coordinatesShip = []                                # координаты корабля
        vector = random.randint(0, 1)                       # горизонтальный или вертикальный(х = 0 у = 1)
        direction = random.choice((-1, 1))                  # вверх или вниз, влево или вправо
        x, y = random.choice(tuple(coordinatesFree))        # выбор свободной координаты
        for _ in range(numderOfCell):
            coordinatesShip.append((x, y))                  # записываем координаты в кортеж
            if not vector:
                direction, x = self.addBlockToShip(x, direction, vector, coordinatesShip)
            else:
                direction, y = self.addBlockToShip(y, direction, vector, coordinatesShip)

        if set(coordinatesShip).issubset(coordinatesFree):
            return coordinatesShip
        return self.createShipComputer(numderOfCell, coordinatesFree)

    def addBlockToShip(self, coor, direction, vector, coordinatesShip):
        """возвращает новую клетку для корабля, которая она удовлетворяет требованиям - не выходит за рамки поля,
        иначе меняет напраление в противополжную сторону"""
        if (coor <= 1 - Background.OFFSET * Background.cellSize * vector and direction == -1) or (coor >= 10 + Background.OFFSET * Background.cellSize * vector and direction == 1):
            direction *= -1
            return direction, coordinatesShip[0][vector] + direction
        else:
            return direction, coordinatesShip[-1][vector] + direction

    def removeCoorFromFree(self, newShip):
        """удаляет все клетки вокруг корабля из свободных"""
        for coor in newShip:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 + self.offset < (coor[0] + i) < 11 + self.offset and 0 < (coor[1] + j) < 11 and (coor[0] + i, coor[1] + j) in self.coordinatesFree:           # не выходим ли за рамки сетки
                        self.coordinatesFree.remove((coor[0] + i, coor[1] + j))

    def populateGrid(self):
        """формирает корабли коспьютера"""
        for countCell in range(4, 0, -1):
             for _ in range(5 - countCell):
                 newShip = self.createShipComputer(countCell, self.coordinatesFree)
                 shipCopy = newShip.copy()
                 self.coorOwnShips.append(newShip)
                 self.coorLiveCell.append(shipCopy)
                 self.removeCoorFromFree(newShip)

    def drawRectangleHuman(self):
        """дает возможность игроку рисовать корабли"""
        drawship = True
        drawing = False
        startX, startY = 0, 0
        start = (0, 0)
        shipSize = (0, 0)
        numberOfDowned = [0, 0, 0, 0]

        while drawship:
            nowBack = Background()
            nowBack.drawBackground()
            exitButton = Button()
            rulesButton = Button()
            exitButton.drawButton(Background.WIDTH - 7 * Background.cellSize, "Выйти", nowBack)
            rulesButton.drawButton(2 * Background.cellSize, "Правила", nowBack)
            nowBack.sendMessage("Разместите корабли")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    drawing = True
                    startX, startY = event.pos
                    start = startX, startY
                    shipSize = (0, 0)
                    if ((Background.WIDTH - Background.cellSize * 7) <= startX <= (Background.WIDTH - Background.cellSize * 2)) and (Background.cellSize <= startY <= (Background.cellSize * 3)):
                        pygame.quit()
                        sys.exit()
                    if ((Background.cellSize * 2) <= startX <= (Background.cellSize * 7)) and (Background.cellSize <= startY <= (Background.cellSize * 3)):
                        instruct = Frame()
                        instruct.printInstruction()
                        nowBack.drawWholeBackground(self, self, False)
                        nowBack.sendMessage("Разместите корабли")
                        nowBack.drawShips(self.coorOwnShips)
                        pygame.display.update()
                elif drawing and event.type == pygame.MOUSEMOTION:
                    endX, endY = event.pos
                    shipSize = endX - startX, endY - startY
                elif drawing and event.type == pygame.MOUSEBUTTONUP:
                    endX, endY = event.pos
                    drawing = False
                    shipSize = (0, 0)
                    tempShip = self.creatingShip(startX, startY, endX, endY, nowBack)
                    if tempShip:
                        self.addShipToDraw(tempShip, numberOfDowned, nowBack)

                if len(self.coorOwnShips) == 10:
                    drawship = False

                pygame.draw.rect(Background.screen, Background.objectColor, (start, shipSize), Background.thicknessOfObjects)
                nowBack.drawShips(self.coorOwnShips)
                pygame.display.update()

    def addShipToDraw(self, tempShip, numberOfDowned, nowBack):
        if set(tempShip).issubset(self.coordinatesFree):
            if (5 - len(tempShip)) > numberOfDowned[len(tempShip) - 1]:
                numberOfDowned[len(tempShip) - 1] += 1
                tempShipCopy = tempShip.copy()
                self.coorOwnShips.append(tempShip)
                self.coorLiveCell.append(tempShipCopy)
                self.removeCoorFromFree(tempShip)
            else:
                Background.showErrorMessage(nowBack, f'Уже достаточно {len(tempShip)} кораблей!')
        else:
            Background.showErrorMessage(nowBack, f'Корабли соприкасаются!')

    def creatingShip(self, startX, startY, endX, endY, nowBack):
        tempShip = []  # временный корабль
        cellStart = ((startX + Background.cellSize - Background.leftMargin) // (Background.cellSize + 1),
                     (startY + Background.cellSize - Background.upperMargin) // (Background.cellSize + 1))
        cellEnd = ((endX + Background.cellSize - Background.leftMargin) // (Background.cellSize + 1),
                   (endY + Background.cellSize - Background.upperMargin) // (Background.cellSize + 1))
        if cellStart > cellEnd:
            cellStart, cellEnd = cellEnd, cellStart
        if 0 < cellStart[0] < 11 and 0 < cellStart[1] < 11 and 0 < cellEnd[0] < 11 and 0 < cellEnd[1] < 11:
            if cellStart[0] == cellEnd[0] and (cellEnd[1] - cellStart[1]) < 4:
                for cell in range(cellStart[1], cellEnd[1] + 1):
                    tempShip.append((cellStart[0], cell))
            elif cellStart[1] == cellEnd[1] and (cellEnd[0] - cellStart[0]) < 4:
                for cell in range(cellStart[0], cellEnd[0] + 1):
                    tempShip.append((cell, cellStart[1]))
            else:
                Background.showErrorMessage(nowBack, "Корабль слишком большой!")

        else:
            Background.showErrorMessage(nowBack, "Корабль за пределами сетки!")
        return tempShip

    def computerShots(self, game, opponent, coorForShots, back, useRandom = True):
        """формирует выстрел компьютера"""
        if useRandom:
            computerFiredCell = random.choice(tuple(coorForShots))
        else:
            computerFiredCell = coorForShots[0]
            coorForShots.remove(computerFiredCell)
        if computerFiredCell in self.coordinatesForShots:
            self.coordinatesForShots.remove(computerFiredCell)
        else:
            return self.computerShots(game, opponent, coorForShots, back)
        if computerFiredCell in self.computerNextShot:
            self.computerNextShot.remove(computerFiredCell)
        return game.checkingShot(computerFiredCell, self, opponent, True, back)
