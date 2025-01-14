import pygame
from environment_frames import EnvironmentFrames



class Coordinates(EnvironmentFrames):

    def __init__(self, ms_game) -> None:
        super().__init__(ms_game)

        self.flag_cave = False



    def level1(self):

        self.flag_cave = True

        self.initial_coordinates_soldier = (1100, 400)
        self.initial_coordinates_enemies = ((650, 500), (700, 100))

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
            (self.land_middle1, 60, 0, 280),
            (self.land_down1, 60, 0, 300),
            (self.house, 1, 100, 120),
            (self.rock, 1, 600, 240),
            (self.mushroom, 1, 260, 247),
            (self.mushroom, 1, 1100, 247),
            (self.mushroom, 1, 470, 247),
            (self.bush, 1, 800, 225),
            (self.grass1, 1, 100, 240),
            (self.grass1, 1, 300, 240),
            (self.grass0, 1, 340, 240),
            (self.grass1, 1, 500, 240),
            (self.grass0, 1, 900, 240),
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
            (self.land_up2, 60, 0, 260),
            (self.land_middle1, 60, 0, 280),
            (self.land_down1, 60, 0, 300)
            ]
        
  
        stairs = [
            (self.stairs, 10, 260, 1000, 'y')
            ]

        level = {
            'background' : background,
            'platform1' : platform1,
            'platform2' : platform2,
            'platform3' : platform3,
            'platform4' : platform4,
            'platform5' : platform5,
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
            (self.land_down1, 4, 80, 270)
        ]

        # Segunda fila de plataformas  
        platform6 = [
            (self.land_up2, 9, 280, 420),
        ]

        platform7 = [
            (self.land_up2, 9, 520, 420),
        ]

        platform8 = [
            (self.land_up2, 9, 760, 420),
        ]

        # Tercera fila de plataformas  
        platform9 = [
            (self.land_up2, 9, 400, 650),
        ]

        platform10 = [
            (self.land_up2, 9, 640, 650),
        ]





        level = {
            'background' : background,
            'platform1' : platform1,
            'platform2' : platform2,
            'platform3' : platform3,
            'platform4' : platform4,
            'platform5' : platform5,
            'platform6' : platform6,
            'platform7' : platform7,
            'platform8' : platform8,
            'platform9' : platform9,
            'platform10' : platform10
            }
        return level
    



    # def level3(self):

    #     platform1 = [
    #         (self.land_up[2], 9, 0, 600),
    #         (self.land_middle[1], 9, 0, 620),
    #         (self.land_middle[1], 9, 0, 640),
    #         (self.land_middle[1], 9, 0, 660),
    #         (self.land_middle[1], 9, 0, 680),
    #         (self.land_middle[1], 9, 0, 700),
    #         (self.land_middle[1], 9, 0, 720),
    #         (self.land_middle[1], 9, 0, 740),
    #         (self.land_middle[1], 9, 0, 760),
    #         (self.land_middle[1], 9, 0, 780),
    #         (self.land_middle[1], 9, 0, 800)

    #         # (self.land_middle[1], 9, 620, 40, 'y'),
    #         # (self.land_middle[1], 9, 620, 60, 'y'),
    #         # (self.land_middle[1], 9, 620, 80, 'y'),
    #         # (self.land_middle[1], 9, 620, 100, 'y'),
    #         # (self.land_middle[1], 9, 620, 120, 'y'),
    #         # (self.land_middle[1], 9, 620, 140, 'y'),
    #         # (self.land_middle[2], 9, 620, 160, 'y'),

    #     ]
        

    #     platform2 = [
    #         (self.land_up[2], 1, 400, 600)
    #     ]

    #     platform3 = [
    #         (self.land_up[2], 6, 700, 600), 
    #         (self.land_up[2], 6, 700, 620),
    #         (self.land_up[2], 6, 700, 640),
    #         (self.land_up[2], 6, 700, 660),
    #         (self.land_up[2], 6, 700, 680),
    #         (self.land_up[2], 6, 700, 700)
    #     ]

    #     platform4 = [
    #         (self.land_up[2], 6, 900, 600), 
    #         (self.land_up[2], 6, 900, 620),
    #         (self.land_up[2], 6, 900, 640),
    #         (self.land_up[2], 6, 900, 660),
    #         (self.land_up[2], 6, 900, 680),
    #         (self.land_up[2], 6, 900, 700)
    #     ]

    #     level = [platform1, platform2, platform3, platform4]

    #     return level






    # self.repeat(self.cave_edges_up[0], 44, 320, 350)
    # self.repeat(self.cave_edges_middle[0], 44, 320, 370)
    # self.repeat(self.cave_edges_down[0], 44, 320, 390)
    

    # self.screen.blit(self.stone_grass[3], (160, 270))
    # self.screen.blit(self.stone_grass[1], (330, 250))
    # self.screen.blit(self.stone_grass[2], (360, 250))
    # self.screen.blit(self.stone_grass[3], (390, 250))
    # self.screen.blit(self.stone_grass[0], (160, 270))


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