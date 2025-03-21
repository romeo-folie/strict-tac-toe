class Player:
  def __init__(self, symbol: str, is_computer: bool = False):
    self.symbol = symbol
    self.is_computer = is_computer
    
  def __str__(self) -> str:
    return self.symbol
    