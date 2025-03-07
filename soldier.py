import pygame
from pygame.sprite import Sprite

from settings import Settings
from paths import Paths
from environment import  Stairs


class Soldier(Sprite):
    '''Creamos el personaje principal del juego'''

    def __init__(self, ms_game):


        self.settings = Settings()
        self.environment = ms_game.environment
        self.levels = ms_game.levels
        self.platforms = self.levels.make_platforms()

        self.screen = ms_game.screen
        self.screen_rect = self.screen.get_rect()

        self.path_image_soldiers_run = Paths('resources\\pixel_char_pack\\Player\\Sprites\\Player_run.png').__str__()
        self.path_image_soldiers_jump = Paths('resources\\pixel_char_pack\\Player\\Sprites\\Player_jump.png').__str__()
        self.path_image_knife_attack = Paths('resources\\pixel_char_pack\\Player\\Sprites\\Player_knife_attack.png').__str__()
        self.path_image_crawl_stairs = Paths('resources\\pixel_char_pack\\Player\\Sprites\\crawl_stairs.png').__str__()
        self.path_image_be_shoted_soldier = Paths('resources\\pixel_char_pack\\Player\\Sprites\\player_be_shoted_red.png').__str__()

        
        self.image_soldiers_run = pygame.image.load(self.path_image_soldiers_run).convert_alpha()
        self.image_soldiers_jump = pygame.image.load(self.path_image_soldiers_jump).convert_alpha()
        self.image_soldiers_knife_attack = pygame.image.load(self.path_image_knife_attack).convert_alpha()
        self.image_crawl_stairs = pygame.image.load(self.path_image_crawl_stairs).convert_alpha()
        self.image_be_shoted_soldier = pygame.image.load(self.path_image_be_shoted_soldier).convert_alpha()
        self.image_be_shoted_reverse = pygame.transform.flip(self.image_be_shoted_soldier, True, False)




        # VARIABLES DE ANIMACIÓN

        # Animación de correr
        self.sprite_width = self.image_soldiers_run.get_width() // 8
        self.sprite_height = self.image_soldiers_run.get_height()
        self.animation_run_front = []
        self.animation_run_back = []

        # Animación de saltar
        self.animation_jump_front = []
        self.animation_jump_back = []

        # Variables para llevar a cabo la animación
        self.frame_index = 0
        self.frame_timer = 0
        self.hearts = 3
        self.times_touched = 3
        self.be_shot = 0

        # Banderas de movimiento 
        self.move_right = False
        self.move_left = False
        self.move_flag = True
        self.look_right = True
        self.move_jump = False
        self.be_covered = False
        self.knife_attack = False
        self.move_stairs_up = False
        self.move_stairs_down = False
        self.dead = False
        self.stay_in_floor = False
        self.drop = True
        self.update_indicators = False
        
        
        # GUARDAMOS LAS IMÁGENES ANIMADAS EN LISTAS

        # Animación de correr
        self.animation_run_front = []
        self.animation_run_back = []
        
        # Animación de saltar
        self.animation_jump_front = []
        self.animation_jump_back = []

        # Animación de estar a cubierto
        self.animation_be_covered_front = []
        self.animation_be_covered_back = []

        # Animación de ataque con cuchillo
        self.animation_knife_attack_front = []
        self.animation_knife_attack_back = []

        # Animación de escalar escaleras
        self.animation_crawl_stairs_front = []
        self.animation_crawl_stairs_back = []

        # Animación de morir
        self.animation_die_front = []
        self.animation_die_back = []

        # Creamos las animaciones
        self.make_frames(self.image_soldiers_run, self.animation_run_front, self.animation_run_back, 8)
        self.make_frames(self.image_soldiers_jump,  self.animation_jump_front, self.animation_jump_back, 2)   # Ascenso del salto
        self.make_frames(self.image_soldiers_jump, self.animation_jump_front, self.animation_jump_back, -1, 2, -1)    # Aterrizaje del salto

        
        self.make_frames(self.image_soldiers_knife_attack, self.animation_knife_attack_front, self.animation_knife_attack_back, 7)
        self.make_frames(self.image_crawl_stairs, self.animation_crawl_stairs_front, self.animation_crawl_stairs_back, 5)

        self.make_split_frames("death", self.animation_die_front, self.animation_die_back, 8)
        self.make_split_frames("be_covered", self.animation_be_covered_front, self.animation_be_covered_back, 3)

        # Eliminamos la lista de la animación de bajar la escalera porque no la necesitamos
        del self.animation_crawl_stairs_front
    
        self.image = self.animation_run_front[3]
        self.rect = self.image.get_rect(width=40)
        self.rect.x = self.levels.coordinates_soldier[0]
        self.rect.y = self.levels.coordinates_soldier[1]
        self.animation_frame = self.animation_run_front
        
        self.stairs_rect = self.save_stairs_rect()

        


    
    def make_frames(self, image, list_frames, list_frames_reverse, rango_fin, rango_ini=0, recorrido=1):
        '''Creación a utomatizada de los frames que se usarán en las animaciones'''

        for i in range(rango_ini, rango_fin, recorrido):
            frame = image.subsurface((i * self.sprite_width) +46, 0, self.sprite_width-55, self.sprite_height)
            list_frames.append(frame)

            frame = image.subsurface((i * self.sprite_width), 0, self.sprite_width-18, self.sprite_height)
            frame_reverse = pygame.transform.flip(frame, True, False)
            list_frames_reverse.append(frame_reverse)

    

    def make_split_frames(self, folder, list_frames_front, list_frames_reverse, num_images, root='Player\\Sprites'):
	
        for i in range(num_images):
            path_image = Paths(f"resources\\pixel_char_pack\\{root}\\{folder}\\{folder}{i}.png").__str__()
                
            frame = pygame.image.load(path_image).convert_alpha()
            
            list_frames_front.append(frame)
            
            frame_reverse = pygame.transform.flip(frame, True, False)
            
            list_frames_reverse.append(frame_reverse)




    def standar_position(self, animation_front, animation_back):
        '''Después de cada animación le establecemos una postura estandar al personaje'''

        if self.look_right:
            self.animation_frame = animation_front

        else:
            self.animation_frame = animation_back


    def detect_stairs(self, inside_stairs):
        if inside_stairs and (self.rect.bottom -9 >= self.stairs_rect.top or self.rect.top > self.stairs_rect.bottom):
            pygame.draw.rect(self.screen, (0, 0, 255), self.stairs_rect)
            self.image = self.animation_crawl_stairs_back[3]

        return self.stairs_rect



    def animation(self, animation, current_time, velocity_animation = 100):
        '''Actualizamos la animación de correr del personaje'''

        if current_time - self.frame_timer > velocity_animation:
            self.image = animation[self.frame_index]
            self.frame_index = (self.frame_index + 1) % len(animation) 
            self.frame_timer = current_time

    
    def animation_be_shoted(self):
        if self.look_right:
            self.image = self.image_be_shoted_soldier
        else:
            self.image = self.image_be_shoted_reverse
        

            
    
    def _move_run(self, current_time):
        '''Generamos el movimiento del soldado cuando corre hacia la izquierda y hacia la derecha'''

        if self.be_covered == False and self.knife_attack == False:
            
            if self.move_jump and self.frame_index > 1:
                self.settings.displace_x = 5
            else:
                self.settings.displace_x = 3

            if self.move_right and self.rect.right < self.screen_rect.right + 20 and self.drop == False: # Ajustamos limites
                self.rect.x += self.settings.displace_x
                if self.move_jump == False:
                    self.animation(self.animation_run_front, current_time)

            if self.move_left and self.rect.left > -20 and self.drop == False:
                self.rect.x -= self.settings.displace_x
                if self.move_jump == False:
                    self.animation(self.animation_run_back, current_time)



    def _move_jump(self, current_time):
        '''Animación del salto'''

        if self.move_jump and self.drop == False:

            self.standar_position(self.animation_jump_front, self.animation_jump_back)

            if self.frame_index == 2:
                self.rect.y -= self.settings.displace_y 
                
            elif self.frame_index == 4:
                self.move_jump = False
            
            self.animation(self.animation_frame, current_time)




    def _be_covered(self, current_time):
        '''Animación en la que el personaje se tira al suelo para estar a cubierto'''

        if self.be_covered:

            self.standar_position(self.animation_be_covered_front, self.animation_be_covered_back)

            self.animation(self.animation_frame, current_time)

            if self.frame_index > 1 or self.stay_in_floor == True: # Para que se mantenga tendido en el suelo
                self.stay_in_floor = True
                self.frame_index = 2

        else:
            self.standar_position(self.animation_be_covered_front, self.animation_be_covered_back)




    def _knife_attack(self, current_time):
        '''Animación del ataque con cuchillo'''

        if self.knife_attack:

            self.standar_position(self.animation_knife_attack_front, self.animation_knife_attack_back)

            self.animation(self.animation_frame, current_time)

            if self.frame_index == 0:
                self.knife_attack = False



    def check_stairs(self):
        '''Comprobamos si el soldado está debajo o encima de las escaleras de las escaleras'''

        for platform in self.platforms:
            if isinstance(platform, Stairs):
                if self.rect.colliderect(platform.rect):
                    return platform

                
    
    def save_stairs_rect(self):
        '''Guardamos as coordenadas de las escaleras en el constructor'''

        for platform in self.platforms:
            if isinstance(platform, Stairs):
                stairs = platform
                stairs_rect = stairs.rect
                return stairs_rect



    def _crawl_stairs(self, current_time):
        '''Animación del subir y bajar escaleras'''

        platforms = self.levels.make_platforms()
        stairs = self.check_stairs()

        if stairs:
        
            if self.move_stairs_down:
                self.animation(self.animation_crawl_stairs_back, current_time)
                self.rect.x = stairs.rect.x - 30
                self.rect.y += 1

            elif self.move_stairs_up:
                self.animation(self.animation_crawl_stairs_back, current_time)
                self.rect.x = stairs.rect.x - 30
                self.rect.y -= 1

            else: # Empiece la animación de crawl_stairs en cuanto el soldado se pone en contacto con las escaleras
                if self.rect.y > stairs.rect.y:
                    self.image = self.animation_crawl_stairs_back[0]




    def move(self, current_time):
        '''Agrupamos en esta función todas las animaciones de los movimientos del personaje'''
        self._move_run(current_time)
        self._move_jump(current_time)
        self._be_covered(current_time)
        self._knife_attack(current_time)
        self._crawl_stairs(current_time)
        self.fall_into_the_void()
        self._die(current_time)



    def detecter_collision(self):
        '''Esta función comprueba si el personaje se encuentra en la superficie de una plataforma o no.
        Esto lo generamos para saber si la gravedad tendrá que ejercer su fuerza o no.
        'drop' está a True de forma determinada por que la caida se lleva a cabo a no ser que la 
        condición diga la contrario'''


        # Ajustamos los píxeles por que el rect del soldado no está proporcionado con sus pies, 

        # Esto deberíamos dividirlo en funciones más pequeñas
        if self.move_right or self.look_right:
            margin = 10
            margin_right = 12

        elif self.move_left or self.look_right == False:
            margin = -10
            margin_right = -30

        if self.check_stairs():
            self.drop = False
        else:
            self.drop = True

        for platform in self.platforms:

            # Detecta las colisiones 
            if self.rect.colliderect(platform):

                #Detecta la colision del soldado sobre la plataforma
                if self.rect.y <= platform.rect.top and (self.rect.right > platform.rect.left + margin and self.rect.left < platform.rect.right + margin_right):
                    self.drop = False

                # Detecta la colision desde la izquierda
                if self.rect.right > platform.rect.left and self.rect.bottom -10 > platform.rect.top and self.rect.left < platform.rect.left or self.rect.right > 1200:
                    self.move_right = False
        
                # Detecta la colision desde la derecha
                elif self.rect.left < platform.rect.right and self.rect.bottom-10 > platform.rect.top  and self.move_jump == False or self.rect.left < 0:
                    self.move_left = False
                    
        # Que la gravedad no afecta al soldado durante el salto hasta que este se encuentre en el aire        
        if self.move_jump and self.frame_index >= 2:
            self.drop = False

        if self.drop == True:
            self.rect.y += 10

    
    def fall_into_the_void(self):
        if self.rect.y > 800:
            self.dead = True



    def _die(self, current_time):
        if self.be_shot >= 3 and self.dead == False:
            self.move_left = False
            self.move_right = False
            self.be_covered = False
            self.knife_attack = False
            self.frame_index = 0
            self.dead = True

        if self.dead:

            self.standar_position(self.animation_die_front, self.animation_die_back)

            self.animation(self.animation_frame, current_time, velocity_animation=150)

            if self.frame_index == 7:
                self.rect.x = self.levels.coordinates_soldier[0]
                self.rect.y = self.levels.coordinates_soldier[1]
                self.be_shot = 0
                self.image = self.animation_run_front[3]
                self.dead = False
                self.update_indicators = True
                self.times_touched = 3
                self.hearts -= 1
                print("Hearts: ", self.hearts)


    def blitme(self):    

        self.screen.blit(self.image, self.rect)

        # for platform in self.platforms:

        #     pygame.draw.rect(self.screen, (255,0,0), platform.rect)

    
