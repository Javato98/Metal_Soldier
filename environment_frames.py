import pygame
from paths import Paths



class EnvironmentFrames():

    def __init__(self, ms_game):
        
        self.screen = ms_game.screen



        self.path_back = Paths('resources\\Sunny-land-assets-files\\PNG\\environment\\layers\\back.png').__str__()
        self.path_middle = Paths('resources\\Sunny-land-assets-files\\PNG\\environment\\layers\\middle.png').__str__()
        self.path_land = Paths('resources\\Sunny-land-assets-files\\PNG\\environment\\layers\\land.png').__str__()
        self.path_stone_grass = Paths('resources\\Sunny-land-assets-files\\PNG\\environment\\layers\\stone_and_grass.png').__str__()
        self.path_cave_edges = Paths('resources\\Sunny-land-assets-files\\PNG\\environment\\layers\\cave_edges.png').__str__()
        self.path_stairs= Paths('resources\\Sunny-land-assets-files\\PNG\\environment\\layers\\stairs.png').__str__()

        #Cargamos las imágenes
        self.image_back = pygame.image.load(self.path_back)
        self.image_palm = pygame.image.load(self.path_middle)
        self.image_land = pygame.image.load(self.path_land)
        self.stone_grass = pygame.image.load(self.path_stone_grass)
        self.cave_edges = pygame.image.load(self.path_cave_edges)
        
        self.stairs = pygame.image.load(self.path_stairs)

        
        
        # Recolectamos los paquetes de imágenes que necesitamos y lo guardamos en listas
        self.land_up = self.make_subimages(self.image_land, 5, 5)
        self.land_middle = self.make_subimages(self.image_land, 5, 5, 2)
        self.land_down = self.make_subimages(self.image_land, 5, 5, 4)

        self.stone_grass = self.make_subimages(self.stone_grass, 4, 2, 0, False)

        self.cave_edges_up = self.make_subimages(self.cave_edges, 5, 5)
        self.cave_edges_middle = self.make_subimages(self.cave_edges, 5, 5, 2)
        self.cave_edges_down = self.make_subimages(self.cave_edges, 5, 5, 4)

        


        #Acumentamos el tamaño de las imágenes
        self.image_back = self.increase(self.image_back, 1.6)
        self.stairs = self.increase(self.stairs)
        self.land_up = self.increase_iteration(self.land_up)
        self.land_middle = self.increase_iteration(self.land_middle)
        self.land_down = self.increase_iteration(self.land_down)

        self.cave_edges_up = self.increase_iteration(self.cave_edges_up)
        self.cave_edges_middle = self.increase_iteration(self.cave_edges_middle)
        self.cave_edges_down = self.increase_iteration(self.cave_edges_down)
        
        


    def make_subimages(self, image, num_images_x, num_images_y, altura = 0, empty_space=True):
        '''Creamos las imágenes unitarias que necesitamos para crear el mapa'''
        


        image_width = image.get_width() // num_images_x
        image_height = image.get_height() // num_images_y

        frame_list = []

        for i in range(num_images_x):
            if empty_space: # Para ver si queremos quitar los espacios de en medio
                if i % 2 == 0:  # No queremos los espacios vacíos
                    #Aquí estamos obteniendo las imágenes en función de las medidas de la imagen padre que las contiene
                    frame = image.subsurface(i * image_width, image_height * altura, image_width, image_height)
                    frame_list.append(frame)
            else:
                frame = image.subsurface(i * image_width, image_height * altura, image_width, image_height)
                frame_list.append(frame)


        return frame_list
    
        

    def increase(self, image, increase=1.3):
        '''Incrementamos el tamaño de la imagen en relación a su proporción original'''

        image_width = image.get_width() * increase
        image_height = image.get_height() * increase

        image_size = (image_width, image_height)
        image = pygame.transform.scale(image, image_size)


        return image
    


    
    def increase_iteration(self, list_images):
        '''Hace lo mismo que increase, pero no para una sola imagen, si no para todas las imágenes empaquetadas en la lista'''

        for i in range(len(list_images)):
            image = self.increase(list_images[i])
            list_images[i] = image

        return list_images
    