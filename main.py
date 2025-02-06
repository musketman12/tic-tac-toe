#tic tac toe console-based
#
#this program will allow the player to play tic tac toe against 
#the computer, the board will be drawn in text-characters on
#the screen
#
#author: levi dominighini   
#date: 2024-05-12

EMPTY = "empty"
board = [
   EMPTY, EMPTY, EMPTY,
   EMPTY, EMPTY, EMPTY, 
   EMPTY, EMPTY, EMPTY
]

def get_symbol(the_board, square_number):
   symbol = the_board[square_number - 1]
   if symbol == EMPTY:
    return square_number

   return symbol
   
def draw_board (the_board):
   for row in range(3):
      print("   |   |   ")
      print(" {} | {} | {} ".format (get_symbol(the_board, row * 3 + 1), get_symbol(the_board, row * 3 + 2 ), get_symbol(the_board, row * 3 + 3)))
      print("   |   |   ")
      if row < 2: 
          print("---+---+---")

draw_board(board)