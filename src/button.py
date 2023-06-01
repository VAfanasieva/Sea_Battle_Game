import pygame

pygame.font.init()
pygame.init()


class Button:
    def __init__(self):
        pass

    def drawButton(self, x, text, Background):
        """рисует кнопку - прямоугольник с переданным текстом"""
        rect = pygame.Rect(x, Background.cellSize, 5 * Background.cellSize, 2 * Background.cellSize)
        pygame.draw.rect(Background.screen, Background.objectColor, rect, width=Background.thicknessOfObjects)
        txt = Background.font.render(text, True, Background.objectColor)
        Background.screen.blit(txt, (x + (5 * Background.cellSize - txt.get_width()) // 2, Background.cellSize + (2 * Background.cellSize - txt.get_height()) // 2))

    def drawButtonClose(self, x0, y0, Background, backColor):
        """рисует кнопку с выходом - крестик"""
        pygame.draw.circle(Background.screen, backColor, (x0, y0), 20)
        pygame.draw.circle(Background.screen, Background.objectColor, (x0, y0), 20, width=Background.thicknessOfObjects)
        pygame.draw.line(Background.screen, Background.objectColor, (x0 - 9, y0 - 9), (x0 + 9, y0 + 9),
                         Background.thicknessOfObjects)
        pygame.draw.line(Background.screen, Background.objectColor, (x0 - 9, y0 + 9), (x0 + 9, y0 - 9),
                         Background.thicknessOfObjects)
