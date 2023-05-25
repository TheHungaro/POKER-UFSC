import pygame
from pygame.locals import *
from card import Card
from deck import Deck
from pokertable import PokerTable
from pygame.locals import Rect

pygame.init()
WIDTH, HEIGHT = 1400, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Poker Table")

table_image = pygame.image.load("table.png")
card_back = pygame.image.load("cards/card_back.png")
card_width = 100
card_height = 150

table_rect = pygame.Rect((0, 0), (table_image.get_width(), table_image.get_height()))
table_rect.center = (WIDTH // 2, HEIGHT // 2)

table = PokerTable(WIDTH, HEIGHT, card_width, card_height, card_back, window, table_image, table_rect)




main_pack_x = (WIDTH - card_width) // 2
main_pack_y = (HEIGHT - card_height) // 2

deck = Deck(card_width, card_height)
deck.shuffle()

for card in deck.cards:
    table.add_card(card)

clock = pygame.time.Clock()

while True:
    clock.tick(60)

    table.handle_events()
    table.update()
    table.draw()