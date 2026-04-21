class Chip:
  registry = []

  def __init__(self, name, amount):
    self.name = name
    self.amount = amount
    Chip.registry.append(self)

  def get_name(self):
    return self.name

  def get_value(self):
    return self.amount
