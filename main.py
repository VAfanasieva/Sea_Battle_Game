# размер шрифта заменить на 20
import pygame
import sys
import random

cellSize = 30
WIDTH = 35 * cellSize  # ширина игрового окна
HEIGHT = 19 * cellSize  # высота игрового окна

OFFSET = 12

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))       #создаем экран для отображения
pygame.display.set_caption("Sea battle")                #заголовок окна


class Game:
    coorOfCrosses = []
    coorOfPoints = []
    coorOfUnnecessaryCells = []

    def getCoor(self):
        pass
    def removeCoorFromFree(self):
        pass
    def addCoorOfCrosses(self):
        pass
    def addPointCoor(self):
        pass
    def addCoorOfUnnecessaryCells(self):
        pass
    def CheckingShot(self):
        pass

class Background():
    colorBackground = (255, 255, 255)
    colorGrid = (172, 172, 172)
    objectColor = (85, 85, 85)
    leftMargin = 7 * cellSize  # отступ слева
    upperMargin = 5 * cellSize  # отступ сверху
    thicknessOfObjects = 2
    fontName = 'MuseoSansCyrl500.otf'
    fontSize = int(cellSize / 1.25)
    font = pygame.font.SysFont(fontName, fontSize)
    LETTERS = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К']

    def __init__(self):
        pass

    def drawGrid(self, offset, title):
        """рисует поле, подписи игрока и компьютера, в зависимости от отступа"""
        rect = pygame.Rect(self.leftMargin + offset * cellSize, self.upperMargin, 10 * cellSize, 10 * cellSize)
        pygame.draw.rect(screen, self.objectColor, rect, width=self.thicknessOfObjects)

        player = self.font.render(title, True, self.objectColor)
        screen.blit(player, (self.leftMargin + 5 * cellSize - player.get_width() // 2 + offset * cellSize,
                             self.upperMargin + 9.5 * cellSize + self.fontSize))

        for i in range(1, 11):
            num_ver = self.font.render(str(i), True, self.objectColor)      # рендер цифр
            letters_hot = self.font.render(self.LETTERS[i - 1], True, self.objectColor)     # рендер букв
            num_ver_width = num_ver.get_width()     # ширина цифры
            num_ver_height = num_ver.get_height()       # высота текста
            letters_hot_width = letters_hot.get_width()     # ширина букв

            # отображение цифр и букв для 1 сетки
            screen.blit(num_ver, (self.leftMargin - (cellSize // 2 + num_ver_width // 2) + offset * cellSize,
                                  self.upperMargin + (i - 1) * cellSize + (
                                          cellSize // 2 - num_ver_height // 2)))

            screen.blit(letters_hot,
                        (self.leftMargin + (i - 1) * cellSize + (cellSize // 2 - letters_hot_width // 2) + offset * cellSize,
                         self.upperMargin - (cellSize // 2 + num_ver_height // 2)))



    def drawBackground(self):
        """рисуем фон - сетку, поле"""
        screen.fill(self.colorBackground)
        for hor in range(cellSize, HEIGHT, cellSize):
            pygame.draw.line(screen, self.colorGrid, (0, hor), (WIDTH, hor), 1)
        for ver in range(cellSize, WIDTH, cellSize):
            pygame.draw.line(screen, self.colorGrid, (ver, 0), (ver, HEIGHT), 1)
        self.drawGrid(0, "MY")
        self.drawGrid(OFFSET, "COMPUTER")

    def showErrorMessage(self, message):
        fontMes = pygame.font.SysFont(Background.fontName, cellSize)
        text = fontMes.render(message, True, Background.objectColor)
        screen.blit(text, ((WIDTH - text.get_width()) / 2, HEIGHT - cellSize * 1.5))



class PlayersField():
    colorPoint = (0, 0, 0)
    cellsUnnecessary = pygame.image.load('unnecessaryСells.bmp')
    colorOfCross = (255, 0, 0)

    def __init__(self, offset):
        self.offset = offset
        self.coordinatesFree = [(x, y) for x in range(1 + self.offset, 11 + self.offset) for y in range(1, 11)]     # свободные ячейки
        self.coorOwnShips = []      # координаты собсвенных кораблей
        self.listShipsCoordinates = []
    #def __init__(self, player, offset, numderOfCell, coordinates ):
    # self.numderOfCell = numderOfCell

    def hit(self):
        pass

    def miss(self):
        pass

    # создаем корабль, клетки которого записаны в виде кордежа
    def createShipComputer(self, numderOfCell, coordinatesFree):
        coordinatesShip = []       # координаты корабля
        vector = random.randint(0, 1)       # горизонтальный или вертикальный(х = 0 у = 1)
        direction = random.choice((-1, 1))      # вверх или вниз, влево или вправо
        x, y = random.choice(tuple(coordinatesFree))     # выбор свободной координаты
        for _ in range(numderOfCell):
            coordinatesShip.append((x, y))                                             #записываем координаты в кортеж
            if not vector:
                direction, x = self.addBlockToShip(x, direction, vector, coordinatesShip)
            else:
                direction, y = self.addBlockToShip(y, direction, vector, coordinatesShip)

        if set(coordinatesShip).issubset(coordinatesFree):
            return coordinatesShip
        return self.createShipComputer(numderOfCell, coordinatesFree)

    # возвращает блок для корабля
    def addBlockToShip(self, coor, direction, vector, coordinatesShip):      # получаеи новую клетку для корабля, если она удовлетворяет требованиям - не выходит за рамки поля
        if (coor <= 1 - OFFSET * cellSize * vector and direction == -1) or (coor >= 10 + OFFSET * cellSize * vector and direction == 1):
            direction *= -1
            return direction, coordinatesShip[0][vector] + direction
        else:
            return direction, coordinatesShip[-1][vector] + direction

    # удаляет все клетки вокруг нового корабля из доступных
    def removeCoorFromFree(self, newShip):
        for coor in newShip:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 12 < (coor[0] + i) < 23 and 0 < (coor[1] + j) < 11 and (coor[0] + i, coor[1] + j) in self.coordinatesFree:           # не выходим ли за рамки сетки
                        self.coordinatesFree.remove((coor[0] + i, coor[1] + j))

    def populateGrid(self):
        for countCell in range(4, 0, -1):
             for _ in range(5 - countCell):
                 newShip = self.createShipComputer(countCell, self.coordinatesFree)
                 self.listShipsCoordinates.append(newShip)
                 self.coorOwnShips.append(newShip)
                 self.removeCoorFromFree(newShip)

    def drawShips(self):
        for coor in self.coorOwnShips:
            ship = sorted(coor)
            x_start = ship[0][0]
            y_start = ship[0][1]

            ship_width = cellSize * len(ship)  # горизонтальные корабли и корабли состоящие из одной клетки
            ship_height = cellSize

            if len(ship) > 1 and ship[0][0] == ship[1][0]:
                ship_width, ship_height = ship_height, ship_width

            x = cellSize * (x_start - 1) + Background.leftMargin
            y = cellSize * (y_start - 1) + Background.upperMargin

            pygame.draw.rect(screen, Background.objectColor, ((x, y), (ship_width, ship_height)), width=2)


    def drawRectangleHuman(self, back):
        drawing = False
        startX, startY = (0, 0)
        start = (0, 0)
        shipSize = (0, 0)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    drawing = True
                    startX, startY = event.pos
                    start = (startX, startY)
                    shipSize = (startX, startY)
                elif drawing and event.type == pygame.MOUSEMOTION:
                    endX, endY = event.pos
                    end = (endX, endY)
                    shipSize = (endX - startX, endY - startY)
                elif drawing and event.type == pygame.MOUSEBUTTONDOWN:
                    tempShip = [] #временный корабль
                    endX, endY = event.pos
                    drawing = False
                    shipSize = (0, 0)
                    numberOfDowned = [0, 0, 0, 0]
                    cellStart = ((startX - Background.leftMargin) // (cellSize + 1),
                                 (startY - Background.upperMargin) // (cellSize + 1))
                    cellEnd = ((endX - Background.leftMargin) // (cellSize + 1),
                                 (endY - Background.upperMargin) // (cellSize + 1))
                    if cellStart > cellEnd:
                        cellStart, cellEnd = cellEnd, cellStart
                    if 0 < cellStart[0] < 11 and 0 < cellStart[1] < 11 and 0 < cellEnd[0] < 11 and 0 < cellEnd[1] < 11:
                        if cellStart[0] == cellEnd[0] and (cellEnd[1] - cellStart[1]) < 4:
                            for cell in range(cellStart[1], cellEnd[1] + 1):
                                tempShip.append((cellStart[0], cell))
                        elif cellStart[1] == cellEnd[1] and (cellEnd[0] - cellEnd[0]) < 4:
                            for cell in range(cellStart[0], cellEnd[0] + 1):
                                tempShip.append((cell, cellStart[1]))
                        else:
                            Background.showErrorMessage(back, "Корабль слишком большой!")
                    else:
                        Background.showErrorMessage(back, "Корабль за пределами сетки!")
                    if tempShip:
                        if set(tempShip).issubset(self.coordinatesFree):
                            if (5 - len(tempShip)) > numberOfDowned[len(tempShip) - 1]:
                                numberOfDowned[len(tempShip) - 1] += 1
                                self.coorOwnShips.append((tempShip))
                                self.removeCoorFromFree(tempShip, self)
                            else:
                                Background.showErrorMessage(back, f'Уже достаточно {len(tempShip)} кораблей!')
                        else:
                            Background.showErrorMessage(back, f'Корабли соприкасаются!')
            if len(self.coorOwnShips) == 10:
                break
            pygame.draw.rect(screen, Background.objectColor, (start, shipSize), Background.thicknessOfObjects)
            #self.drawBordersShips(player.coorOwnShips)
            pygame.display.update()


    def drawCross(self, addCoorOfCrosses):  # какой сет передаем
        for cell in addCoorOfCrosses:
            x1 = cellSize * (cell[0] - 1) + Background.leftMargin
            y1 = cellSize * (cell[1] - 1) + Background.upperMargin
            pygame.draw.line(screen, self.colorOfCross, (x1, y1), (x1 + cellSize, y1 + cellSize),
                             Background.thicknessOfObjects)
            pygame.draw.line(screen, self.colorOfCross, (x1, y1 + cellSize), (x1 + cellSize, y1),
                             Background.thicknessOfObjects)


    def drawPoints(self, coorOfPoints):
        for coor in coorOfPoints:
            pygame.draw.circle(screen, self.colorPoint,
                               (cellSize * (coor[0] - 0.5) + Background.leftMargin,
                                cellSize * (coor[1] - 0.5) + Background.upperMargin),
                               cellSize // 6)

    def drawUnnecessaryCells(self, x0, y0):
        self.cellsUnnecessary.set_colorkey((255, 255, 255))
        rectUnnecessary = self.cellsUnnecessary.get_rect(center=(x0, y0))
        screen.blit(self.cellsUnnecessary, rectUnnecessary)

    def drawField(self):
        pass

class Button():
    def __init__(self):
        pass

    def drawButton(self, x, text):
        rect = pygame.Rect(x, cellSize, 5 * cellSize, 2 * cellSize)
        pygame.draw.rect(screen, Background.objectColor, rect, width=Background.thicknessOfObjects)
        txt = Background.font.render(text, True, Background.objectColor)
        screen.blit(txt, (x + (5 * cellSize - txt.get_width()) // 2, cellSize + (2 * cellSize - txt.get_height()) // 2))


class Close(Button):
    def drawButtonClose(self, x0, y0):
        pygame.draw.circle(screen, Frame.backColor, (x0, y0), 20)
        pygame.draw.circle(screen, Background.objectColor, (x0, y0), 20, width=Background.thicknessOfObjects)
        pygame.draw.line(screen, Background.objectColor, (x0 - 9, y0 - 9), (x0 + 9, y0 + 9),
                         Background.thicknessOfObjects)
        pygame.draw.line(screen, Background.objectColor, (x0 - 9, y0 + 9), (x0 + 9, y0 - 9),
                         Background.thicknessOfObjects)
    def hideFrame(self):
        pass


class Frame():
    sizeName = 20
    fontName = 'MuseoSansCyrl500Italic.otf'
    backColor = (217, 217, 217)
    colorFill = (115, 115, 115, 110)
    sizeFontTitle = 30
    fontTitle = 'MuseoSansCyrl700Italic.otf'
    font = pygame.font.SysFont(fontTitle, cellSize, italic=True)
    title = "Правила игры “Морской бой”"
    name = ["Цель игры состоит в том, чтобы утопить все боевые единицы соперника.",
            "Игрок выбирает, какую клетку хочет проверить,после кликает на выбранную клетку.",
            "Если у противника в такой клеточке располагается корабль, то в данной клеточке ставится крестик.",
            "После попадания игрок получает право на еще один выстрел.",
            "Когда он кликает на клетку, которая у противника пустая,",
            "то в этой клетке ставится точка и ход переходит противнику.",
            "Победителем становится тот, кто первым обнаружил все суда соперника."]

    def __init__(self):
        pass

    def hideFrame(self):
        pass


    def printInstruction(self):
        back = pygame.Surface((WIDTH, HEIGHT))
        back = back.convert_alpha()
        back.fill(self.colorFill)
        screen.blit(back, (0, 0))
        rect = pygame.Rect(115, 75, 825, 335)
        pygame.draw.rect(screen, self.backColor, rect)
        txtTitle = self.font.render(self.title, True, Background.objectColor)
        screen.blit(txtTitle, ((WIDTH - txtTitle.get_width()) // 2, 100))
        for i in range(0, 7):
            self.printstr(i)
        buttonClose = Close()
        buttonClose.drawButtonClose(940, 75)

    def printstr(self, i):
        txtName = Background.font.render(self.name[i], True, Background.objectColor)
        screen.blit(txtName, ((WIDTH - txtName.get_width()) // 2, HEIGHT // 2 + cellSize * (i - 3) - 50))

    def printResult(self, rez):
        back = pygame.Surface((WIDTH, HEIGHT))
        back = back.convert_alpha()
        back.fill(self.colorFill)
        screen.blit(back, (0, 0))
        rect = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 - 60, 300, 120)
        pygame.draw.rect(screen, self.backColor, rect)
        txt = Background.font.render(rez, True, Background.objectColor)
        screen.blit(txt, (WIDTH // 2, HEIGHT // 2))

def main():
    nowBack = Background()
    nowBack.drawBackground()
    exitButton = Button()
    rulesButton = Button()
    exitButton.drawButton(WIDTH - 7 * cellSize, "Выйти")
    rulesButton.drawButton(2 * cellSize, "Правила")

    computerTurn = False
    computer = PlayersField(OFFSET)
    print(computer.coordinatesFree)
    computer.populateGrid()
    computer.drawShips()


    #human = PlayersField(0)

    #human.drawRectangleHuman(nowBack)
    #computer.coorOwnShips.update(Ship.populate_grid())
    #Ship.drawBordersShips(computer.coorOwnShips)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if ((WIDTH - cellSize * 7) <= x <= (WIDTH - cellSize * 2)) and (cellSize <= y <= (cellSize * 3)):
                    pygame.quit()
                    sys.exit()
                if ((cellSize * 2) <= x <= (cellSize * 7)) and (cellSize <= y <= (cellSize * 3)):
                    instruct = Frame()
                    instruct.printInstruction()
        pygame.display.update()


if __name__ == '__main__':
    main()

