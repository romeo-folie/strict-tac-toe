from board import Board
from player import Player

class Game:
  def __init__(self):
    self.board = Board()
    self.player_X = Player('X')
    self.player_O = Player('O')
    self.winner = None
    self.current_player = self.player_X.symbol
    
  def print_instructions(self):
    # print out game instructions
    print("GAME INSTRUCTIONS")
    print("Row and Column values should be between 0-2 inclusive")
    print("Press Ctrl + C to exit\n")
    print("PLAYERS")
    print("{} {}\n".format(self.player_X, self.player_O))
  
  def get_next_player(self):
    return 'O' if self.current_player == 'X' else 'X'
  
  def start(self):
    # this should run in a loop till there's a winner or an interrupt is received from the cmd
    # print board state
    # print next player message
    # based on next player
    # get their input on the position on the board to put their symbol
    self.print_instructions()
    self.board.reset()
    # find a way to make sure this infinite loop doesn't cost me
    # this should also depend on whether the board is full
    
    while(self.winner is None):
      self.board.print()
      print("Current Player is {}\n".format(self.current_player))
      
      # try:
      position = input("Enter row and column (e.g. 0,2 or 0 2): ")
      # except ValueError:
      #   # consider not breaking but making the user forfeit their turn instead
      #   # print("Please refer to game instructions and restart")
      #   # self.next_player = self.get_next_player()
      #   break
        
      # check input range to ensure that it's within bounds of a 3x3 matrix
      # also ensure they're integers or throw an Error
      self.winner = self.board.play(self.current_player, position)
      self.current_player = self.get_next_player()
      
    print("Winner is Player {}".format(self.winner))
    
    
if __name__ == '__main__':
  try:
    game = Game()
    game.start()
  except KeyboardInterrupt:
    print("\nGame Exited")


  
  