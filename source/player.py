class Player:
  def __init__(self,name,shards=100):
    self.name = name
    self.shards = shards
    self.hand = []
    self.hand_value = 0

  def add_shards(self,amount):
    self.shards += amount
    return self.shards

  def remove_money(self,amount):
    self.shards -= amount
    return self.shards

  def add_card(self, card):
      self.hand.append(card)
      return self.hand
    
  def clear_hand(self):
    self.hand.clear()
    return self.hand
