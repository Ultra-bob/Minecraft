from random import randrange


class Player:

    name = "Player"
    cards = []
    discard = []
    active = None
    opponent = None
    game = None

    def add_card(self, card):
        print(self.cards)
        card.owner = self
        self.cards.append(card)

    def choose_card(self, return_card=True):
        print(f"{self.name}'s Cards:")
        self.cards = list(filter(None, self.cards))
        for num, card in enumerate(self.cards, 1):
            print(f"{num}: {card.name}")
        card = int(input("Choose a card (use numbers) "))
        act = self.active
        self.active = self.cards[card - 1]
        self.cards.remove(self.active)
        if return_card:
            self.cards.append(act)

        print(f"{self.active.name} is now your active card")

    def choose_move(self):
        if self.active.health <= 0:
            return
        move = int(input("Choose a move (1/2): "))
        if move == 1:
            self.active.primary(self.opponent.active)
        elif move == 2:
            self.active.secondary()

    def card_dies(self, card):
        self.game.discard.append(self.active)
        self.choose_card(False)

    def update_cards(self):
      for card in self.cards:
        card.owner = self


class AI(Player):

    algorithm = None

    def __init__(self, rating_algorithm, cards):
        super().__init__(cards)
        self.algorithm = rating_algorithm

    def choose_card(self, card=-1, random=False, return_card=True):
        act = self.active
        self.active = self.cards[card if not random else randrange(len(self.cards))]
        self.cards.remove(self.active)
        if return_card:
            self.cards.append(act)
        print(f"{self.name} has selected their {self.active.name}")

    def choose_move(self):
        if self.active.health <= 0:  # this is disgusting
            self.active.on_turn()
            return
        pri = self.active.primary_stats
        sec = self.active.secondary_stats
        if self.algorithm(pri, sec, self.active, self.opponent.active):
            self.active.primary(self.opponent.active)
        else:
            self.active.secondary(self.opponent.active)

    def card_dies(self, card):
        self.game.discard.append(self.active)
        self.choose_card(random=True, return_card=False)
