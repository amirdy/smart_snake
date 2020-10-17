# Smart_Snake
|<img src="./README_Files/sample1.gif"  height="300" width="500" > | 
|:--:| 
| <b> score = 43 </b> |

<table>
  <tr>
    <td> <img src="./README_Files/sample1.gif"  alt="1" width = 300px height = 200px ></td>
    <td> <img src="./README_Files/sample11.gif"  alt="2" width = 300px height = 200px></td>
    <td> <img src="./README_Files/sample11.gif"  alt="2" width = 300px height = 200px></td>
   </tr> 
   <tr> 
      <td align="center"><b>score = 43</b></td>
      <td align="center"><b>score = 43</b></td>
      <td align="center"><b>score = 43</b></td>
  </tr>
</table>



# Algorithm

|<img src="README_Files/Algorithm1.png"  height="400" width="500" > | 
|:--:| 
| *DQN Pseudo Code (https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf)* |


###### Q = Q<sub>&theta;</sub> = Action-Value Function = Policy network
###### Q<sup>^</sup> = Q<sub>&theta;<sup>-</sup></sub> = Target Function = Target network
### Note:

#### The implementation has some differences with the above algorithm:

1. ##### The training (calculating loss and updating the weights) doesn't apply on the first 2000 steps.
   - ###### Because there is not enough samples in the replay memory.

2. ##### Target Network updates every C episodes (not every C steps).


# Hyperparameters
- #### C: 
   - ###### 10
- #### &gamma;: 
   - ###### 0.99
- #### Batch size : 
   - ###### 128
- #### actions : 
   - ###### (Left, Right, Up, Down) ~ (0, 1, 2, 3)
- #### Rewards : 
   - ###### (Reward<sub>Food</sub> , Reward<sub>Loose</sub> , Reward<sub>Move</sub>) ~ (100, -100, -0.1)
- #### N (Replay Memory Size) : 
   - ###### 50000
- #### M (Number of Episodes) : 
   - ###### 30000
- #### Learning rate : 
   - ###### 0.001
- #### Optimizer : 
   - ###### RMSprop

# State
### s<sub>t</sub> : 
#### &nbsp; Frame of the game after t transitions
|<img src="README_Files/frame.png"  height="300" width="500" > | 
|:--:| 
| Np array - (12 &times; 12) |


### &phi;(s<sub>t</sub>) :
&nbsp; 8 features extracted from the frame as below:
##### &nbsp; [Adjoining_wall_x, Adjoining_wall_y, food_dir_x, food_dir_y, Adjoining_body_top, Adjoining_body_bottom, Adjoining_body_left, Adjoining_body_right]

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ![equation](https://latex.codecogs.com/svg.latex?%5Cfn_cs%20%5Csmall%20%5Ctext%7BAdjoining%5C_wall%5C_x%7D%3D%5Cbegin%7Bcases%7D%200%2C%20%26%20%5Ctext%7Bno%20adjoining%20wall%20on%20x%20axis%7D.%5C%5C%201%2C%20%26%20%5Ctext%7Bwall%20on%20snake%20head%20left%7D.%20%5C%5C%202%2C%20%26%20%5Ctext%7Bwall%20on%20snake%20head%20right%7D.%20%5Cend%7Bcases%7D)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ![equation](https://latex.codecogs.com/svg.latex?%5Cfn_cs%20%5Csmall%20%5Ctext%7BAdjoining%5C_wall%5C_y%7D%3D%5Cbegin%7Bcases%7D%200%2C%20%26%20%5Ctext%7Bno%20adjoining%20wall%20on%20y%20axis%7D.%5C%5C%201%2C%20%26%20%5Ctext%7Bwall%20on%20snake%20head%20top%7D.%20%5C%5C%202%2C%20%26%20%5Ctext%7Bwall%20on%20snake%20head%20bottom%7D.%20%5Cend%7Bcases%7D)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ![equation](https://latex.codecogs.com/svg.latex?%5Cfn_cs%20%5Csmall%20%5Ctext%7BFood%5C_dir%5C_x%7D%3D%5Cbegin%7Bcases%7D%200%2C%20%26%20%5Ctext%7Bsame%20coords%20on%20x%20axis%7D.%5C%5C%201%2C%20%26%20%5Ctext%7Bfood%20on%20snake%20head%20left%7D.%20%5C%5C%202%2C%20%26%20%5Ctext%7Bfood%20on%20snake%20head%20right%7D.%20%5Cend%7Bcases%7D)
 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ![equation](https://latex.codecogs.com/svg.latex?%5Cfn_cs%20%5Csmall%20%5Ctext%7BFood%5C_dir%5C_y%7D%3D%5Cbegin%7Bcases%7D%200%2C%20%26%20%5Ctext%7Bsame%20coords%20on%20y%20axis%7D.%5C%5C%201%2C%20%26%20%5Ctext%7Bfood%20on%20snake%20head%20top%7D.%20%5C%5C%202%2C%20%26%20%5Ctext%7Bfood%20on%20snake%20head%20bottom%7D.%20%5Cend%7Bcases%7D)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ![equation](https://latex.codecogs.com/svg.latex?%5Cfn_cs%20%5Csmall%20%5Ctext%7BAdjoining%5C_body%5C_top%7D%20%3D%5Cbegin%7Bcases%7D%201%2C%20%26%20%5Ctext%7Badjoining%20top%20square%20has%20snake%20body%7D.%5C%5C%200%2C%20%26%20%5Ctext%7Botherwise%7D.%20%5Cend%7Bcases%7D)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ![equation](https://latex.codecogs.com/svg.latex?%5Cfn_cs%20%5Csmall%20%5Ctext%7BAdjoining%5C_body%5C_bottom%7D%20%3D%5Cbegin%7Bcases%7D%201%2C%20%26%20%5Ctext%7Badjoining%20bottom%20square%20has%20snake%20body%7D.%5C%5C%200%2C%20%26%20%5Ctext%7Botherwise%7D.%20%5Cend%7Bcases%7D)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ![equation](https://latex.codecogs.com/svg.latex?%5Cfn_cs%20%5Csmall%20%5Ctext%7BAdjoining%5C_body%5C_left%7D%20%3D%5Cbegin%7Bcases%7D%201%2C%20%26%20%5Ctext%7Badjoining%20left%20square%20has%20snake%20body%7D.%5C%5C%200%2C%20%26%20%5Ctext%7Botherwise%7D.%20%5Cend%7Bcases%7D)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ![equation](https://latex.codecogs.com/svg.latex?%5Cfn_cs%20%5Csmall%20%5Ctext%7BAdjoining%5C_body%5C_right%7D%20%3D%5Cbegin%7Bcases%7D%201%2C%20%26%20%5Ctext%7Badjoining%20right%20square%20has%20snake%20body%7D.%5C%5C%200%2C%20%26%20%5Ctext%7Botherwise%7D.%20%5Cend%7Bcases%7D)


# Network
#### Input Data :
###### &nbsp; **(Batch_size, 8)**

#### Layers  : 
###### &nbsp; **FC(1024)** &rarr; **ReLU** &rarr; **FC(1024)** &rarr; **ReLU** &rarr; **FC(512)** &rarr; **ReLU** &rarr; **FC(4)** 




 
