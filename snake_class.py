import numpy as np

class Agent:
  def __init__(self,dimension):
    headVar = [np.random.randint(3,dimension-1),np.random.randint(1,dimension-1)] # [x,y]
    midVar = [headVar[0] -1 , headVar[1]] # [x,y]
    tailVar = [headVar[0] -2 , headVar[1]] # [x,y]
    self.path =  [tailVar ,midVar, headVar]
    self.head = self.path[-1]



  def move(self,direction,dimension):
    x = self.head[0]
    y = self.head[1]
    if direction == "Left":
      x = (self.head[0] - 1) 
      if x < 0 :
        x = dimension - 1

    elif direction == "Right":
      x = (self.head[0] + 1) %  (dimension) 

    elif direction == "Up":
      y = (self.head[1] - 1)
      if y < 0 :
        y = dimension - 1

    elif direction == "Down":
      y = (self.head[1] + 1) % (dimension)  

    self.path.append([x,y])

    self.head = self.path[-1]
