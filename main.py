from card import Card
from player import Player, AI
from card_stats import zombie, creeper
from rating import rate_move, alternate_rate

ai = AI(rate_move, [Card(zombie)])
ai2 = AI(alternate_rate, [Card(zombie)])

ai.choose_card(0)
ai2.choose_card(0)

ai.opponent = ai2
ai2.opponent = ai

ai2.name = 'CPU2'
ai.name = 'CPU1'

while True:
    ai.choose_move()

    if ai2.active.health < 0:
        print("CPU1 won")
        break

    ai2.choose_move()

    if ai.active.health < 0:
        print("CPU2 won")
        break
