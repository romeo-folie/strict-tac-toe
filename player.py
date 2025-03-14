class Player:
  def __init__(self, symbol: str):
    self.symbol = symbol
    
  def __str__(self) -> str:
    return self.symbol
    