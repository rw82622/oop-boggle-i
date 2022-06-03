import random

class BoggleBoard:
  
  def __init__(self):
    self.board = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    self.display = ""
    for i in range(16):
      for j in range(6):
        self.board[i].append('_')
    for i in range(len(self.board)):
      self.display += f"{self.board[i][random.randint(0, 5)]} "
      if (i+1) % 4 == 0:
        self.display += "\n"
      

  def shake(self):
    self.board = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    self.display = ""
    for i in range(16):
      for j in range(6):
        random_letter = chr(random.randint(65, 90))
        if random_letter == "Q":
          random_letter = "Qu"
        self.board[i].append(random_letter)
    for i in range(len(self.board)):
      self.display += f"{self.board[i][random.randint(0, 5)]} "
      if (i+1) % 4 == 0:
        self.display += "\n"
  
  
game = BoggleBoard()
print(game.display)
game.shake()
print(game.display)
game.shake()
print(game.display)
