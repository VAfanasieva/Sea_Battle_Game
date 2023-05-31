import pygame
import sys
from src.Background import Background
from src.Button import Button

pygame.font.init()
pygame.init()


class Frame:
    sizeName = 20
    fontName = 'MuseoSansCyrl500Italic.otf'
    backColor = (217, 217, 217)
    colorFill = (115, 115, 115, 110)
    sizeFontTitle = 30
    fontTitle = 'MuseoSansCyrl700Italic.otf'
    font = pygame.font.SysFont(fontTitle, Background.cellSize, italic=True)
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

    def printInstruction(self):
        """рисует фрейм с инструкцией"""
        back = pygame.Surface((Background.WIDTH, Background.HEIGHT))
        back = back.convert_alpha()
        back.fill(self.colorFill)
        Background.screen.blit(back, (0, 0))
        rect = pygame.Rect(115, 75, 825, 335)
        pygame.draw.rect(Background.screen, self.backColor, rect)
        txtTitle = self.font.render(self.title, True, Background.objectColor)
        Background.screen.blit(txtTitle, ((Background.WIDTH - txtTitle.get_width()) // 2, 100))
        for i in range(0, 7):
            self.printstr(i)
        buttonClose = Button()
        buttonClose.drawButtonClose(940, 75, Background(), self.backColor)
        flag = False
        while not flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if 920 <= x <= 960 and 55 <= y <= 95:
                        flag = True
            pygame.display.update()

    def printstr(self, i):
        """печатает строчку инструкции"""
        txtName = Background.font.render(self.name[i], True, Background.objectColor)
        Background.screen.blit(txtName, ((Background.WIDTH - txtName.get_width()) // 2, Background.HEIGHT // 2 + Background.cellSize * (i - 3) - 50))

    def printResult(self, rez):
        """рисует фрейм с результатом после окончания игры"""
        back = pygame.Surface((Background.WIDTH, Background.HEIGHT))
        back = back.convert_alpha()
        back.fill(self.colorFill)
        Background.screen.blit(back, (0, 0))
        rect = pygame.Rect(Background.WIDTH // 2 - 150, Background.HEIGHT // 2 - 60, 300, 120)
        pygame.draw.rect(Background.screen, self.backColor, rect)
        txt = Background.font.render(rez, True, Background.objectColor)
        Background.screen.blit(txt, ((Background.WIDTH - txt.get_width()) // 2, (Background.HEIGHT - txt.get_height()) // 2))
        pygame.display.update()
        buttonClose = Button()
        buttonClose.drawButtonClose(Background.WIDTH // 2 + 150, Background.HEIGHT // 2 - 60, Background(), self.backColor)
        flag = False
        while not flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if ((Background.WIDTH // 2 + 130) <= x <= (Background.WIDTH // 2 + 170)) and ((Background.HEIGHT // 2 - 80) <= y <= (Background.HEIGHT // 2 - 40)):
                        flag = True
            pygame.display.update()
