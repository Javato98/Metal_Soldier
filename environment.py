import pygame
from coordenates_levels import Coordinates, Platform




class Environment():
    

    def __init__(self, ms_game):
        
        self.screen = ms_game.screen
        self.coordinates = Coordinates(ms_game)
        self.platform_sprites = pygame.sprite.Group()

        self.screen = ms_game.screen

        self.list_soil = []
        self.flag_soil = True
        self.coord_level2 = self.coordinates.level2()

        
        

    def repeat(self, image, repeat,  eje_x, eje_y, direction='x', id='p'):
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

    def __init__(self, ms_game):
        super().__init__(ms_game)

    
    def background(self):
        
        self.repeat(self.coordinates.image_back, 2, 0, 0)
        self.repeat(self.coordinates.image_palm, 7, 0, 150)
        



    def make_platforms(self):
        stairs = False

        
        for platform in self.coord_level2:
            height = 0


            for coordinates in platform:


                image, *params = coordinates  # Separa la imagen del resto de los parámetros        

                self.repeat(image, *params)


                if len(self.platform_sprites) < len(self.coord_level2):
                    try:
                        if coordinates[4] == 'y':
                            pass
                    except:
                        width = coordinates[1] * 20
                        height = height + 20
                        x = coordinates[2]
                        y = coordinates[3] -height +20


            if len(self.platform_sprites) < len(self.coord_level2):
                

                if 'stairs' in coordinates:
                    stairs = True

                
                rect = pygame.Rect(x, y, width, height)
                if stairs:
                    platform = Platform(rect, 'stairs')
                else:
                    platform = Platform(rect)
                stairs = False
                self.platform_sprites.add(platform)

        return self.platform_sprites




    def blitme(self):
        '''Recuerda que el número de repeats tiene que ser par'''   

        self.flag_soil = False

