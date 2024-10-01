import pygame
import sys

from settings import Settings
from soldier import Soldier 
from bullet import Bullet
from environment import Environment, Levels


class Metal_soldier():

    def __init__(self):
        '''Definimos los elementos que componen el juego'''

        pygame.init()

        self.settings = Settings()
        self.screen = self.settings.screen
        self.environment = Environment(self)
        self.levels = Levels(self)
        self.soldier = Soldier(self)
        self.bullets = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        




    def check_events(self):
        '''Gestionamos los eventos del juego'''

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._events_keydown(event)

            elif event.type == pygame.KEYUP:
                self._events_keyup(event)
                



    def _events_keydown(self, event):
        '''Establecemos los eventos para cuando pulsamos las teclas'''
        
        # Ignorar entrada si el soldado está en el aire
        if self.soldier.move_jump:
            return
        
        check_stairs = self.soldier.check_stairs()
        
        # Inicializamos el índice de los frames en 0 antes de cualquier evento
        self.soldier.frame_index = 0 

        if event.key == pygame.K_RIGHT:
            self.soldier.move_right = True
            if self.soldier.look_right == False:
                self.soldier.rect.x = self.soldier.rect.x + 10
            self.soldier.look_right = True

        if event.key == pygame.K_LEFT:
            self.soldier.move_left = True
            if self.soldier.look_right:
                self.soldier.rect.x = self.soldier.rect.x - 10

            self.soldier.look_right = False
            

        if event.key == pygame.K_UP:
            if check_stairs:
                self.soldier.move_stairs_up = True
            else:
                self.soldier.move_jump = True


        if event.key == pygame.K_DOWN:
            if check_stairs:
                self.soldier.move_stairs_down = True
            else:
                self.soldier.be_covered = True

        if event.key == pygame.K_k:
            self.soldier.knife_attack = True


        if event.key == pygame.K_SPACE:
            self.fire_bullet()



    

    def _events_keyup(self, event):
        '''Establecemos los eventos para cuando dejamos de pulsar las teclas'''

        inside_stairs = False
        check_stairs = self.soldier.check_stairs()

        if event.key == pygame.K_RIGHT:
            self.soldier.move_right = False
        
        if event.key == pygame.K_LEFT:
            self.soldier.move_left = False

        if event.key == pygame.K_UP:
            self.soldier.move_stairs_up = False
            if check_stairs:
                inside_stairs = True

        if event.key == pygame.K_DOWN:
            self.soldier.move_stairs_down = False
            self.soldier.be_covered = False

            if check_stairs:
                inside_stairs = True

        if event.key and self.soldier.move_jump == False and self.soldier.knife_attack == False:
            self.soldier.standar_position(inside_stairs)




    

    def fire_bullet(self):
        '''Creamos la bala y la añadimos a la lista'''

        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)


    def bullet_detecter_colision(self):
        '''Detecta y elimina las balas que colisionan o que se salen de la pantalla'''

        platforms = self.levels.make_platforms()

        collisions = pygame.sprite.groupcollide(self.bullets, platforms, True, False)
        
        for bullet in self.bullets:
            if bullet.rect.left > self.settings.screen_width or bullet.rect.right < 0:
                self.bullets.remove(bullet)     # Eliminamos la bala que sobresale por la pantalla


    def update_bullet(self):
        '''Actualizamos las balas'''

        self.bullets.update()      # Desplazamos las balas para darle movimiento
        self.bullet_detecter_colision()




    
    def update_screen(self):
        '''Actualizamos los cambios que se van realizando durante el juego'''

        current_time = pygame.time.get_ticks()  # Obtiene el tiempo actual en millisegundos

        self.screen.fill(self.settings.bg_screen) # Actualiza el color del fondo de la pantalla
        
        self.levels.background()
        self.levels.blitme() # Actualizamos el mapa


        self.soldier.detecter_collision()

        self.soldier.move(current_time)


        for bullet in self.bullets.sprites():
            bullet.blitme()    # Dibujamos las balas

        


    
    def run_game(self):
        '''Motor del juego'''

        while True:
            
            self.check_events()
            self.update_bullet()
            self.update_screen()
            self.soldier.blitme()
    
            pygame.display.flip()
            self.clock.tick(45) # Mantén un framerate constante de 60 FPS



ms_game = Metal_soldier()
ms_game.run_game()
    