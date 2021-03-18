def import_card_data(card):
  name = card['name']
  max_hp = card['max_health']
  primary_stats = card['primary_stats']
  secondary_stats = card['secondary_stats']

  return name, max_hp, primary_stats, secondary_stats