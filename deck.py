import random
from card import Card

class Deck:
    def __init__(self, card_width, card_height):
        self.cards = []
        for suit in ["hearts", "diamonds", "clubs", "spades"]:
            for rank in range(1, 14):
                image = f"cards/{suit}_{rank}.png"
                card = Card(image, (0, 0))
                card.rect.width = card_width
                card.rect.height = card_height
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self, position):
        if len(self.cards) > 0:
            card = self.cards.pop()
            card.rect.topleft = position
            return card
        else:
            return None