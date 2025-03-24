from game import Game, console

if __name__ == '__main__':
  try:
    game = Game()
    game.start()
  except KeyboardInterrupt:
    console.print("\nGame Exited", style="bold red")