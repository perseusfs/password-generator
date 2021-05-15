import pygame
import random
import pyperclip
import sys
from pygame.locals import *

BG_COLOR = (88, 77, 74)
WIDTH = 800
HEIGHT = 600
mainClock = pygame.time.Clock()
pygame.init()
pygame.font.init()
pygame.display.set_caption("Password Generator")
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 64)
font = pygame.font.SysFont("Sans", 32)


def draw_text(text, fonts, color, surface, x, y):
    text_obj = fonts.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)


def main_menu():
    lower_chars = "abcdefghijklmnopqrstuvwxyz"
    upper_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!'^+%&/()=*-_>£#${[]}|@.,;:"
    password_structure = lower_chars + upper_chars + numbers + symbols
    password_length = 16
    password = "".join(random.sample(password_structure, password_length))
    screen.fill(BG_COLOR)
    draw_text("By Utku Faruk Şen", font, (255, 255, 255), screen, 560, 540)
    pygame.draw.rect(screen, (65, 54, 51), (240, 170, 310, 8))  #top
    pygame.draw.rect(screen, (65, 54, 51), (240, 170, 8, 100))  #left
    pygame.draw.rect(screen, (65, 54, 51), (550, 170, 8, 100))  #right
    pygame.draw.rect(screen, (65, 54, 51), (240, 270, 318, 8))  #bottom

    pygame.draw.rect(screen, (65, 54, 51), (300, 320, 200, 50))
    pygame.draw.rect(screen, (65, 54, 51), (300, 400, 200, 50))
    pygame.draw.rect(screen, (65, 54, 51), (300, 480, 200, 50))
    draw_text("Generate!", font, (0, 0, 0), screen, 330, 325)
    draw_text("Copy", font, (0, 0, 0), screen, 365, 405)
    draw_text("Clear", font, (0, 0, 0), screen, 365, 485)
    click = False
    running = True
    while running:
        mx, my = pygame.mouse.get_pos()
        button1 = pygame.Rect(300, 320, 200, 50)
        button2 = pygame.Rect(300, 400, 200, 50)
        button3 = pygame.Rect(300, 480, 200, 50)
        if button1.collidepoint((mx, my)):
            if click:
                screen.fill(BG_COLOR, (260, 180, 270, 80))
                draw_text(str(password), font, (255, 255, 255), screen, 260, 200)
        if button2.collidepoint((mx, my)):
            if click:
                pyperclip.copy(str(password))


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                if button3.collidepoint((mx, my)):
                        main_menu()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
        pygame.display.update()
        mainClock.tick(60)


main_menu()
