class Player:

    name = "Player"
    cards = []
    active = None
    opponent = None

    def __init__(self, cards):
        self.cards = cards
        for card in cards:
            card.owner = self

    def choose_card(self):
        print("Cards:")
        for num, card in enumerate(self.cards):
            print(f"{num}: {card.name}")
        card = int(input("Choose a card (use numbers) "))
        act = self.active
        self.active = self.cards[card]
        self.cards.remove(self.active)
        self.cards.append(act)

        print(f"{self.active.name} is now your active card")

class AI(Player):

    algorithm = None

    def __init__(self, rating_algorithm, cards):
        super().__init__(cards)
        self.algorithm = rating_algorithm

    def choose_card(self, card):
        act = self.active
        self.active = self.cards[card]
        self.cards.remove(self.active)
        self.cards.append(act)
    
    def choose_move(self):
        pri = self.active.primary_stats
        sec = self.active.secondary_stats
        if self.algorithm(pri, sec, self.active, self.opponent.active):
            self.active.primary(self.opponent.active)
        else:
            self.active.secondary()
