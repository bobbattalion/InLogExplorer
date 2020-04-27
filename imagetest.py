import pygame

pygame.init()

win = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Image Test")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

test = pygame.image.load("test.png")

win.fill((0, 255, 255))

win.blit(test, (0,0))

pygame.display.update()
