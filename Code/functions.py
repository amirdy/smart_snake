import numpy as np
import torch
from __main__ import dimension, features, ep_min, delta_ep, e, memory, batch_size, cuda, Q_target, gamma


def create_frame(path, food): # Coloring
    frame = np.zeros((dimension,dimension))

    frame[0,:] = 0.08 # wall
    frame[dimension-1,:] = 0.08 # wall
    frame[:,0] = 0.08 # wall
    frame[:,dimension-1] = 0.08 # wall

    for item in path[0:-1]:
        frame[item[1],item[0]] = 0.25 # Body

    frame[path[-1][1],path[-1][0]] += 0.5 # Head
    if food!=None:
      frame[food.y,food.x] = 1 # Food

    

    return frame



def return_state(path, food):
    global features
    frame = create_frame(path, food)
    
    state = np.zeros((1,features))
    hx = path[-1][0]
    hy = path[-1][1]
    if food==None: #  Snake won the game
      fx = path[-1][0] # Food x
      fy = path[-1][1] # Food y
    else: 
      fx = food.x # Food x
      fy = food.y # Food y
    
    #adj_wall_x
    if (hx == 1) :
      state[0,0] = 1
    elif hx == (dimension-2) :
      state[0,0] = 2
    else :
      state[0,0] = 0

    #adj_wall_y
    if (hy == 1) :
      state[0,1] = 1
    elif hy == (dimension-2) :
      state[0,1] = 2
    else :
      state[0,1] = 0

    #food_x
    if (fx < hx) :
      state[0,2] = 1
    elif (fx > hx) :
      state[0,2] = 2
    else :
      state[0,2] = 0
      
    #food_y
    if (fy < hy) :
      state[0,3] = 1
    elif (fy > hy) :
      state[0,3] = 2
    else :
      state[0,3] = 0
     
    # Top
    if hy == 0:
      state[0,4] = 0
    else:
      top = frame[hy-1,hx]
      if top == 0.25:
        state[0,4] = 1
      else:
        state[0,4] = 0


    # Bottom
    if hy == (dimension - 1):
      state[0,5] = 0
    else:
      top = frame[hy+1,hx]
      if top == 0.25:
        state[0,5] = 1
      else:
        state[0,5] = 0
    
    # Left
    if hx == 0:
      state[0,6] = 0
    else:
      top = frame[hy,hx-1]
      if top == 0.25:
        state[0,6] = 1
      else:
        state[0,6] = 0

    # Right
    if hx == (dimension - 1):
      state[0,7] = 0
    else:
      top = frame[hy,hx+1]
      if top == 0.25:
        state[0,7] = 1
      else:
        state[0,7] = 0

    

    return state.copy() # np array ([1, features])


def epsilon_greedy(best_action):
    global e

    prob = np.random.rand()
    e = max(ep_min, e - delta_ep)

    if prob < e:
      a = np.random.randint(0,4)
      return a # Random
    else:
      return best_action


def return_batch_X(memory):

    if len(memory) == 1 :
      new_X = np.zeros((2,features))

    else:
      new_X = np.zeros((min(len(memory), batch_size),features))

    indexes = []


    if len(memory) < batch_size:
        for i in range(len(memory)):
            new_X[i,:] = memory[i][0]
            indexes.append(i)

        if len(memory) == 1:
            new_X[1,:] = memory[0][0]
            indexes.append(0)
    

    else : 
        indexes = np.random.choice(len(memory),new_X.shape[0], replace=False)
        for index , value in enumerate(indexes):
            new_X[index,:] = memory[value][0]

    return torch.from_numpy(new_X), indexes




def cal_Y(memory_indexes, memory):
    y = np.zeros((len(memory_indexes),1))

    next_state = np.zeros((y.shape[0],features))
    r = np.zeros((y.shape[0],1))
    terminal = np.zeros((y.shape[0],1))

    for idx , value in enumerate(memory_indexes):
            next_state[idx] = memory[value][3] #  torch.Size([1 ,features]) 
            r[idx,0] = memory[value][2]
            terminal[idx,0] = memory[value][4]

    tensor_next_state = torch.from_numpy(next_state)
    r = torch.from_numpy(r)
    y = torch.from_numpy(y)
    terminal = torch.from_numpy(terminal)

    if cuda.is_available():
       tensor_next_state = tensor_next_state.cuda()
       r = r.cuda()
       terminal = terminal.cuda()


    with torch.no_grad():
      Q = Q_target( tensor_next_state)

    gamma_Q = gamma * torch.max(Q,dim=1)[0]
    gamma_Q = gamma_Q.view(len(memory_indexes),1)

    y = r + gamma_Q * (1 - terminal)



    return  y #  torch.Size([batch_size, 1]) 




##### Just for Test phase (showing the frames)
def return_state_frame(path, food):	
    global features
    frame = create_frame(path, food)
    
    state = np.zeros((1,features))
    hx = path[-1][0]
    hy = path[-1][1]
    if food==None: #  Snake won the game
      fx = path[-1][0] # Food x
      fy = path[-1][1] # Food y
    else: 
      fx = food.x # Food x
      fy = food.y # Food y
    
    #adj_wall_x
    if (hx == 1) :
      state[0,0] = 1
    elif hx == (dimension-2) :
      state[0,0] = 2
    else :
      state[0,0] = 0

    #adj_wall_y
    if (hy == 1) :
      state[0,1] = 1
    elif hy == (dimension-2) :
      state[0,1] = 2
    else :
      state[0,1] = 0

    #food_x
    if (fx < hx) :
      state[0,2] = 1
    elif (fx > hx) :
      state[0,2] = 2
    else :
      state[0,2] = 0
      
    #food_y
    if (fy < hy) :
      state[0,3] = 1
    elif (fy > hy) :
      state[0,3] = 2
    else :
      state[0,3] = 0
     
    # Top
    if hy == 0:
      state[0,4] = 0
    else:
      top = frame[hy-1,hx]
      if top == 0.25:
        state[0,4] = 1
      else:
        state[0,4] = 0


    # Bottom
    if hy == (dimension - 1):
      state[0,5] = 0
    else:
      top = frame[hy+1,hx]
      if top == 0.25:
        state[0,5] = 1
      else:
        state[0,5] = 0
    
    # Left
    if hx == 0:
      state[0,6] = 0
    else:
      top = frame[hy,hx-1]
      if top == 0.25:
        state[0,6] = 1
      else:
        state[0,6] = 0

    # Right
    if hx == (dimension - 1):
      state[0,7] = 0
    else:
      top = frame[hy,hx+1]
      if top == 0.25:
        state[0,7] = 1
      else:
        state[0,7] = 0

    

    return state.copy(), frame # state: np array ([1, features]) , frame: np array ([dimension, dimension])

