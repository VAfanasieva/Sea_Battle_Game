import pygame
import sys

cellSize = 30
WIDTH = 35 * cellSize  # ширина игрового окна
HEIGHT = 19 * cellSize  # высота игрового окна

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))       #создаем экран для отображения
pygame.display.set_caption("Sea battle")                #заголовок окна


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
        self.drawGrid(12, "COMPUTER")

class Button():
    def __init__(self):
        pass

    def drawButton(self, x, text):
        rect = pygame.Rect(x, cellSize, 5 * cellSize, 2 * cellSize)
        pygame.draw.rect(screen, Background.objectColor, rect, width=Background.thicknessOfObjects)
        txt = Background.font.render(text, True, Background.objectColor)
        screen.blit(txt, (x + (5 * cellSize - txt.get_width()) // 2, cellSize + (2 * cellSize - txt.get_height()) // 2))


def main():
    nowBack = Background()
    nowBack.drawBackground()
    exitButton = Button()
    rulesButton = Button()
    exitButton.drawButton(WIDTH - 7 * cellSize, "Выйти")
    rulesButton.drawButton(2 * cellSize, "Правила")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


if __name__ == '__main__':
    main()

