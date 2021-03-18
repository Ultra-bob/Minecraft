def rate_move(move1, move2, card, other):
  more_damage = move1 if move1['damage'] > move2['damage'] else move2
  more_health = move1 if move1['heal'] > move2['heal'] else move2

  other_turns = other.health / more_damage['damage']
  card_turns = card.health / other.primary_stats['damage']

  if card_turns > other_turns:
    return True
  elif card.health + more_health['heal'] > other.health:
    return False
  else:
    return True
  

def alternate_rate(move1, move2, card, other):
  pri_rating = 0
  pri_rating += move1['heal'] * card.max_health / card.health if card.health != 0 else 0.01
  pri_rating += move1['damage'] * other.max_health / other.health if other.health != 0 else 0.01

  sec_rating = 0
  sec_rating += move2['heal'] * card.max_health / card.health if card.health != 0 else 0.01
  sec_rating += move2['damage'] * other.max_health / other.health if other.health != 0 else 0.01
  return pri_rating > sec_rating

def nonzero(num):
  if num == 0:
    return 0.001
  else:
    return num