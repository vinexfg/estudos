import time
import pygame
from pygame.locals import *


def init_pygame():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Jogo das Emoções')
    return screen


def show_image(screen, image_path):
    image = pygame.image.load(image_path)
    screen.blit(image, (0, 0))
    pygame.display.update()


def play_sound(sound_path):
    sound = pygame.mixer.Sound(sound_path)
    sound.play()

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    screen = init_pygame()
    slow_print("Bem-vindo ao jogo das emoções!")
    time.sleep(1)
    slow_print("Vamos começar com algumas perguntas que podem mexer com seus sentimentos.")
    time.sleep(1)

    questions = [
        ("Qual é sua lembrança mais feliz?", "happy.jpg", "happy.wav"),
        ("Se pudesse mudar algo no passado, o que seria?", "reflective.jpg", "reflective.wav"),
        ("Qual é seu maior medo?", "scared.jpg", "scared.wav"),
        ("Qual foi o momento mais difícil que já enfrentou?", "sad.jpg", "sad.wav"),
        ("O que te faz sentir mais vivo?", "happy.jpg", "happy.wav")
    ]

    for question, image_path, sound_path in questions:
        show_image(screen, image_path)
        play_sound(sound_path)
        slow_print(question)
        answer = input("> ")
        slow_print("Obrigado por compartilhar.\n")
        time.sleep(1)

    slow_print("Obrigado por jogar! Esperamos que você tenha aproveitado essa experiência.")
    time.sleep(1)

    pygame.quit()

if __name__ == "__main__":
    main()