import pygame
import sys

from settings import Settings
from soldier import Soldier 
from bullet import Bullet
from environment import Environment, Levels
from enemies import Enemy


class Metal_soldier():

    def __init__(self):
        '''Definimos los elementos que componen el juego'''

        pygame.init()

        self.settings = Settings()
        self.screen = self.settings.screen
        self.environment = Environment(self)
        self.levels = Levels(self, 2, ((500, 300), (700, 100)))
        self.soldier = Soldier(self)
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.clock = pygame.time.Clock()

        self.last_shot_enemy = 0
     
        self.make_enemies()


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
        
        # Ignorar entrada si el soldado está en el aire o está muerto
        if self.soldier.move_jump or self.soldier.dead:
            return
        
        check_stairs = self.soldier.check_stairs()
        
        # Inicializamos el índice de los frames en 0 antes de cualquier evento
        self.soldier.frame_index = 0 


            

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
            self.fire_bullet(self.soldier)



    

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
                self.look_right = False
                inside_stairs = True

        if event.key and self.soldier.move_jump == False and self.soldier.knife_attack == False:
            self.soldier.standar_position(inside_stairs)




    def bullet_detecter_colision(self):
        '''Detecta y elimina las balas que colisionan o que se salen de la pantalla'''

        platforms = self.levels.make_platforms()

        collisions = pygame.sprite.groupcollide(self.bullets, platforms, True, False)
        
        for bullet in self.bullets:
            if bullet.rect.left > self.settings.screen_width or bullet.rect.right < 0:
                self.bullets.remove(bullet)     # Eliminamos la bala que sobresale por la pantalla


    
    def fire_bullet(self, character):
        '''Creamos la bala y le damos una frecuencia de disparo si es el enemigo'''

        def create_bullet(self, character):
            '''Creamos la bala y la añadimos a la lista'''
            new_bullet = Bullet(self, character)
            self.bullets.add(new_bullet)
            

        if character != self.soldier:
            if self.current_time - self.last_shot_enemy > 600:
                create_bullet(self, character)
                self.last_shot_enemy = self.current_time

        else:
            create_bullet(self, character)




    def update_bullet(self):
        '''Actualizamos las balas'''

        self.bullets.update()      # Desplazamos las balas para darle movimiento
        self.bullet_detecter_colision()



    def knife_kill(self):
        '''Apuñalamos al enemigo'''
        for enemy in self.enemies.sprites():
            if self.soldier.rect.colliderect(enemy) and self.soldier.knife_attack:
                enemy.dead = True

    

    def bullet_kill(self):
        '''Disparamos al enemigo'''

        for bullet in self.bullets:
            if bullet.character == self.soldier:
                for enemy in self.enemies:
                    if bullet.rect.colliderect(enemy):
                        self.bullets.remove(bullet) 
                        enemy.be_shot += 1


    def kill_enemy(self):
        '''Muertes del enemigo, apuñalado o disparado'''
        self.knife_kill()
        self.bullet_kill()


        
    def make_enemies(self):

        for i in range(2):
            enemy = Enemy(self, 1, self.levels.coodinates_enemies[i][0], self.levels.coodinates_enemies[i][1])
            self.enemies.add(enemy)



    def detect_soldier(self):
        '''El enemigo detecta al soldado y dispara'''

        for enemy in self.enemies:
            if (enemy.rect.y - self.soldier.rect.y) <= 10 and (enemy.rect.y - self.soldier.rect.y) >= -10:
                if enemy.detect_soldier == False:
                    enemy.detect_soldier = True
                    enemy.frame_index = 0
                self.fire_bullet(enemy)
            else:
                enemy.detect_soldier = False


    def kill_us(self):
        '''Disparamos al enemigo'''

        for bullet in self.bullets:
            if bullet.character != self.soldier:
                if bullet.rect.colliderect(self.soldier):
                    self.bullets.remove(bullet) 
                    self.soldier.be_shot += 1


    
    def update_screen(self):
        '''Actualizamos los cambios que se van realizando durante el juego'''

        self.current_time = pygame.time.get_ticks()  # Obtiene el tiempo actual en millisegundos

        self.screen.fill(self.settings.bg_screen) # Actualiza el color del fondo de la pantalla
        
        self.levels.background()
        self.levels.blitme() # Actualizamos el mapa


        self.soldier.detecter_collision()
        self.kill_enemy()
        self.kill_us()

        self.soldier.move(self.current_time)
        self.enemies.update(self.current_time)
        self.detect_soldier()

        self.update_bullet()

        for bullet in self.bullets.sprites():
            bullet.blitme()    # Dibujamos las balas

        for enemy in self.enemies.sprites():
            enemy.blitme()



    
    def run_game(self):
        '''Motor del juego'''

        while True:
            
            self.check_events()
            self.update_screen()
            self.soldier.blitme()
    
            pygame.display.flip()
            self.clock.tick(45) # Mantén un framerate constante de 60 FPS


ms_game = Metal_soldier()
ms_game.run_game()
    