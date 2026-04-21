class Card:
  registry = []

  def __init__(self, rank, suit, number_rank, image=None):
    self.rank = rank
    self.suit = suit
    self.number_rank = number_rank
    self.image = image
    Card.registry.append(self)

  def get_rank(self):
    return self.rank

  def get_suit(self):
    return self.suit

  def get_value(self):
    return self.number_rank

  def get_image(self):
    return self.image
