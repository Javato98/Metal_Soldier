import pygame
from pygame.sprite import Sprite
from paths import Paths



class Bullet(Sprite):

    def __init__(self, ms_game, character):
        '''Establecemos el constructor y las características de la bala'''

        super().__init__()

        self.screen = ms_game.screen
        self.settings = ms_game.settings
        self.character = character
        self.enemies = ms_game.enemies
        self.soldier = ms_game.soldier
        self.levels = ms_game.levels

        self.fit_initial_position()

        self.flag_direction = False

        self.image_path = Paths('resources\\Bullets\\fire_bullet.png').__str__()
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (self.settings.bullet_width, self.settings.bullet_height))

        # Obtiene el rectángulo de la imagen y ajusta su posición
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)


        self.x = float(self.rect.x)


    def fit_initial_position(self):
        if self.character == self.soldier:
            self.fit_x = 40
            self.fit_y = 21
        else:
            self.fit_x = 40
            self.fit_y = 25

        self.x = self.character.rect.x + self.fit_x
        self.y = self.character.rect.y + self.fit_y


    
    def set_direction(self):

        if self.flag_direction == False: # nos aseguramos que la bala no vuelva a cambiar la dirección una vez que ha empezado su recorrido

            for enemy in self.enemies:
                if self.character == enemy:
                    if self.soldier.rect.x < enemy.rect.x:
                        enemy.look_right = False
                        self.direction_enemy = -1
                    else:
                        enemy.look_right = True
                        self.direction_enemy = 1

            if self.character == self.soldier:
                if self.soldier.look_right:
                    self.direction_soldier = 1
                else:
                    self.direction_soldier = -1

            self.flag_direction = True



    def update(self):
        '''Generamos movimiento a la bala'''

        self.set_direction()

        direction = 0

        if self.character == self.soldier:
            direction = self.direction_soldier
        else:
            direction = self.direction_enemy

        # Establecer el tiempo entre disparo y disparo
        self.x += self.settings.bullet_speed * direction
        self.rect.x = self.x





    def blitme(self):
        '''Ponemos una bala como imagen'''

        self.screen.blit(self.image, self.rect)




