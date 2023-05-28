import pygame


# Define Button class
class pygamePushButton:
    """
    Class represents pygame viable pushbuttons

    Attributes:
        rect (pygame.Rect)  : Object defining the position and size.
        backColor (tuple)   : The background color of the object in RGB format.
        text (str)          : The text currently displayed on the box.
        textColor (tuple)   : The color of the text in RGB format.

    Methods:
        draw()                  : Draw the button on the Pygame window.
        is_clicked(mouse_pos)   : Check if the button is clicked based on the mouse position.
    """
    def __init__(self, window, x: int, y: int, width: int, height: int, color: tuple, text: str, textColor: tuple):
        """
        Button class represents a clickable button in Pygame.

        Args:
            x (int): The x-coordinate of the top-left corner of the button.
            y (int): The y-coordinate of the top-left corner of the button.
            width (int): The width of the button.
            height (int): The height of the button.
            color (tuple): The color of the button in RGB format.
            text (str): The text to be displayed on the button.
            text_color (tuple): The color of the text in RGB format.
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.backColor = color
        self.text = text
        self.textColor = textColor
        self.window = window


    def draw(self):
        """
        Draw the button on the Pygame window.
        """
        pygame.draw.rect(self.window, self.backColor, self.rect)     # Draw the button rectangle
        font = pygame.font.Font(None, 32)                       # Set the font for the button text
        text = font.render(self.text, True, self.textColor)     # Render the button text
        text_rect = text.get_rect(center=self.rect.center)      # Position the text at the center of the button
        self.window.blit(text, text_rect)                            # Draw the text on the window


    def is_clicked(self, mouse_pos):
        """
        Check if the button is clicked based on the mouse position.

        Args:
            mouse_pos (tuple): The current position of the mouse.

        Returns:
            bool: True if the button is clicked, False otherwise.
        """
        return self.rect.collidepoint(mouse_pos)


