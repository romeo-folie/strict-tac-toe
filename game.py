import re
import sys
import time
from typing import Tuple
from board import Board
from player import Player
from rich.console import Console

console = Console()
position_pattern = re.compile(r"^[0-2]{1}[,\s]{1}[0-2]{1}$")

class Game:
  def __init__(self):
    self.board = Board()
    self.player_X = Player('X')
    self.player_O = Player('O', True)
    self.winner = None
    self.current_player = self.player_X
    
  def print_instructions(self) -> None:
    console.print("\nGAME INSTRUCTIONS", style="bold")
    console.print("Row and Column values should be between 0-2 inclusive")
    console.print("Press Ctrl + C to exit\n")
  
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
      console.print("Current Player is {}\n".format(self.current_player), style="yellow")
      
      if self.current_player.is_computer:
        print("Thinking...")
        time.sleep(1)
        position = self.board.get_computer_move(self.current_player.symbol)
      else:
        try:
          position = self.get_player_input()
        except ValueError:
          console.print("\n:x: Wrong Input. You have forfeited your turn\n", style="bold red")
          self.current_player = self.get_next_player()
          continue
        
        if self.board.is_position_occupied(position):
          console.print("\n:prohibited: POSITION ALREADY OCCUPIED\n", style="bold red")
          continue
      
      self.winner = self.board.move(self.current_player, position)
      self.current_player = self.get_next_player()
    
    console.print("\nGAME OVER", style="bold red")
    self.board.print()
    if self.winner:
      console.print("Outcome: Player {} wins :1st_place_medal:\n".format(self.winner), style="green bold")
    elif self.board.is_board_full():
      console.print("Outcome: Tie\n", style="yellow bold")
      
    restart_input = input("Restart Game? (y/n): ")
    if restart_input.lower() == 'y':
      self.restart(self.winner)
    else:
      console.print("Game Exited", style="bold red")
      sys.exit(0)
      
  def restart(self, last_winner: str | None) -> None:
    if last_winner:
      self.current_player = self.player_X if self.player_X.symbol == last_winner else self.player_O
    self.winner = None
    self.start()

  
  