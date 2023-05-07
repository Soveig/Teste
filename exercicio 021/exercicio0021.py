#crie um mp3
import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
input('digite algo para tocar: ')
pygame.mixer.music.play()
input('digite algo para tocar: ')