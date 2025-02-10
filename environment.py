import pygame
from coordenates_levels import Coordinates, Platform, Stairs
from main_menu import Menu

class Environment():
    

    def __init__(self, ms_game):
        
        self.screen = ms_game.screen
        self.coordinates = Coordinates(ms_game)
        
        self.platform_sprites = pygame.sprite.Group()

        self.screen = ms_game.screen
        self.main_menu = Menu(ms_game)

        self.list_soil = []
        self.flag_soil = True



    def fade(self, speed=3):

        fade_surface = pygame.Surface((1200, 800))
        fade_surface.fill((0, 0, 0))
        
        # FADE IN (Vuelve a aparecer el juego)
        for alpha in range(255, 0, -speed):
            self.main_menu.title()
            fade_surface.set_alpha(alpha)
            self.screen.blit(fade_surface, (0, 0))
            pygame.display.update()
            pygame.time.delay(20)

        pygame.time.delay(2000)


    
    def fade_level(self, level, speed=3):

        fade_surface = pygame.Surface((1200, 800))
        fade_surface.fill((0, 0, 0))
        title_level_image = pygame.image.load(f"resources/fonts/title-level{level}.png").convert_alpha()
        
        # FADE IN (Vuelve a aparecer el juego)
        for alpha in range(255, 0, -speed):
            self.main_menu.title()
            fade_surface.set_alpha(alpha)
            self.screen.blit(fade_surface, (0, 0))
            pygame.display.update()
            pygame.time.delay(20)

        pygame.time.delay(500)

        # FADE IN (Vuelve a aparecer el juego)
        for alpha in range(255, 0, -speed):
            self.main_menu.title_level(title_level_image)
            fade_surface.set_alpha(alpha)
            self.screen.blit(fade_surface, (0, 0))
            self.main_menu.title()
            pygame.display.update()
            pygame.time.delay(20)

        pygame.time.delay(1000)





    def repeat(self, image, repeat,  eje_x, eje_y, direction='x'):
        '''Repetimos la imagen las veces necesarias para crear la que nos interesa. 
        Debemos de tener en cuenta, que si 'direction' tiene el valor 'y', el orden 
        de los ejes se invertirán. La función retorna las las cordenadas del suelo, 
        para posteriormente poder generar la gravedad'''

        for i in range(repeat):
                
            if direction == 'x':
                width = i * image.get_size()[0]
                self.screen.blit(image, (eje_x + width, eje_y))
            
            elif direction == 'y':
                self.screen.blit(image, (eje_y, eje_x + (i * image.get_size()[0])))

        if self.flag_soil and (image in self.coordinates.land_up or image in self.coordinates.cave_edges_up):

            self.list_soil = self.surface_soil_boundaries(image, repeat, eje_x, eje_y)
        


    def surface_soil_boundaries(self, image, repeat, eje_x, eje_y):
        '''Guarda en una lista las coordenadas de los vértices, límites o bordes de las superficies de las plataformas'''

        image_width = image.get_width()
        length_soil = image_width * repeat
        eje_x = (eje_x + length_soil) - image_width
        self.list_soil.append((eje_x, eje_y))
        
        return self.list_soil
    


    def surface_soil(self):
        '''Creamos otra lista con los datos que realmente nos importa. Estamos depurando los datos de la lista anterior, obteniendo así una más simple y dejando fuera los datos que no necesitamos. Ya que solamente estamos guardando tuplas con 3 valores.
        1. Dónde empieza en el eje x
        2. Dónde acaba en el eje x
        3. A qué altura se encuentra en el eje y'''

        vertices = len(self.list_soil)
        coordinates = []

        try:
            for i in range(0, vertices, 2):
                coordinates.append((self.list_soil[i][0], self.list_soil[i+1][0], self.list_soil[i][1]))

            return coordinates
        
        except:
            print("LAS COORDENADAS TIENEN QUE SER PARES")



        
class Levels(Environment):

    def __init__(self, ms_game , number=1):
        super().__init__(ms_game)
        self.level_flag = number

        self.coord_level = self.update_level()

        self.coordinates_soldier = self.coordinates.initial_coordinates_soldier
        self.enemies_count = len(self.coordinates.initial_coordinates_enemies)
        self.coodinates_enemies = self.coordinates.initial_coordinates_enemies
        self.image_back_x = 0


    def update_level(self):
        print(self.level_flag)
        
        if self.level_flag == 0:
            self.coord_level = self.coordinates.level0()
        elif self.level_flag == 1:
            self.coord_level = self.coordinates.level1()
        elif self.level_flag == 2:
            self.coord_level = self.coordinates.level2()
        elif self.level_flag == 3:
            self.coord_level = self.coordinates.level3()



        return self.coord_level


    
    def background(self):
        
        self.repeat(self.coordinates.image_back, 6, self.image_back_x, 0)
        self.repeat(self.coordinates.image_palm, 7, 0, 150)
        
        if self.level_flag == 0:
            self.main_menu.title()
            self.image_back_x -= 1
            if self.image_back_x < -2400:
                self.image_back_x = 0

        if self.level_flag == 1:
            self.repeat(self.coordinates.background_cave, 1, 0, 310)
        self.flag_soil = False
        


    def make_platforms(self):

        for clave, platform in self.coord_level.items():
            height = 0
            width = 0

            for coordinates in platform:

                image, *params = coordinates  # Separa la imagen del resto de los parámetros        

                self.repeat(image, *params)

                if len(self.platform_sprites) < len(self.coord_level):
                    try:
                        if coordinates[4] == 'y':
                            height = coordinates[1] * 20
                            width += 20
                            x = coordinates[3]
                            y = coordinates[2]
                    except:
                            width = coordinates[1] * 20
                            height += 20
                            x = coordinates[2]
                            y = coordinates[3] -height +20

            if len(self.platform_sprites) < len(self.coord_level):


                if clave == 'background':
                    continue
                
                rect = pygame.Rect(x, y, width, height)
                if 'stairs' in clave:
                    platform = Stairs(rect)
                else:
                    platform = Platform(rect)
                self.platform_sprites.add(platform)


        return self.platform_sprites






        

