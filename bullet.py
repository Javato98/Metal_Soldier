import pygame
from pygame.sprite import Sprite
from paths import Paths



class Bullet(Sprite):

    def __init__(self, ms_game):
        '''Establecemos el constructor y las características de la bala'''

        super().__init__()

        self.screen = ms_game.screen
        self.settings = ms_game.settings
        self.soldier = ms_game.soldier
        self.levels = ms_game.levels


        self.x = ms_game.soldier.rect.x + 40
        self.y = ms_game.soldier.rect.y + 21

        if self.soldier.look_right:
            self.direction = 1
        else:
            self.direction = -1

        self.image_path = Paths('resources\\Bullets\\fire_bullet.png').__str__()
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (self.settings.bullet_width, self.settings.bullet_height))

        # Obtiene el rectángulo de la imagen y ajusta su posición
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)


        self.x = float(self.rect.x)



    def update(self):
        '''Generamos movimiento a la bala'''

        self.x += self.settings.bullet_speed * self.direction
        self.rect.x = self.x




    def blitme(self):
        '''Ponemos una bala como imagen'''

        self.screen.blit(self.image, self.rect)




