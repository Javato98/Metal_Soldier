from soldier import Soldier
from paths import Paths
from pygame.sprite import Sprite
from coordenates_levels import Stairs
import pygame

# Creamos los la clase Enemigo
class Enemy(Sprite):

    def __init__(self, ms_game, enemie_number, x, y):

        super().__init__()

        # Instanciamos un soldado para poder reutilizar los métodos para crear los frames 
        self.ms_game = ms_game
        self.soldier = Soldier(ms_game)
        self.screen = ms_game.screen
        self.levels = ms_game.levels
        self.enemies = ms_game.enemies

        # Creamos la ruta del enemigo elegido por parámetro
        self.path_image_run = Paths(f"resources\\pixel_char_pack\\Enemies\\Enemy Patrol\\Enemy{enemie_number}\\Enemy{enemie_number}_sprites\\Enemy{enemie_number}_run.png").__str__()
        self.path_image_fire = Paths(f"resources\\pixel_char_pack\\Enemies\\Enemy Patrol\\Enemy{enemie_number}\\Enemy{enemie_number}_sprites\\Enemy{enemie_number}_fire.png").__str__()

        # Cargamos la ruta de la imagen
        self.image_run = pygame.image.load(self.path_image_run).convert_alpha()
        self.image_fire = pygame.image.load(self.path_image_fire).convert_alpha()

        # Creamos las listas para desarrollar las animaciones
        self.animation_run_front = []
        self.animation_run_back = []

        self.animation_die_front = []
        self.animation_die_back = []

        self.animation_fire_front = []
        self.animation_fire_back = []


        # Creamos los frames
        self.animation_run = self.soldier.make_frames(self.image_run, self.animation_run_front, self.animation_run_back, 8)
        self.animation_die = self.soldier.make_split_frames("death", self.animation_die_front, self.animation_die_back, 8, root='Enemies\\Enemy Patrol\\Enemy1\\Enemy1_sprites')
        self.animation_fire = self.soldier.make_frames(self.image_fire, self.animation_fire_front, self.animation_fire_back, 5)

        self.image = self.animation_run_front[3]
        self.rect = self.image.get_rect(width=40)
        self.rect.x = x
        self.rect.y = y
        self.animation_frame = self.animation_run_front

        self.look_right = True
        self.dead = False
        self.check_frame = True
        self.detect_soldier = False
        self.be_shot = 0
        self.displace_x = 1

        self.frame_index = 0
        self.frame_timer = 0
        self.time_last_shot = 0
        self.time_detect_soldier = 0
        self.is_detecting = False
        self.ready_to_shoot = False

        self.drop = True
        

    
    def animation(self, animation, current_time, velocity_animation = 150):

        if current_time - self.frame_timer > velocity_animation:

            self.image = animation[self.frame_index]
            self.frame_index = (self.frame_index + 1) % len(animation) 
            self.frame_timer = current_time
            

    def standar_position(self, animation_front, animation_back):
        '''Después de cada animación le establecemos una postura estandar al personaje'''

        if self.look_right:
            self.animation_frame = animation_front

        elif self.look_right == False:
            self.animation_frame = animation_back



    def _detecter_collision_enemy(self, current_time):
        
        platforms = self.ms_game.platforms
        collisions = bool(pygame.sprite.spritecollide(self, platforms, False))
        
        if collisions:
            if self.dead == False:
                for platform in platforms:
                    if not isinstance(platform, Stairs):

                        #Si llega a uno de los bordes de la plataforma, su dirección cambia de rumbo
                        if self.rect.colliderect(platform) and self.detect_soldier == False:
                            self.animation(self.animation_frame, current_time)

                            if self.rect.right > platform.rect.right - 10 or self.look_right == False:
                                self.look_right = False
                                self.rect.x -= self.displace_x

                            if self.rect.left < platform.rect.left -10 or self.look_right:
                                self.look_right = True
                                self.rect.x += self.displace_x
                            self.standar_position(self.animation_run_front, self.animation_run_back)

        else:
            self.drop = True
            self.rect.y += self.soldier.settings.displace_y

            

    
    def _die(self, current_time):
        '''Animación de la muerte del enemigo'''
        if self.dead:
            if self.check_frame:
                self.frame_index = 1
                self.check_frame = False
                self.standar_position(self.animation_die_front, self.animation_die_back)
            self.animation(self.animation_frame, current_time)

            if self.frame_index == 0:
                self.enemies.remove(self)
                self.dead = False
                self.check_frame = True

    
    def check_die(self):
        if self.be_shot == 5:
            self.dead = True

    
    def set_direction(self):
        if self.soldier.rect.x < self.rect.x:
            self.look_right = False
        else:
            self.look_right = True

    
    def guard(self, current_time):
        if self.dead == False:
            if self.detect_soldier:
                # Damos un tiempo de tregua entre que detecta a soldado y empieza a disparar
                if self.is_detecting == False:
                    self.time_detect_soldier = self.ms_game.current_time
                    self.is_detecting = True
                # Tregua : 200ms
                if self.ms_game.current_time - self.time_detect_soldier > 250:
                    self.ready_to_shoot = True
                    self.standar_position(self.animation_fire_front, self.animation_fire_back)
                    self.animation(self.animation_frame, current_time, 100)
            else:
                self._detecter_collision_enemy(current_time)
                self.is_detecting = False
                self.ready_to_shoot = False
            


    def update(self, current_time):
        self.check_die()
        self.guard(current_time)
        self._die(current_time)
    

    def blitme(self):    

        self.screen.blit(self.image, self.rect)


        
        





