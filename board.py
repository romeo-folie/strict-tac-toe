from typing import Tuple
from player import Player
from random import choice

class Board:
  def __init__(self):
    # representing board state with a 3*3 matrix
    self.state = [[' '] * 3, [' '] * 3, [' '] * 3]
    self.winning_combinations = [
      # rows
      [(0,0), (0,1), (0,2)],
      [(1,0), (1,1), (1,2)],
      [(2,0), (2,1), (2,2)],
      # columns
      [(0,0), (1,0), (2,0)],
      [(0,1), (1,1), (2,1)],
      [(0,2), (1,2), (2,2)],
      # diagonals
      [(0,0), (1,1), (2,2)],
      [(0,2), (1,1), (2,0)],
    ]
  
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
  
  def is_board_full(self) -> bool:
    for row in range(len(self.state)):
      for col in range(len(self.state[0])):
        if self.state[row][col] == ' ':
          return False
    return True
    
  def move(self, current_player: Player, position: Tuple[int, int]) -> str | None:
    row, col = position
    self.state[row][col] = current_player.symbol
    return self.check_for_winner()
  
  def get_computer_move(self, symbol: str) -> Tuple[int, int]:
    winning_move = self.get_winning_move(symbol)
    blocking_move = self.get_blocking_move(symbol)
    
    if winning_move:
      return winning_move
    elif blocking_move:
      return blocking_move
    else:
      return self.get_random_move()
  
  def get_random_move(self) -> Tuple[int, int]:
    empty_cells = []
    
    for row in range(len(self.state)):
      for col in range(len(self.state[0])):
        if self.state[row][col] == ' ':
          empty_cells.append((row, col))
          
    return choice(empty_cells)
  
  def get_winning_move(self, symbol: str) -> Tuple[int, int] | None:
    opposing_symbol = 'X' if symbol == 'O' else 'O'
    for combo in self.winning_combinations:
      symbols = [self.state[row][col] for row, col in combo]
      if all(item in symbols for item in (symbol, ' ')):
        if symbols.count(' ') == 1 and symbols.count(opposing_symbol) == 0:
          return combo[symbols.index(' ')]
    return None
  
  def get_blocking_move(self, symbol: str) -> Tuple[int, int] | None:
    opposing_symbol = 'X' if symbol == 'O' else 'O'
    for combo in self.winning_combinations:
      symbols = [self.state[row][col] for row, col in combo]
      if all(item in symbols for item in (opposing_symbol, ' ')):
        if symbols.count(' ') == 1 and symbols.count(symbol) == 0:
          return combo[symbols.index(' ')]
    return None
    
  def check_for_winner(self) -> str | None:
    for combo in self.winning_combinations:
      symbols = [self.state[row][col] for row, col in combo]      
      if symbols[0] in ('X', 'O') and symbols[0] == symbols[1] == symbols[2]:
        return symbols[0]
    return None
  
  