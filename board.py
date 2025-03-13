class Board:
  def __init__(self):
    # representing board state with a 3*3 matrix
    self.state = [['*'] * 3, ['*'] * 3, ['*'] * 3]
  
  def print(self):
    print("-------------")
    for i, row in enumerate(self.state):
      print("| {} | {} | {} |".format(row[0], row[1], row[2]))
      if i < 2: 
        print("----+---+----")
    print("-------------")

  def reset(self):
    self.state = [['*'] * 3, ['*'] * 3, ['*'] * 3]
    
  def play(self, current_player_symbol, position):
    # serialize position data
    # modify board state with the given symbol
    position = map(int, position.replace(',', ' ').split())
    row, col = next(position), next(position)
    # handle the case when the spot is already occupied
    self.state[row][col] = current_player_symbol
    return self.check_winner()
    
  def check_winner(self):
    # return None if there's no winner
    # otherwise, return the symbol of the current player
    # construct a list of possible winning index combinations
    # loop through that matrix
    # for each row, get the indices
    # compare them and if they match
    # return that value
    # if we reach the end of the loop we return None
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