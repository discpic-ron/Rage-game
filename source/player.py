class Player:
  def __init__(self,name,shards=100):
    self.name = name
    self.shards = shards
    self.hand = []

  def add_shards(self,amount):
    self.shards += amount
    return self.shards

  def remove_money(self,amount):
    self.shards -= amount
    return self.shards
