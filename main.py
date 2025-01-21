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

def draw_board (the_board):
  print("   |   |   ")
  print(" {} | {} | {} ".format(1,2,3))
  print("   |   |   ")
  print("---+---+---")
  print("   |   |   ")
  print(" {} | {} | {} ".format(4,5,6))
  print("   |   |   ")
  print("---+---+---")
  print("   |   |   ")
  print(" {} | {} | {} ".format(7,8,9))
  print("   |   |   ")

draw_board(board)
 