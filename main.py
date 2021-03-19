from card import Card
from game import Game, Deck
from card_stats import zombie, creeper

deck = Deck()

game = Game(deck)

while True:
  game.turn()
