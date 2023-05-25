import pygame

class Card:
    def __init__(self, image, position, is_face_up=False):
        self.face_image = pygame.image.load(image)
        self.rect = self.face_image.get_rect()
        self.rect.topleft = position
        self.is_face_up = is_face_up

    def draw(self, window, card_width, card_height, card_back):
        if self.is_face_up:
            card_image = pygame.transform.scale(self.face_image, (card_width, card_height))
            window.blit(card_image, self.rect.topleft)
        else:
            card_image = pygame.transform.scale(card_back, (card_width, card_height))
            window.blit(card_image, self.rect.topleft)