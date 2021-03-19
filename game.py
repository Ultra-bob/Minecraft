from random import shuffle
from player import Player, AI
from card import Card
from card_stats import zombie
from utils import print_card

class Game():
  player1 = None
  player2 = None
  discard = []

  def __init__(self, deck,cpu=False):
    deck.shuffle()
    self.player1 = Player()
    self.player2 = Player()


    # set names
    self.player1.name = 'P1'
    if self.player2 is AI:
      self.player2.name = 'CPU'
    else:
      self.player2.name = 'P2'

    # set opponents and game

    self.player1.opponent = self.player2
    self.player2.opponent = self.player1
    self.player1.game = self
    self.player2.game = self
    
    self.player2.add_card(Card(zombie))
    self.player1.add_card(Card(zombie))
    self.player2.add_card(Card(zombie))
    self.player1.add_card(Card(zombie))

    self.player1.update_cards()
    self.player2.update_cards()

    # choose active
    self.player1.choose_card()
    self.player2.choose_card()

  def turn(self):
    print_card(self.player1.active)

    # player1 moves
    self.player1.choose_move()

    print_card(self.player2.active)

    # player2 moves
    self.player2.choose_move()

    self.player1.active.check_death()
    self.player2.active.check_death()
    
    
    

class Deck():
  cards = []

  def shuffle(self):
    shuffle(self.cards)