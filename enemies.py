from soldier import Soldier
from paths import Paths
from pygame.sprite import Sprite
import pygame

# Creamos los la clase Enemigo
class Enemy(Sprite):

    def __init__(self, ms_game, enemie_number, x, y):

        super().__init__()

        # Instanciamos un soldado para poder reutilizar los métodos para crear los frames 
        self.soldier = Soldier(ms_game)
        self.screen = ms_game.screen
        self.levels = ms_game.levels
        self.enemies = ms_game.enemies

        # Creamos la ruta del enemigo elegido por parámetro
        self.path_image_run = Paths(f"resources\\pixel_char_pack\\Enemies\\Enemy Patrol\\Enemy{enemie_number}\\Enemy{enemie_number}_sprites\\Enemy{enemie_number}_run.png").__str__()
        self.path_image_die = Paths(f"resources\\pixel_char_pack\\Enemies\\Enemy Patrol\\Enemy{enemie_number}\\Enemy{enemie_number}_sprites\\Enemy{enemie_number}_Death1.png").__str__()

        # Cargamos la ruta de la imagen
        self.image_run = pygame.image.load(self.path_image_run).convert_alpha()
        self.image_die = pygame.image.load(self.path_image_die).convert_alpha()

        # Creamos las listas para desarrollar las animaciones
        self.animation_run_front = []
        self.animation_run_back = []

        self.animation_die_front = []
        self.animation_die_back = []


        # Creamos los frames
        self.animation_run = self.soldier.make_frames(self.image_run, self.animation_run_front, self.animation_run_back, 8)
        self.animation_die = self.soldier.make_frames(self.image_die, self.animation_die_front, self.animation_die_back, 8)

        self.image = self.animation_run_front[3]
        self.rect = self.image.get_rect(width=40)
        self.rect.x = x
        self.rect.y = y
        self.animation_frame = self.animation_run_front

        self.look_right = True
        self.dead = False
        self.check_frame = True
        self.be_shot = 0
        self.displace_x = 1

        self.frame_index = 0
        self.frame_timer = 0

        self.drop = True
        

    
    def animation(self, animation, current_time, velocity_animation = 150):

        if current_time - self.frame_timer > velocity_animation:

            self.image = animation[self.frame_index]
            self.frame_index = (self.frame_index + 1) % len(animation) 
            self.frame_timer = current_time
            

    def standar_position(self):
        '''Después de cada animación le establecemos una postura estandar al personaje'''

        if self.look_right:
            self.animation_frame = self.animation_run_front

        elif self.look_right == False:
            self.animation_frame = self.animation_run_back



    def _detecter_collision_enemy(self, current_time):
        
        platforms = self.levels.make_platforms()

        collisions = bool(pygame.sprite.spritecollide(self, platforms, False))

        
        if collisions:
            if self.dead == False:
                self.animation(self.animation_frame, current_time)

                for platform in platforms:

                    if self.rect.colliderect(platform):

                        if self.rect.right > platform.rect.right - 10 or self.look_right == False:
                            self.look_right = False
                            self.rect.x -= self.displace_x

                        if self.rect.left < platform.rect.left -10 or self.look_right:
                            self.look_right = True
                            self.rect.x += self.displace_x

                        self.standar_position()

        else:
            self.drop = True
            self.rect.y += self.soldier.settings.displace_y

    
    def _die(self, current_time):
        if self.dead:
            if self.check_frame:
                self.frame_index = 1
                self.check_frame = False
            self.animation(self.animation_die_front, current_time)
            print(self.frame_index)

            if self.frame_index == 0:
                self.enemies.remove(self)
                self.dead = False
                self.check_frame = True



    
    def check_die(self):
        if self.be_shot == 5:
            self.dead = True
            


    def update(self, current_time):
        self.check_die()
        self._die(current_time)
        self._detecter_collision_enemy(current_time)
    

    def blitme(self):    

        self.screen.blit(self.image, self.rect)


        
        





