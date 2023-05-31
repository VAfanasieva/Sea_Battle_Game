import pygame
from src.Button import Button

pygame.font.init()
pygame.init()


class Background:
    OFFSET = 12
    cellSize = 30
    WIDTH = 35 * cellSize       # ширина игрового окна
    HEIGHT = 19 * cellSize      # высота игрового окна
    leftMargin = 7 * cellSize   # отступ слева
    upperMargin = 5 * cellSize  # отступ сверху
    colorBackground = (255, 255, 255)
    colorGrid = (172, 172, 172)
    objectColor = (85, 85, 85)
    colorPoint = (0, 0, 0)
    colorOfCross = (255, 0, 0)
    thicknessOfObjects = 2
    fontName = 'MuseoSansCyrl500.otf'
    LETTERS = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К']
    cellsUnnecessary = pygame.image.load('unnecessaryСells.bmp')

    coorOfCrosses = []              # лист с координатами всех крестиков
    coorOfPoints = []               # лист с координатами всех точек
    coorOfUnnecessaryCells = []     # лист с координатами всех ненужных клеток

    fontSize = int(cellSize / 1.25)
    font = pygame.font.SysFont(fontName, fontSize)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # создаем экран для отображения
    pygame.display.set_caption("Sea battle")  # заголовок окна

    def __init__(self):
        pass

    def drawGrid(self, offset, title):
        """рисует поле, подписи игрока и компьютера, в зависимости от отступа"""
        rect = pygame.Rect(self.leftMargin + offset * self.cellSize, self.upperMargin, 10 * self.cellSize, 10 * self.cellSize)
        pygame.draw.rect(self.screen, self.objectColor, rect, width=self.thicknessOfObjects)

        player = self.font.render(title, True, self.objectColor)
        self.screen.blit(player, (self.leftMargin + 5 * self.cellSize - player.get_width() // 2 + offset * self.cellSize,
                             self.upperMargin + 9.5 * self.cellSize + self.fontSize))

        for i in range(1, 11):
            num_ver = self.font.render(str(i), True, self.objectColor)                      # рендер цифр
            letters_hot = self.font.render(self.LETTERS[i - 1], True, self.objectColor)     # рендер букв
            num_ver_width = num_ver.get_width()             # ширина цифры
            num_ver_height = num_ver.get_height()           # высота текста
            letters_hot_width = letters_hot.get_width()     # ширина букв

            # отображение цифр и букв для 1 сетки
            self.screen.blit(num_ver, (self.leftMargin - (self.cellSize // 2 + num_ver_width // 2) + offset * self.cellSize,
                                  self.upperMargin + (i - 1) * self.cellSize + (
                                          self.cellSize // 2 - num_ver_height // 2)))

            self.screen.blit(letters_hot,
                        (self.leftMargin + (i - 1) * self.cellSize + (self.cellSize // 2 - letters_hot_width // 2) + offset * self.cellSize,
                         self.upperMargin - (self.cellSize // 2 + num_ver_height // 2)))

    def drawBackground(self):
        """рисует фон - сетку, поле"""
        self.screen.fill(self.colorBackground)
        for hor in range(self.cellSize, self.HEIGHT, self.cellSize):
            pygame.draw.line(self.screen, self.colorGrid, (0, hor), (self.WIDTH, hor), 1)
        for ver in range(self.cellSize, self.WIDTH, self.cellSize):
            pygame.draw.line(self.screen, self.colorGrid, (ver, 0), (ver, self.HEIGHT), 1)
        self.drawGrid(0, "MY")
        self.drawGrid(self.OFFSET, "COMPUTER")

    def drawCross(self):
        """"рисует крестики"""
        for cell in self.coorOfCrosses:
            x1 = self.cellSize * (cell[0] - 1) + self.leftMargin
            y1 = self.cellSize * (cell[1] - 1) + self.upperMargin
            pygame.draw.line(self.screen, self.colorOfCross, (x1, y1), (x1 + self.cellSize, y1 + self.cellSize),
                             self.thicknessOfObjects)
            pygame.draw.line(self.screen, self.colorOfCross, (x1, y1 + self.cellSize), (x1 + self.cellSize, y1),
                             self.thicknessOfObjects)

    def drawPoints(self):
        """"рисует точки"""
        for coor in self.coorOfPoints:
            pygame.draw.circle(self.screen, self.colorPoint,
                               (self.cellSize * (coor[0] - 0.5) + self.leftMargin,
                                self.cellSize * (coor[1] - 0.5) + self.upperMargin),
                               self.cellSize // 6)

    def drawUnnecessaryCells(self):
        """"рисует картинку с заливкой, где точно нет корабля"""
        for coor in self.coorOfUnnecessaryCells:
            x0 = self.leftMargin + coor[0] * self.cellSize - self.cellSize // 2
            y0 = self.upperMargin + coor[1] * self.cellSize - self.cellSize // 2
            self.cellsUnnecessary.set_colorkey((255, 255, 255))
            rectUnnecessary = self.cellsUnnecessary.get_rect(center=(x0, y0))
            self.screen.blit(self.cellsUnnecessary, rectUnnecessary)

    def drawShips(self, listShip):
        """рисует корабли"""
        # listShip - вложенный список с координатами караблей [[( , ), ( , ),  ],  [( , ), ( , )  ]  ]
        for coor in listShip:
            if coor:
                ship = sorted(coor)
                x_start = ship[0][0]
                y_start = ship[0][1]

                ship_width = self.cellSize * len(ship)  # горизонтальные корабли и корабли состоящие из одной клетки
                ship_height = self.cellSize

                if len(ship) > 1 and ship[0][0] == ship[1][0]:
                    ship_width, ship_height = ship_height, ship_width

                x = self.cellSize * (x_start - 1) + Background.leftMargin
                y = self.cellSize * (y_start - 1) + Background.upperMargin

                pygame.draw.rect(self.screen, Background.objectColor, ((x, y), (ship_width, ship_height)), width=2)

    def sendMessage(self, message):
        """"выводит сообщение на верхнюю часть экран"""
        fontMes = pygame.font.SysFont(self.fontName, self.cellSize)
        text = fontMes.render(message, True, self.objectColor)
        self.screen.blit(text, ((self.WIDTH - text.get_width()) / 2, self.cellSize * 2.3))

    def showErrorMessage(self, message):
        """"выводит сообщение-ошибку на нижнюю часть экран"""
        fontMes = pygame.font.SysFont(Background.fontName, self.cellSize)
        text = fontMes.render(message, True, self.objectColor)
        self.screen.blit(text, ((self.WIDTH - text.get_width()) / 2, self.HEIGHT - self.cellSize * 1.5))

    def drawWholeBackground(self, human, computer, mes):
        """полностью отрисовывает экран после изменения данных"""
        nowBack = Background()
        nowBack.drawBackground()
        exitButton = Button()
        rulesButton = Button()
        exitButton.drawButton(self.WIDTH - 7 * self.cellSize, "Выйти", nowBack)
        rulesButton.drawButton(2 * self.cellSize, "Правила", nowBack)
        self.drawPoints()
        self.drawUnnecessaryCells()
        self.drawCross()
        self.drawShips(human.coorOwnShips)
        self.drawShips(computer.shipsKilled)
        if mes:
            nowBack.sendMessage(mes)
