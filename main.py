def print_board(board):
  print("\n")
  for row in range(3):
      row_display = []
      for col in range(3):
          row_display.append(board[row][col] if board[row][col] in "XO" else str(3 * row + col + 1))
      print(" | ".join(row_display))
      if row < 2:
          print("-" * 9)
  print("\n")

def check_win(board, player):
  win_conditions = [
      [board[0][0], board[0][1], board[0][2]],
      [board[1][0], board[1][1], board[1][2]],
      [board[2][0], board[2][1], board[2][2]],
      [board[0][0], board[1][0], board[2][0]],
      [board[0][1], board[1][1], board[2][1]],
      [board[0][2], board[1][2], board[2][2]],
      [board[0][0], board[1][1], board[2][2]],
      [board[2][0], board[1][1], board[0][2]]
  ]
  return [player, player, player] in win_conditions

def make_move(board, num, player):
  mapping = {
      1: (0, 0),
      2: (0, 1),
      3: (0, 2),
      4: (1, 0),
      5: (1, 1),
      6: (1, 2),
      7: (2, 0),
      8: (2, 1),
      9: (2, 2),
  }
  pos = mapping[num]
  if board[pos[0]][pos[1]] in "XO":
      return False
  else:
      board[pos[0]][pos[1]] = player
      return True

def tic_tac_toe():
  board = [[" " for _ in range(3)] for _ in range(3)]
  players = ["X", "O"]
  turn = 0

  while True:
      print_board(board)
      current_player = players[turn % 2]
      print(f"Player {current_player}'s turn. Choose a square (1-9):")

      try:
          choice = int(input())
          if choice < 1 or choice > 9:
              print("Invalid input. Please choose a number between 1 and 9.")
              continue
      except ValueError:
          print("Invalid input. Please enter a number.")
          continue

      if not make_move(board, choice, current_player):
          print("This position is already taken. Choose another one.")
          continue

      if check_win(board, current_player):
          print_board(board)
          print(f"Player {current_player} wins!")
          break

      if all(board[row][col] in "XO" for row in range(3) for col in range(3)):
          print_board(board)
          print("It's a tie!")
          break

      turn += 1

tic_tac_toe()
