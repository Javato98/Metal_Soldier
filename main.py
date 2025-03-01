import pygame
import sys

from settings import Settings
from soldier import Soldier 
from bullet import Bullet
from environment import Environment, Levels
from enemies import Enemy
from main_menu import Menu
from scoreboard import Scoreboard



class Metal_soldier():

    def __init__(self):
        '''Definimos los elementos que componen el juego'''

        pygame.init()

        self.settings = Settings()
        self.screen = self.settings.screen
        self.environment = Environment(self)
        self.levels = Levels(self, 0)
        self.bullets = pygame.sprite.Group()
        self.main_menu = Menu(self)
        self.clock = pygame.time.Clock()
        self.scoreboard = Scoreboard(self)
        
        self.platforms = self.levels.make_platforms()
        self.main_menu_buttons = self.main_menu.buttons

        self.flag_animation_transition = True
        self.level_number = 0

     
        self.levels.update_level()
        self.create_characters()
        self.make_enemies()
        
        

    def check_events(self):
        '''Gestionamos los eventos del juego'''
        self._event_hover()

        for event in pygame.event.get():
            if self.levels.level_flag == 0:
                self._event_click(event)

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._events_keydown(event)

            elif event.type == pygame.KEYUP:
                self._events_keyup(event)
                


    def _events_keydown(self, event):
        '''Establecemos los eventos para cuando pulsamos las teclas'''

        if self.soldier.dead == False:

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
            if self.soldier.move_jump:
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
                    self.soldier.stay_in_floor = False
                    self.soldier.be_covered = True
 
            if event.key == pygame.K_k:
                self.soldier.knife_attack = True
                self.soldier.frame_index = 1

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

        # Establecemos el frame determinado si el soldado no está ejecutando ninguna animación
        if event.key and self.soldier.move_jump == False and self.soldier.knife_attack == False:
            self.soldier.standar_position(self.soldier.animation_run_front, self.soldier.animation_run_back)
            self.soldier.image = self.soldier.animation_frame[3]
            self.soldier.detect_stairs(inside_stairs)
            

    def _event_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        for i, button in enumerate(self.main_menu_buttons):
            if button.msg_image_rect.collidepoint(mouse_pos):
                button.text_color = (255, 121, 64)
            else:
                button.text_color = (255, 255, 58)

            button = button._prep_msg(self.main_menu.button_texts[i]) 
                

    def _event_click(self, event):
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.main_menu_buttons:
                if button.msg_image_rect.collidepoint(event.pos):
                    if button == self.main_menu_buttons[0]:
                        self.environment.game_over_menu = False
                        self.level_up()


# Tenemos que meter las instrucciones
                    elif button == self.main_menu_buttons[2]:
                        sys.exit()

        


    def create_characters(self):
        if self.level_number > 1:
            save_hearts = self.soldier.hearts
            self.soldier = Soldier(self)
            self.soldier.hearts = save_hearts
            self.update_scoreboard()
        else:
            self.soldier = Soldier(self)
        self.enemies = pygame.sprite.Group()
        self.make_enemies()



    def bullet_detecter_colision(self):
        '''Detecta y elimina las balas que colisionan o que se salen de la pantalla'''
        collisions = pygame.sprite.groupcollide(self.bullets, self.platforms, True, False)
        
        for bullet in self.bullets:
            if bullet.rect.left > self.settings.screen_width or bullet.rect.right < 0:
                self.bullets.remove(bullet)     # Eliminamos la bala que sobresale por la pantalla


    
    def fire_bullet(self, character):
        '''Creamos la bala y le damos una frecuencia de disparo si es el enemigo'''
            
        if character != self.soldier:
            if character.ready_to_shoot:
                if self.current_time - character.time_last_shot > 600:
                    self.create_bullet(character)
                    character.time_last_shot = self.current_time
        else:
            self.create_bullet(character)


    def create_bullet(self, character):
        '''Creamos la bala y la añadimos a la lista'''
        new_bullet = Bullet(self, character)
        self.bullets.add(new_bullet)


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
                        enemy.animation_be_shoted()
                        self.bullets.remove(bullet) 
                        enemy.be_shot += 1



    def kill_enemy(self):
        '''Muertes del enemigo, apuñalado o disparado'''
        self.knife_kill()
        self.bullet_kill()
        
        if len(self.enemies) <= 0:
            self.level_up()


    def level_up(self):
        self.level_number += 1
        self.levels = Levels(self, self.level_number)
        # self.environment.fade_level(self.level_number)
        self.platforms = self.levels.make_platforms()
        self.create_characters()

        
    def make_enemies(self):

        for i in range(self.levels.enemies_count):
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


    def shoot_us(self):
        '''Nos dispara el enemigo'''

        for bullet in self.bullets:
            if bullet.character != self.soldier:
                if bullet.rect.colliderect(self.soldier):
                    self.bullets.remove(bullet)
                    self.shot_received_soldier()
                    self.remove_endurance_indicator_soldier()


    def shot_received_soldier(self):
        '''Animación y apuntamos el disparo recibido'''
        self.soldier.animation_be_shoted()
        self.soldier.be_shot += 1

        

    def remove_endurance_indicator_soldier(self):
        '''Quitamos el muñeco de ser disparo del scoreboard'''
        self.soldier.times_touched -= 1
        self.scoreboard.times_touched = self.scoreboard.prep_touched(self.soldier.times_touched)

    
    def game_over(self):

        if self.soldier.hearts < 1:
            self.environment.game_over_animation()

    def update_scoreboard_new_game(self):
        if self.environment.game_over_menu:
            self.levels.level_flag = 0
            self.level_number = 0
            self.soldier.hearts = 3
            self.update_scoreboard()


    def update_scoreboard(self):
        self.scoreboard.times_touched = self.scoreboard.prep_touched(self.soldier.times_touched)
        self.scoreboard.hearts = self.scoreboard.prep_heart(self.soldier.hearts)
        self.soldier.update_indicators = False


    
    def update_screen(self):
        '''Actualizamos los cambios que se van realizando durante el juego'''

        self.current_time = pygame.time.get_ticks()  # Obtiene el tiempo actual en millisegundos

        self.screen.fill(self.settings.bg_screen) # Actualiza el color del fondo de la pantalla
        
        self.levels.background()
        self.game_over()
        self.update_scoreboard_new_game()


        if self.levels.level_flag == 0:
            if self.environment.game_over_menu:
                self.screen.fill((0, 0, 0))
                self.main_menu.title('resources/fonts/title-game-over.png')   
            if self.flag_animation_transition:
                # self.environment.fade(speed=2)
                self.flag_animation_transition = False
            self.main_menu.create_menu()
        else:
            self.soldier.detecter_collision()
            self.kill_enemy()
            self.shoot_us()

            for bullet in self.bullets.sprites():
                bullet.blitme()  

            self.soldier.move(self.current_time)
            # VAMOS A PONER EL SOLDIER.DEAD A PARTE
            
            ''' Si el soldado ha muerto actualizamos el scoreboard'''
            if self.soldier.update_indicators:
                self.update_scoreboard()
                

            self.enemies.update(self.current_time)
            self.detect_soldier()

            self.update_bullet()
            self.soldier.blitme()
            

            self.scoreboard.draw()


            for enemy in self.enemies.sprites():
                enemy.blitme()




    
    def run_game(self):
        '''Motor del juego'''

        while True:

            self.check_events()
            self.update_screen()
    
            pygame.display.flip()
            self.clock.tick(45) # Mantén un framerate constante de 60 FPS


ms_game = Metal_soldier()
ms_game.run_game()
    