import pygame
from paths import Paths



class EnvironmentFrames():

    def __init__(self, ms_game):

        self.screen = ms_game.screen

        self.image_back = self.make_image('back.png', 1.6)
        self.image_palm = self.make_image('middle.png')

        # Surfaces
        self.background_cave = self.make_image('background_cave.png')
        self.land_up1 = self.make_image('surfaces\\land_up1.png')
        self.land_up0 = self.make_image('surfaces\\land_up0.png')
        self.land_up1 = self.make_image('surfaces\\land_up1.png')
        self.land_up2 = self.make_image('surfaces\\land_up2.png')
        self.land_middle0 = self.make_image('surfaces\\land_middle0.png')
        self.land_middle1 = self.make_image('surfaces\\land_middle1.png')
        self.land_middle2 = self.make_image('surfaces\\land_middle2.png')
        self.land_down0 = self.make_image('surfaces\\land_down0.png')
        self.land_down1 = self.make_image('surfaces\\land_down1.png')
        self.land_down2 = self.make_image('surfaces\\land_down2.png')
        self.wood_up0 = self.make_image('surfaces\\wood_up0.png')
        self.wood_up1 = self.make_image('surfaces\\wood_up1.png')
        self.wood_up2 = self.make_image('surfaces\\wood_up2.png')
        self.wood_middle0 = self.make_image('surfaces\\wood_middle0.png')
        self.wood_middle1 = self.make_image('surfaces\\wood_middle1.png')
        self.wood_middle2 = self.make_image('surfaces\\wood_middle2.png')
        self.wood_down0 = self.make_image('surfaces\\wood_down0.png')
        self.wood_down1 = self.make_image('surfaces\\wood_down1.png')
        self.wood_down2 = self.make_image('surfaces\\wood_down2.png')
        
        

        # Objects
        self.branch_left = self.make_image('objects\\branch_left.png')
        self.branch_right = self.make_image('objects\\branch_right.png')
        self.cut_tree = self.make_image('objects\\cut_tree.png')
        self.fallen_tree = self.make_image('objects\\fallen_tree.png')
        self.grass0 = self.make_image('objects\\grass0.png')
        self.grass1 = self.make_image('objects\\grass1.png')
        self.stairs = self.make_image('objects\\stairs.png')

        # Cave
        self.column_left = self.make_image('cave\\column_left.png')
        self.column_right = self.make_image('cave\\column_right.png')
        self.column_down = self.make_image('cave\\column_down.png')
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
        self.background_cave_unit = self.make_image('cave\\background_cave_unit.png')

        # Props
        self.bones = self.make_image('props\\bones.png')
        self.bones2 = self.make_image('props\\bones2.png')
        self.box = self.make_image('props\\box.png')
        self.bush = self.make_image('props\\bush.png')
        self.death_poster = self.make_image('props\\death_poster.png')
        self.door = self.make_image('props\\door.png')
        self.house = self.make_image('props\\house.png')
        self.lever_off = self.make_image('props\\lever_off.png')
        self.lever_on = self.make_image('props\\lever_on.png')
        self.mushroom = self.make_image('props\\mushroom.png')
        self.rock = self.make_image('props\\rock.png')
        self.shadow_box = self.make_image('props\\shadow_box.png')
        self.shadow_box_demon = self.make_image('props\\shadow_box_demon.png')
        self.shadow_box_long = self.make_image('props\\shadow_box_long.png')
        self.skulls = self.make_image('props\\skulls.png')
        self.small_box = self.make_image('props\\small_box.png')
        self.tree = self.make_image('props\\tree.png')
        self.tribal_box = self.make_image('props\\tribal_box.png')
        self.tribal_box_small = self.make_image('props\\tribal_box_small.png')



        self.land_up = [self.land_up0, self.land_up1, self.land_up2]
        self.cave_edges_up = [self.wood_up0, self.wood_up1, self.wood_up2]



    def make_image(self, root, increase=1.3):

        path = Paths(f'resources\\Sunny-land-assets-files\\PNG\\environment\\layers\\{root}').__str__()
        image = pygame.image.load(path).convert_alpha()
        increased_image = self.increase(image, increase)
        return increased_image
    


    def increase(self, image, increase):
        '''Incrementamos el tamaño de la imagen en relación a su proporción original'''

        image_width = image.get_width() * increase
        image_height = image.get_height() * increase

        image_size = (image_width, image_height)
        image = pygame.transform.scale(image, image_size)
        return image


  
    