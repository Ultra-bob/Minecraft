from card import Card
from player import Player, AI
from card_stats import zombie, creeper
from rating import rate_move, alternate_rate

ai = AI(rate_move, [Card(zombie)])
p1 = Player([Card(zombie)])

ai.choose_card(0)
p1.choose_card()

ai.opponent = p1
p1.opponent = ai

p1.name = 'P1'
ai.name = 'CPU1'

while True:
    ai.choose_move()

    if p1.active.health < 0:
        print("CPU1 won")
        break

    p1.choose_move()

    if ai.active.health < 0:
        print("P1 won")
        break
