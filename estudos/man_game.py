import time
import pygame
from pygame.locals import *

# Função para inicializar o pygame
def init_pygame():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Jogo das Emoções')
    return screen

# Função para carregar e mostrar imagem
def show_image(screen, image_path):
    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, (640, 480))  # Ajusta a imagem ao tamanho da janela
    screen.blit(image, (0, 0))
    pygame.display.update()

# Função para tocar som
def play_sound(sound_path):
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play()

# Função para impressão lenta do texto
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
        ("Qual é sua lembrança mais feliz?", "happy.jpg", "happy.mp3"),
        ("Se pudesse mudar algo no passado, o que seria?", "reflective.jpg", "reflective.mp3"),
        ("Qual
