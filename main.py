import pygame
import time
from data.classes.Board import Board

pygame.init()

WINDOW_SIZE = (600,600)
FONT = pygame.font.Font('freesansbold.ttf', 32)

screen = pygame.display.set_mode(WINDOW_SIZE)
board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])


def draw(display):
    display.fill('white')
    board.draw(display)
    pygame.display.update()

def show_text(message):
    text = FONT.render(message, True, "Black", "White")
    textRect = text.get_rect()
    textRect.center = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2)
    screen.blit(text, textRect)
    pygame.display.update()
    time.sleep(3)

if __name__ == '__main__':
    running = True
    while running:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type ==pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    board.handle_click(mx,my)
        if board.is_in_checkmate('black'):
            show_text("White Won!!")
            running = False
        elif board.is_in_checkmate('white'):
            show_text("Black Won!!")
            running = False
        draw(screen)