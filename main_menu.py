import pygame.font


class Menu():
    def __init__(self, ms_game):
        self.button_texts = ["Start", "Instructions", "Exit"]
        self.ms_game = ms_game
        self.screen = ms_game.screen
        self.screen_rect = self.screen.get_rect()
        self.desplace_button_position = 0
        self.buttons = []

        self.title_image = pygame.image.load("resources/fonts/title.png").convert_alpha()


        self.create_buttons()

    def title(self):
        title_image = self.title_image.copy()
        title_image_rect = title_image.get_rect()
        title_image_rect.center = self.screen_rect.center
        title_image_rect.y -= 200
        self.screen.blit(title_image, title_image_rect)


    def title_level(self, level):
        title_image = level.copy()  
        title_image_rect = title_image.get_rect()
        title_image_rect.center = self.screen_rect.center
        title_image_rect.y += 50
        self.screen.blit(title_image, title_image_rect)


    def create_buttons(self):
        for text in self.button_texts:
            button = Button(self.ms_game, text)
            button.rect.y = button.rect.y - self.desplace_button_position
            button.msg_image_rect.y = button.rect.y + 10
            self.buttons.append(button)
            self.desplace_button_position -= 100

            
    def create_menu(self):
        for button in self.buttons:
            button.draw_button()
            



class Button():

    def __init__(self, ms_game, msg):
        '''Inicializa los atributos del botón'''
        self.screen = ms_game.screen
        self.screen_rect = self.screen.get_rect()

        # EConfigura las dimensiones y propiedades del botón
        self.width, self.height = 200, 80
        self.text_color = (255, 255, 58)
        self.font = pygame.font.Font("resources/fonts/Retro Gaming.ttf", 48)

        # Creamos el objeto rect botón y lo centramos 
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Preparamos el mensaje del botón
        self._prep_msg(msg)


    def _prep_msg(self, msg):
        '''Convierte el texto en una imagen renderizada y lo centra en el centro'''
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center



    def draw_button(self):
        '''Dibuja un botón en blanco y luego el mensaje'''
        self.screen.blit(self.msg_image, self.msg_image_rect)

        