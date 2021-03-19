from utils import import_card_data


class Card:

    health = 0
    max_health = 0
    effects = []
    name = "base"
    owner = None
    dead = False

    boosts = {
        "healing": 1,
        "attack": 1,
        "resistance": 1,
    }

    # primary move
    primary_stats = {
        "damage": 0,
        "heal": 0,
        "effects_other": [],
        "effects_self": [],
    }

    # secondary move
    secondary_stats = {
        "damage": 0,
        "heal": 0,
        "effects_other": [],
        "effects_self": [],
    }

    def __init__(self, data):
        name, max_health, primary, secondary = import_card_data(data)
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.primary_stats = primary
        self.secondary_stats = secondary

    def check_death(self):
      if self.health <= 0 or self.dead:
        print(f"{self.owner.name}'s {self.name} died!")
        self.owner.card_dies(self)

    def die(self):
      self.dead = True
  
        

    def heal(self, amount):
        amount *= self.boosts["healing"]
        heal = min(self.health + amount, self.max_health)
        if amount != 0:
            print(f"{amount} HP")
        self.health = heal

    def add_effect(self, effect):
        if type(effect) is list:
            for eff in effect:
                self.add_effect(eff)
        else:
            self.effects.append(effect)

    def take_damage(self, amount, dmg_type):
        if dmg_type == "true":
            self.health -= amount
        elif dmg_type == "attack":
            damage = round(amount * (1 / self.boosts["resistance"]))
            print(f"{damage} damage!")
            self.health -= damage


class Effect:
    name = "base"
    duration = 0
    first_turn = False

    def __init__(self, duration):
        self.first_turn = True
        self.duration = duration

    def on_turn(self, card):
        if self.duration == 0:
            return
        elif self.duration == 1:
            self.on_last_turn(card)
        if self.first_turn:
            self.on_first_turn(card)
            # should this return and end or continue running?
        self.first_turn = False

    def on_last_turn(self, card):
        pass

    def on_first_turn(self, card):
        pass
