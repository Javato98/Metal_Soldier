import pygame
from paths import Paths



class EnvironmentFrames():

    def __init__(self, ms_game):

        
        
        self.screen = ms_game.screen

        self.image_back = self.make_image('back.png', 1.6)
        self.image_palm = self.make_image('surfaces\\middle.png')
        self.land_up1 = self.make_image('surfaces\\land_up1.png')
        self.land_up0 = self.make_image('surfaces\\land_up0.png')
        self.land_up1 = self.make_image('surfaces\\land_up1.png')
        self.land_up2 = self.make_image('surfaces\\land_up2.png')
        self.wood_up0 = self.make_image('surfaces\\wood_up0.png')
        self.wood_up1 = self.make_image('surfaces\\wood_up1.png')
        self.wood_up2 = self.make_image('surfaces\\wood_up2.png')
        self.land_middle0 = self.make_image('surfaces\\land_middle0.png')
        self.land_middle1 = self.make_image('surfaces\\land_middle1.png')
        self.land_middle2 = self.make_image('surfaces\\land_middle2.png')
        self.land_down0 = self.make_image('surfaces\\land_down0.png')
        self.land_down1 = self.make_image('surfaces\\land_down1.png')
        self.land_down2 = self.make_image('surfaces\\land_down2.png')
        self.branch_left = self.make_image('objects\\branch_left.png')
        self.branch_right = self.make_image('objects\\branch_right.png')
        self.cut_tree = self.make_image('objects\\cut_tree.png')
        self.fallen_tree = self.make_image('objects\\fallen_tree.png')
        self.grass0 = self.make_image('objects\\grass0.png')
        self.grass1 = self.make_image('objects\\grass1.png')
        self.stairs = self.make_image('objects\\stairs.png')
        self.column_left = self.make_image('cave\\column_left.png')
        self.column_right = self.make_image('cave\\column_right.png')
        self.edge = self.make_image('cave\\edge.png')
        self.edge2 = self.make_image('cave\\edge2.png')
        self.edge3 = self.make_image('cave\\edge3.png')
        self.high_rock_left = self.make_image('cave\\high_rock_left.png')
        self.high_rock_right = self.make_image('cave\\high_rock_right.png')
        self.ivy = self.make_image('cave\\ivy.png')
        self.ivy2 = self.make_image('cave\\ivy2.png')
        self.ivy3 = self.make_image('cave\\ivy3.png')
        self.liana1 = self.make_image('cave\\liana1.png')
        self.liana2 = self.make_image('cave\\liana2.png')
        self.ruins = self.make_image('cave\\ruins.png')
        self.ruins2 = self.make_image('cave\\ruins2.png')
        self.ruins3 = self.make_image('cave\\ruins3.png')
        self.ruins4 = self.make_image('cave\\ruins4.png')
        self.stalactite = self.make_image('cave\\stalactite.png')
        self.stalactite2 = self.make_image('cave\\stalactite2.png')
        self.torch = self.make_image('cave\\torch.png')
        self.tribal_piece = self.make_image('cave\\tribal_piece.png')
        self.tribal_piece2 = self.make_image('cave\\tribal_piece2.png')



        self.land_up = [self.land_up0, self.land_up1, self.land_up2]
        self.cave_edges_up = [self.wood_up0, self.wood_up1, self.wood_up2]



        # self.path_back = Paths('resources\\Sunny-land-assets-files\\PNG\\environment\\layers\\back.png').__str__()
        # self.path_middle = Paths('resources\\Sunny-land-assets-files\\PNG\\environment\\layers\\middle.png').__str__()
        # self.path_land = Paths('resources\\Sunny-land-assets-files\\PNG\\environment\\layers\\land.png').__str__()
        # self.path_stone_grass = Paths('resources\\Sunny-land-assets-files\\PNG\\environment\\layers\\stone_and_grass.png').__str__()
        # self.path_cave_edges = Paths('resources\\Sunny-land-assets-files\\PNG\\environment\\layers\\cave_edges.png').__str__()
        # self.path_stairs= Paths('resources\\Sunny-land-assets-files\\PNG\\environment\\layers\\stairs.png').__str__()

        # #Cargamos las imágenes
        # self.image_back = pygame.image.load(self.path_back).convert_alpha()
        # self.image_palm = pygame.image.load(self.path_middle).convert_alpha()
        # self.image_land = pygame.image.load(self.path_land).convert_alpha()
        # self.stone_grass = pygame.image.load(self.path_stone_grass).convert_alpha()
        # self.cave_edges = pygame.image.load(self.path_cave_edges).convert_alpha()
        # self.stairs = pygame.image.load(self.path_stairs).convert_alpha()

        
        
        # # Recolectamos los paquetes de imágenes que necesitamos y lo guardamos en listas
        # self.land_up = self.make_subimages(self.image_land, 5, 5)
        # self.land_middle = self.make_subimages(self.image_land, 5, 5, 2)
        # self.land_down = self.make_subimages(self.image_land, 5, 5, 4)

        # self.stone_grass = self.make_subimages(self.stone_grass, 4, 2, 0, False)

        # self.cave_edges_up = self.make_subimages(self.cave_edges, 5, 5)
        # self.cave_edges_middle = self.make_subimages(self.cave_edges, 5, 5, 2)
        # self.cave_edges_down = self.make_subimages(self.cave_edges, 5, 5, 4)

        


        # #Acumentamos el tamaño de las imágenes
        # self.image_back = self.increase(self.image_back, 1.6)
        # self.stairs = self.increase(self.stairs)
        # self.land_up = self.increase_iteration(self.land_up)
        # self.land_middle = self.increase_iteration(self.land_middle)
        # self.land_down = self.increase_iteration(self.land_down)

        # self.cave_edges_up = self.increase_iteration(self.cave_edges_up)
        # self.cave_edges_middle = self.increase_iteration(self.cave_edges_middle)
        # self.cave_edges_down = self.increase_iteration(self.cave_edges_down)




    def make_image(self, root, increase=1.3):

        path = Paths(f'resources\\Sunny-land-assets-files\\PNG\\environment\\layers\\{root}').__str__()
        image = pygame.image.load(path).convert_alpha()
        increased_image = self.increase(image, increase)
        return increased_image
    


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
    
        

    def increase(self, image, increase):
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
    