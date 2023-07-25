import pygame.font


class BgButton:
    """Creates and manages the button to choose the
     background image with user input."""

    def __init__(self, ai_game, bg_msg):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 550, 50
        self.button_color = (0, 0, 255)
        self.text_color = (255, 255, 255)
        # The None argument tells Pygame to use the default font,
        # and 48 specifies the size of the text.
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midtop = self.screen_rect.midtop

        # The button message needs to be prepped only once.
        self._prep_bg_msg(bg_msg)

    def _prep_bg_msg(self, bg_msg):
        """Turns msg into a rendered image and center text on the button"""
        # The call to font.render() turns the text stored in
        # msg into an image, which we then store in self.msg_image
        self.msg_image = self.font.render(bg_msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_bg_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
