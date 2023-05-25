import pygame
from pygame.locals import *
from card import Card
import sys

class PokerTable:
    def __init__(self, width, height, card_width, card_height, card_back, window, table_image, table_rect):
        self.width = width
        self.height = height
        self.card_width = card_width
        self.card_height = card_height
        self.card_back = card_back
        self.window = window
        self.table_image = table_image
        self.table_rect = table_rect
        self.cards = []
        self.selected_card = None
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0

    def add_card(self, card):
        card.rect.topleft = ((self.width - self.card_width) // 2, (self.height - self.card_height) // 2)
        self.cards.append(card)
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    for card in self.cards:
                        scaled_rect = pygame.Rect(card.rect.topleft, (self.card_width, self.card_height))
                        if scaled_rect.collidepoint(event.pos):
                            self.selected_card = card
                            self.dragging = True
                            self.offset_x = event.pos[0] - card.rect.left
                            self.offset_y = event.pos[1] - card.rect.top
                            break
                elif event.button == 3:  # Right mouse button
                    for card in self.cards:
                        scaled_rect = pygame.Rect(card.rect.topleft, (self.card_width, self.card_height))
                        if scaled_rect.collidepoint(event.pos):
                            card.is_face_up = not card.is_face_up
                            break

            if event.type == MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button
                    self.dragging = False

            if event.type == MOUSEMOTION:
                if self.dragging and self.selected_card is not None:
                    # Calculate the new position of the card
                    new_x = event.pos[0] - self.offset_x
                    new_y = event.pos[1] - self.offset_y

                    # Restrict the card's movement within the visible area of the window
                    new_x = max(new_x, 0)
                    new_x = min(new_x, self.width - self.card_width)
                    new_y = max(new_y, 0)
                    new_y = min(new_y, self.height - self.card_height)

                    # Update the card's position
                    self.selected_card.rect.topleft = (new_x, new_y)

    def update(self):
        pass

    def draw(self):
        self.window.fill((0, 128, 0))
        self.window.blit(self.table_image, self.table_rect.topleft)

            # Render text
        font = pygame.font.Font(None, 100)  # Choose the desired font and size
        text = font.render("Poker UFSC", True, (255, 255, 255))  # Set the text content and color
        text_rect = text.get_rect(center=(self.width // 2, self.height  // 2 - 150))  # Center the text on the screen

        self.window.blit(text, text_rect)

        for card in self.cards:
            card.draw(self.window, self.card_width, self.card_height, self.card_back)

    

        pygame.display.update()