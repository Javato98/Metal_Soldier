import pygame
from environment_frames import EnvironmentFrames



class Coordinates(EnvironmentFrames):

    def __init__(self, ms_game) -> None:
        super().__init__(ms_game)

        self.flag_cave = False



    def level1(self):

        self.flag_cave = True

        self.initial_coordinates_soldier = (40, 540)
        self.initial_coordinates_enemies = ((650, 500), (700, 100), (1100, 400))

        background = [
						
            # Platform 1
            (self.land_middle1, 9, 0, 620),
            (self.land_middle1, 9, 0, 640),
            (self.land_middle1, 9, 0, 660),
            (self.land_middle1, 9, 0, 680),
            (self.land_middle1, 9, 0, 700),
            (self.land_middle1, 9, 0, 720),
            (self.land_middle1, 9, 0, 740),
            (self.land_middle1, 9, 0, 760),
            (self.land_middle1, 9, 0, 780),
            (self.land_middle1, 9, 0, 800), 
            (self.wood_middle2, 9, 620, 180, 'y'),
            
            # Platform 2
            (self.land_middle1, 48, 260, 620),
            (self.land_middle1, 48, 260, 640),
            (self.land_middle1, 48, 260, 660),
            (self.land_middle1, 48, 260, 680),
            (self.land_middle1, 48, 260, 700),
            (self.land_middle1, 48, 260, 720),
            (self.land_middle1, 48, 260, 740),
            (self.land_middle1, 48, 260, 760),
            (self.land_middle1, 48, 260, 780),
            (self.wood_middle0, 9, 620, 260, 'y'),
            (self.wood_up0, 1, 600, 260, 'y'),
            
            # Platform 3
            (self.wood_up0, 1, 560, 560, 'y'),
            (self.wood_middle0, 1, 580, 560, 'y'),
            (self.land_middle1, 32, 560, 600),
            (self.land_middle1, 32, 580, 580),
            (self.wood_middle0, 1, 600, 560, 'y'),
            
            # Platform 4
            (self.wood_up0, 1, 520, 800, 'y'),
            (self.land_middle1, 20, 800, 540),
            (self.wood_middle0, 1, 540, 800, 'y'),
            (self.land_middle1, 20, 800, 560),
            (self.wood_middle0, 1, 800, 560),

            # Platform 5            
            (self.house, 1, 100, 120),
            (self.rock, 1, 600, 240),
            (self.mushroom, 1, 260, 247),
            (self.mushroom, 1, 470, 247),
            (self.bush, 1, 800, 225),
            (self.grass1, 1, 100, 240),
            (self.grass1, 1, 300, 240),
            (self.grass0, 1, 340, 240),
            (self.grass1, 1, 500, 240),
            (self.grass0, 1, 140, 240),
            (self.grass1, 1, 200, 240),
            (self.grass1, 1, 220, 240),
            (self.grass0, 1, 700, 240),


            # Background
                # Columns
            (self.ruins4, 11, 320, 100, 'y'),
            (self.ivy, 1, 80, 540),
            (self.ruins4, 11, 320, 400, 'y'),
            (self.ivy, 1, 380, 540),
            (self.ruins4, 11, 320, 900, 'y'),
            (self.ivy, 1, 880, 460),
            (self.ruins4, 11, 320, 1100, 'y'),
            (self.ivy, 1, 1080, 460),

                # Boxes
            (self.shadow_box_demon, 1, 210, 380),
            (self.shadow_box, 1, 170, 490),
            (self.shadow_box, 1, 270, 490),
            (self.shadow_box_long, 1, 540, 400),
            (self.shadow_box_long, 1, 740, 400),
            (self.torch, 1, 550, 370),
            (self.torch, 1, 750, 370),
            (self.ruins, 1, 650, 500),
            (self.liana2, 1, 350, 300),
            (self.liana1, 1, 650, 300),
            (self.liana2, 1, 870, 300),
            (self.death_poster, 1, 160, 575),

            (self.stone1, 1, 50, 740),
            (self.stone1, 1, 140, 660),
            (self.stone0, 1, 140, 600),
            (self.stone0, 1, 160, 760),
            (self.stone0, 1, 20, 620),
            

            (self.stone0, 1, 640, 660),
            (self.stone0, 1, 540, 740),
            (self.stone0, 1, 460, 640),
            (self.stone1, 1, 500, 780),

            (self.stone0, 1, 1100, 780),
            (self.stone0, 1, 900, 680),
            (self.stone1, 1, 1140, 640),
            (self.stone1, 1, 860, 740),
            (self.stone1, 1, 980, 740),
            (self.stone1, 1, 980, 560),

	    ]

        platform1 = [(self.wood_up1, 10, 0, 600)]
                    
        platform2 = [(self.wood_up1, 15, 260, 600)]

        platform3 = [
            (self.wood_up1, 12, 560, 560),
            ]
            
        platform4 = [
            (self.wood_up1, 20, 800, 520),
            ]
            
        platform5 = [ 
            (self.land_up2, 45, 0, 260),
            (self.land_middle1, 45, 0, 280),
            (self.land_down1, 45, 0, 300),
            ]

        platform6 = [ 
            (self.land_up2, 15, 900, 300),
            ]
        
  
        stairs = [
            (self.stairs, 8, 300, 1000, 'y')
            ]

        level = {
            'background' : background,
            'platform1' : platform1,
            'platform2' : platform2,
            'platform3' : platform3,
            'platform4' : platform4,
            'platform5' : platform5,
            'platform6' : platform6,
            'stairs' : stairs
            }

        return level






    
    def level2(self):

        self.initial_coordinates_soldier = (80, 100)
        self.initial_coordinates_enemies = ((450, 100), (940, 100),(340, 360), (820, 360), (700, 500), (450, 500))

        background = [
            
            #Platform 1
            (self.land_middle1, 9, 160, 250),
            (self.land_down1, 9, 160, 270),
            (self.land_up0, 1, 160, 230),
            (self.land_middle0, 1, 160, 250),
            (self.land_down0, 1, 160, 270),
            (self.land_up2, 1, 320, 230),
            (self.land_middle2, 1, 320, 250),
            (self.land_down2, 1, 320, 270),
            (self.bush, 1, 200, 195),
            (self.branch_right, 1, 340, 250),
            
            

            #Platform 2
            (self.land_middle1, 9, 400, 250),
            (self.land_down1, 9, 400, 270),
            (self.land_up0, 1, 400, 230),
            (self.land_middle0, 1, 400, 250),
            (self.land_down0, 1, 400, 270),
            (self.land_up2, 1, 560, 230),
            (self.land_middle2, 1, 560, 250),
            (self.land_down2, 1, 560, 270),
            (self.grass0, 1, 440, 210),
            (self.grass0, 1, 480, 210),

            #Platform 3
            (self.land_middle1, 9, 640, 250),
            (self.land_down1, 9, 640, 270),
            (self.land_up0, 1, 640, 230),
            (self.land_middle0, 1, 640, 250),
            (self.land_down0, 1, 640, 270),
            (self.land_up2, 1, 800, 230),
            (self.land_middle2, 1, 800, 250),
            (self.land_down2, 1, 800, 270),
            (self.mushroom, 1, 640, 217),
            (self.grass0, 1, 720, 210),
            (self.grass0, 1, 760, 210),
            (self.grass0, 1, 780, 210),
            (self.branch_left, 1, 620, 250),


            #Platform 4
            (self.land_middle1, 9, 880, 250),
            (self.land_down1, 9, 880, 270),
            (self.land_up0, 1, 880, 230),
            (self.land_middle0, 1,880, 250),
            (self.land_down0, 1, 880, 270),
            (self.land_up2, 1, 1040, 230),
            (self.land_middle2, 1, 1040, 250),
            (self.land_down2, 1, 1040, 270),
            (self.tree, 1, 950, 110),
            (self.rock, 1, 900, 211),
            (self.branch_right, 1, 1060, 250),


            #Platform 5
            (self.land_middle1, 9, 280, 440),
            (self.land_down1, 9, 280, 460),
            (self.land_up0, 1, 280, 420),
            (self.land_middle0, 1, 280, 440),
            (self.land_down0, 1, 280, 460),
            (self.land_up2, 1, 440, 420),
            (self.land_middle2, 1, 440, 440),
            (self.land_down2, 1, 440, 460),
            (self.mushroom, 1, 320, 407),
            (self.grass1, 1, 380, 400),
            (self.grass1, 1, 400, 400),

            #Platform 6
            (self.land_middle1, 9, 520, 440),
            (self.land_down1, 9, 520, 460),
            (self.land_up0, 1, 520, 420),
            (self.land_middle0, 1, 520, 440),
            (self.land_down0, 1, 520, 460),
            (self.land_up2, 1, 680, 420),
            (self.land_middle2, 1, 680, 440),
            (self.land_down2, 1, 680, 460),
            (self.grass0, 1, 540, 400),
            (self.grass1, 1, 620, 400),
            (self.grass1, 1, 640, 400),
            (self.branch_right, 1, 700, 440),
            
            
            #Platform 7 Part 2
            (self.column_left, 1, 900, 380),
            (self.column_right, 1, 940, 380),
            (self.column_down, 1, 885, 442),


            


            #Platform 7
            (self.land_middle1, 9, 760, 440),
            (self.land_down1, 9, 760, 460),
            (self.land_up0, 1, 760, 420),
            (self.land_middle0, 1, 760, 440),
            (self.land_down0, 1, 760, 460),
            (self.land_up2, 1, 920, 420),
            (self.land_middle2, 1, 920, 440),
            (self.land_down2, 1, 920, 460),
            (self.rock, 1, 800, 400),
            (self.grass1, 1, 880, 400),
            

            

            #Platform 8
            (self.land_middle1, 9, 400, 670),
            (self.land_down1, 9, 400, 690),
            (self.land_up0, 1, 400, 650),
            (self.land_middle0, 1, 400, 670),
            (self.land_down0, 1, 400, 690),
            (self.land_up2, 1, 560, 650),
            (self.land_middle2, 1, 560, 670),
            (self.land_down2, 1, 560, 690),
            (self.bush, 1, 430, 615),
            (self.grass0, 1, 480, 630),
            (self.branch_left, 1, 380, 670),
            (self.land_up2, 2, 880, 420),


            #Platform 9
            (self.land_middle1, 9, 640, 670),
            (self.land_down1, 9, 640, 690),
            (self.land_up0, 1, 640, 650),
            (self.land_middle0, 1, 640, 670),
            (self.land_down0, 1, 640, 690),
            (self.land_up2, 1, 800, 650),
            (self.land_middle2, 1, 800, 670),
            (self.land_down2, 1, 800, 690),
            (self.mushroom, 1, 760, 637),
            (self.grass0, 1, 660, 630),
            (self.grass0, 1, 680, 630),

        ]


        platform1 = [
            (self.land_up2, 9, 160, 230)
        ]
        
        platform2 = [
            (self.land_up2, 9, 400, 230),
        ]

        platform3 = [
            (self.land_up2, 9, 640, 230),
        ]

        platform4 = [
            (self.land_up2, 9, 880, 230),
        ]

        platform5 = [
            (self.edge2, 3, 100, 270),
        ]

        platform5_1 = [
            (self.edge, 1, 80, 270),
        ]


        # Segunda fila de plataformas  
        platform6 = [
            (self.land_up2, 9, 280, 420),
        ]

        platform7 = [
            (self.land_up2, 9, 520, 420),
        ]

        platform7_2 = [
            (self.edge2, 5, 900, 380),
        ]

        plafotm7_3 = [
            (self.edge, 1, 880, 380),
        ]

        plafotm7_4 = [
            (self.edge3, 1, 1000, 380),
        ]

        platform8 = [
            (self.land_up2, 6, 760, 420),
        ]

        # Tercera fila de plataformas  
        platform9 = [
            (self.land_up2, 9, 400, 650),
        ]

        platform10 = [
            (self.land_up2, 9, 640, 650),
        ]

        platform11 = [
            (self.edge2, 4, 320, 690),
        ]

        plafotm11_1 = [
            (self.edge, 1, 300, 690),
        ]






        level = {
            'background' : background,
            'platform1' : platform1,
            'platform2' : platform2,
            'platform3' : platform3,
            'platform4' : platform4,
            'platform5' : platform5,
            'platform5_1' : platform5_1,
            'platform6' : platform6,
            'platform7' : platform7,
            'platform7_2' : platform7_2,
            'plafotm7_3' : plafotm7_3,
            'plafotm7_4' : plafotm7_4,
            'platform8' : platform8,
            'platform9' : platform9,
            'platform10' : platform10,
            'platform11' : platform11,
            'plafotm11_1' : plafotm11_1
            }
        return level
    



    def level3(self):

        self.initial_coordinates_soldier = (80, 400)
        self.initial_coordinates_enemies = ()

        background = [

            # background
            (self.background_cave2, 1, -102, 305),

            # Platform 1
            (self.wood_middle2, 2, 520, 160,'y'),
            (self.wood_middle2, 12, 560, 220,'y'),
            (self.land_middle1, 14, 520, 0,'y'),
            (self.land_middle1, 14, 520, 20,'y'),
            (self.land_middle1, 14, 520, 40,'y'),
            (self.land_middle1, 14, 520, 60,'y'),
            (self.land_middle1, 14, 520, 80,'y'),
            (self.land_middle1, 14, 520, 100,'y'),
            (self.land_middle1, 14, 520, 120,'y'),
            (self.land_middle1, 14, 520, 140,'y'),
            (self.land_middle1, 12, 560, 160,'y'),
            (self.land_middle1, 12, 560, 180,'y'),
            (self.land_middle1, 12, 560, 200,'y'),
            (self.border_cave_right, 25, 320, 320, 'y'),

            #platform2
            (self.land_middle0, 16, 480, 400, 'y'),
            (self.land_middle2, 12, 580, 700, 'y'),
            (self.land_middle1, 16, 480, 420,'y'),
            (self.land_middle1, 16, 480, 440,'y'),
            (self.land_middle1, 16, 480, 460,'y'),
            (self.land_middle1, 16, 480, 480,'y'),
            (self.land_middle1, 16, 480, 500,'y'),
            (self.land_middle1, 16, 480, 520,'y'),
            (self.land_middle1, 16, 480, 540,'y'),
            (self.land_middle1, 16, 480, 560,'y'),

            (self.land_middle1, 12, 580, 580,'y'),
            (self.land_middle1, 12, 560, 600,'y'),
            (self.land_middle1, 12, 560, 620,'y'),
            (self.land_middle1, 12, 560, 640,'y'),
            (self.land_middle1, 12, 560, 660,'y'),
            (self.land_middle1, 12, 560, 680,'y'),

            #platform3
            (self.land_middle0, 12, 580, 780, 'y'),
            (self.land_middle0, 2, 540, 900, 'y'),
            (self.land_middle1, 12, 580, 800,'y'),
            (self.land_middle1, 12, 580, 820,'y'),
            (self.land_middle1, 12, 580, 840,'y'),
            (self.land_middle1, 12, 580, 860,'y'),
            (self.land_middle1, 12, 580, 880,'y'),
            (self.land_middle1, 12, 580, 900,'y'),
            (self.land_middle1, 14, 540, 920,'y'),
            (self.land_middle1, 14, 540, 940,'y'),
            (self.land_middle1, 14, 540, 960,'y'),
            (self.land_middle1, 14, 540, 980,'y'),
            (self.land_middle1, 14, 540, 1000,'y'),
            (self.land_middle1, 14, 540, 1020,'y'),
            (self.land_middle1, 14, 540, 1040,'y'),
            (self.land_middle1, 14, 540, 1060,'y'),
            (self.land_middle1, 14, 540, 1080,'y'),
            (self.land_middle1, 14, 540, 1100,'y'),
            (self.land_middle1, 14, 540, 1120,'y'),
            (self.land_middle1, 14, 540, 1160,'y'),
            (self.land_middle1, 14, 540, 1140,'y'),
            (self.land_middle1, 14, 540, 1180,'y'),


            # Air platforms
            (self.land_middle1, 10, 600, 320),
            (self.land_down1, 10, 600, 340),
            (self.land_middle0, 2, 320, 600, 'y'),
            (self.land_middle2, 2, 320, 780, 'y'),

            (self.land_middle1, 10, 860, 190),
            (self.land_down1, 10, 860, 210),
            (self.land_middle0, 2, 190, 860, 'y'),
            (self.land_middle2, 2, 190, 1040, 'y'),

            (self.land_middle1, 10, 460, 80),
            (self.land_down1, 10, 460, 100),
            (self.land_middle0, 2, 80, 460, 'y'),
            (self.land_middle2, 2, 80, 640, 'y'),

            # Environment
            (self.rock, 1, 200, 281),
            (self.rock, 1, 660, 541),
            (self.rock, 1, 1000, 151),
            (self.mushroom, 1, 160, 288),
            (self.mushroom, 1, 660, 288),
            (self.mushroom, 1, 500, 48),
            (self.bush, 1, 520, 30),
            (self.tree, 1, 1000, 400),
            (self.grass0, 6, 20, 280),
            (self.grass0, 4, 260, 280),
            (self.grass1, 6, 440, 440),
            (self.grass0, 4, 820, 540),
            (self.grass0, 13, 940, 500),
            (self.grass0, 5, 700, 280),
            (self.grass0, 6, 860, 150),
            (self.grass0, 5, 460, 60),

            (self.death_poster, 1, 120, 475),
            (self.bones, 2, 20, 486),
            (self.bones2, 1, 200, 530),
            (self.tribal_box, 1, 115, 370),
            (self.tribal_box_small, 1, 210, 380),
            (self.stone0, 1, 60, 560),
            (self.stone1, 1, 70, 600),
            (self.stone1, 1, 50, 740),
            (self.stone1, 1, 140, 660),
            (self.stone0, 1, 140, 600),
            (self.stone0, 1, 160, 760),
            (self.stone0, 1, 20, 620),
            
            (self.stone0, 1, 420, 500),
            (self.stone0, 1, 640, 660),
            (self.stone0, 1, 540, 740),
            (self.stone0, 1, 460, 640),
            (self.stone1, 1, 500, 780),
            (self.stone1, 1, 460, 540),
            (self.stone1, 1, 560, 580),

            (self.stone0, 1, 800, 620),
            (self.stone0, 1, 1100, 780),
            (self.stone0, 1, 900, 680),
            (self.stone1, 1, 1140, 640),
            (self.stone1, 1, 860, 740),
            (self.stone1, 1, 980, 740),
            (self.stone1, 1, 980, 560),



        ]



        platform1 = [
            (self.land_up1, 17, 0, 300)
        ]
        
        platform2 = [
            (self.wood_up1, 9, 0, 500)
        ]

        platform3 = [
            (self.wood_up1, 3, 180, 540)
        ]

        platform4 = [
            (self.land_up1, 10, 400, 460)
        ]

        platform4_2 = [
            (self.land_middle2, 5, 480, 580, 'y'),
        ]

        platform5 = [
            (self.land_up1, 6, 600, 560)
        ]

        platform6 = [
            (self.land_up1, 6, 780, 560)
        ]

        platform7 = [
            (self.land_up1, 15, 900, 520)
        ]

        platform8 = [
            (self.land_up1, 10, 600, 300)
        ]

        platform9 = [
            (self.land_up1, 10, 860, 170)
        ]

        platform10 = [
            (self.land_up1, 10, 460, 60)
        ]

        stairs = [
            (self.stairs, 7, 300, 40, 'y'),
        ]

        stairs2 = [
            (self.stairs, 14, 170, 920, 'y'),
        ]

        stairs3 = [
            (self.stairs, 9, 60, 620, 'y'),
        ]





        level = {
            'background' : background,
            'platform1' : platform1,
            'platform2' : platform2,
            'platform3' : platform3,
            'platform4' : platform4,
            'platform4_2' : platform4_2,
            'platform5' : platform5,
            'platform6' : platform6,
            'platform7' : platform7,
            'platform8' : platform8,
            'platform9' : platform9,
            'platform10' : platform10,
            'stairs' : stairs,
            'stairs2' : stairs2,
            'stairs3' : stairs3
        }

        return level





class Platform(pygame.sprite.Sprite):
    def __init__(self, rect):
        super().__init__()
        self.id = id
        self.image = pygame.Surface((rect.width, rect.height))
        self.rect = rect


class Stairs(pygame.sprite.Sprite):
    def __init__(self, rect):
        super().__init__()
        self.id = id
        self.image = pygame.Surface((rect.width, rect.height))
        self.rect = rect