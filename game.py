import re
import sys
from typing import Tuple
from board import Board
from player import Player

position_pattern = re.compile(r"^[0-2]{1}[,\s]{1}[0-2]{1}$")
class Game:
  def __init__(self):
    self.board = Board()
    self.player_X = Player('X')
    self.player_O = Player('O')
    self.winner = None
    self.current_player = self.player_X
    
  def print_instructions(self) -> None:
    print("GAME INSTRUCTIONS")
    print("Row and Column values should be between 0-2 inclusive")
    print("Press Ctrl + C to exit\n")
  
  def get_next_player(self) -> Player:
    return self.player_O if self.current_player is self.player_X else self.player_X
  
  def game_over(self) -> bool:
    if self.board.is_board_full() or self.winner:
      return True
    return False
  
  def get_player_input(self) -> Tuple[int, int]:
    position_input = input("Enter row and column (e.g. 0,0 or 0 0): ")
    if not position_pattern.match(position_input):
      raise ValueError
    position = map(int, position_input.replace(',', ' ').split())
    row, col = next(position), next(position)
    return (row, col)
    
  def start(self) -> None:
    self.print_instructions()
    self.board.reset()
    
    while not self.game_over():
      self.board.print()
      print("Current Player is {}\n".format(self.current_player))
      
      try:
        position = self.get_player_input()
      except ValueError:
        print("Wrong Input. You have forfeited your turn")
        self.current_player = self.get_next_player()
        continue
      
      if self.board.is_position_occupied(position):
        print("\nPOSITION ALREADY OCCUPIED\n")
        continue
      
      self.winner = self.board.play(self.current_player, position)
      self.current_player = self.get_next_player()
    
    print("\nGAME OVER")
    self.board.print()
    if self.winner:
      print("Outcome: Winner is Player {}\n".format(self.winner))
    elif self.board.is_board_full():
      print("Outcome: Tie\n")
      
    restart_input = input("Restart Game? (y/n): ")
    if restart_input.lower() == 'y':
      self.restart(self.winner)
    else:
      print("Game Exited")
      sys.exit(0)
      
  def restart(self, last_winner: str | None) -> None:
    if last_winner:
      self.current_player = self.player_X if self.player_X.symbol == last_winner else self.player_O
    self.winner = None
    self.start()

  
  