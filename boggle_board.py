import random

def randomize_board(self):
  self.display = ""
  for i in range(len(self.board)):
    random_letter = self.board[i][random.randint(0, 5)]
    self.letters_showing[i].clear()
    self.letters_showing[i].append(random_letter)
    self.display += f"{random_letter} "
    if (i+1) % 4 == 0:
      self.display += "\n"
      

class BoggleBoard:
  
  def __init__(self):
    self.board = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    self.display = ""
    self.letters_showing = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in range(16):
      for j in range(6):
        self.board[i].append('_')
    randomize_board(self)
      
  def shake(self):
    if '_' in self.board[0]:
      for i in range(16):
        self.board[i].clear()
        for j in range(6):
          random_letter = chr(random.randint(65, 90))
          if random_letter == "Q":
            random_letter = "Qu"
          self.board[i].append(random_letter)
    randomize_board(self)
  
  
game = BoggleBoard()
print(game.display)
game.shake()
print(game.display)
game.shake()
print(game.display)