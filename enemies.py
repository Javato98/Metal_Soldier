from soldier import Soldier
from paths import Paths
import pygame

# Creamos los la clase Enemigo
class Enemy():

    def __init__(self, ms_game, enemie_number):

        # Instanciamos un soldado para poder reutilizar los métodos para crear los frames 
        self.soldier = Soldier(ms_game)

        # Creamos la ruta del enemigo elegido por parámetro
        self.path_image_run = Paths(f"resources\\pixel_char_pack\\Enemies\\Enemy Patrol\\Enemy{enemie_number}\\Enemy{enemie_number}_sprites\\Enemy{enemie_number}_run.png").__str__()

        # Cargamos la ruta de la imagen
        self.image_run = pygame.image.load(self.path_image_run).convert_alpha()

        # Creamos las listas para desarrollar las animaciones
        self.animation_run_front = []
        self.animation_run_back = []

        # Creamos los frames
        self.animation_run = self.soldier.make_frames(self.image_run, self.animation_run_front, self.animation_run_back, 8)

        print(self.animation_run)





