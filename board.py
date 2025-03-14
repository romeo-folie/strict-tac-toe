from typing import Tuple
from player import Player

class Board:
  def __init__(self):
    # representing board state with a 3*3 matrix
    self.state = [[' '] * 3, [' '] * 3, [' '] * 3]
  
  def print(self) -> None:
    print("-------------")
    for i, row in enumerate(self.state):
      print("| {} | {} | {} |".format(row[0], row[1], row[2]))
      if i < 2: 
        print("----+---+----")
    print("-------------")

  def reset(self) -> None:
    self.state = [[' '] * 3, [' '] * 3, [' '] * 3]
    
  def is_position_occupied(self, position: Tuple[int, int]) -> bool:
    row, col = position
    return self.state[row][col] != ' '
    
  def play(self, current_player: Player, position: Tuple[int, int]) -> str | None:
    row, col = position
    self.state[row][col] = current_player.symbol
    return self.check_for_winner()
  
  def is_board_full(self) -> bool:
    for i in range(len(self.state)):
      for j in range(len(self.state[i])):
        if self.state[i][j] == ' ':
          return False
    return True
    
  def check_for_winner(self) -> str | None:
    winning_combinations = [
      [(0, 0),(0, 1),(0, 2)],
      [(1,0), (1,1), (1, 2)],
      [(2,0), (2,1), (2, 2)],
      [(0,0), (1,1), (2, 2)],
      [(0,2), (1,1), (2, 0)],
      [(0,0), (1,0), (2, 0)],
      [(0,2), (1,2), (2, 2)]
    ]
    
    for combo in winning_combinations:
      symbols = [self.state[row][col] for row, col in combo]      
      if symbols[0] in ('X', 'O') and symbols[0] == symbols[1] == symbols[2]:
        return symbols[0]
    return None