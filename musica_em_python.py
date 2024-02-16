import pygame

pygame.init()
pygame.mixer.music.load('musica_em_python.mp3') '''Coloque o arquivo de musica'''
pygame.mixer.play()
pygame.event.wait()