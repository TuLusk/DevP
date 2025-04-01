import pygame
pygame.mixer.init()
music = pygame.mixer.music.load('music0.mp3')
pygame.mixer.music.play(loops=-1)