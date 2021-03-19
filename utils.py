def import_card_data(card):
    name = card["name"]
    max_hp = card["max_health"]
    primary_stats = card["primary_stats"]
    secondary_stats = card["secondary_stats"]

    return name, max_hp, primary_stats, secondary_stats


def print_card(card):
    if card is None: return
    topRow = f"{card.name}{card.health:>4}/{card.max_health}HP"
    card = f"""
{card.owner.name}'s
 ┌──────────────────┐
 │ {topRow:<17}│
 │                  │
 │                  │
 │                  │
 │                  │
 │ 1: {card.primary_stats['desc']:<14}│
 │ 2: {card.secondary_stats['desc']:<14}│
 │                  │
 └──────────────────┘"""

    print(card)
