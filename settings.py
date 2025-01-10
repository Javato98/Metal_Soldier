import pygame


class Settings():

    def __init__(self):
        '''Definimos las propiedades de los elmentos clave del juego'''
        
        # Screen
        self.screen_width = 1200
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.bg_screen = (59, 86, 97)
        pygame.display.set_caption('Metal Soldier')


        # Soldier
        self.velocity_animation_run_front = 40
        self.velocity_animation_jump_front = 95
        self.displace_x = 3
        self.displace_y = 10


        # Bullet 
        self.bullet_width = 20
        self.bullet_height = 10
        self.bullet_speed = 20









        
        