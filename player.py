class Player:
  def __init__(self, symbol):
    self.symbol = symbol
    self.score = 0
    
  def __str__(self):
    return self.symbol
    