class Dealer:
  def __init__(self):
    self.hand = []
    self.hand_value = 0

  def add_card(self, card):
    self.hand.append(card)
    return self.hand
    
  def clear_hand(self):
    self.hand.clear()
    return self.hand
