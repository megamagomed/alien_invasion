import pygame


class Lifes:
    """A class to represrnt a single alien in the fleet."""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        # self.rect.x = self.screen_rect.width - 5 * self.rect.width
        self.rect.y = 5
        self.settings = ai_game.settings

    def draw_lifes(self, ships):
        for i in range(ships):
            self.rect.x = self.screen_rect.width - (2 + i) * self.rect.width
            self.screen.blit(self.image, self.rect)
