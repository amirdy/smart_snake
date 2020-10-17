import numpy as np 


class meal:
  def __init__(self,x,y):
    self.x = x
    self.y = y

####################
def food_init(dimension,path):
    if len(path) == ((dimension-2)*(dimension-2)):

         food = None
         return food,True
    while(True):
        foodX = np.random.randint(1,dimension-1)
        foodY = np.random.randint(1,dimension-1)
		
        if  [foodX,foodY] not in path  :
        #global food 
            food= meal(foodX,foodY)
            break
    return food,False
