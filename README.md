# Smart_Snake


# State
### s<sub>t</sub> : 
The last game frame :

### &phi;(s<sub>t</sub>) :
8 features extracted from the frame as below:
##### [Adjoining_wall_x, Adjoining_wall_y, food_dir_x, food_dir_y, Adjoining_body_top, Adjoining_body_bottom, Adjoining_body_left, Adjoining_body_right]

![equation](https://latex.codecogs.com/svg.latex?%5Cfn_cs%20%5Csmall%20%5Ctext%7BAdjoining%5C_wall%5C_x%7D%3D%5Cbegin%7Bcases%7D%200%2C%20%26%20%5Ctext%7Bno%20adjoining%20wall%20on%20x%20axis%7D.%5C%5C%201%2C%20%26%20%5Ctext%7Bwall%20on%20snake%20head%20left%7D.%20%5C%5C%202%2C%20%26%20%5Ctext%7Bwall%20on%20snake%20head%20right%7D.%20%5Cend%7Bcases%7D)

![equation](https://latex.codecogs.com/svg.latex?%5Cfn_cs%20%5Csmall%20%5Ctext%7BAdjoining%5C_wall%5C_y%7D%3D%5Cbegin%7Bcases%7D%200%2C%20%26%20%5Ctext%7Bno%20adjoining%20wall%20on%20y%20axis%7D.%5C%5C%201%2C%20%26%20%5Ctext%7Bwall%20on%20snake%20head%20top%7D.%20%5C%5C%202%2C%20%26%20%5Ctext%7Bwall%20on%20snake%20head%20bottom%7D.%20%5Cend%7Bcases%7D)

![equation](https://latex.codecogs.com/svg.latex?%5Cfn_cs%20%5Csmall%20%5Ctext%7BFood%5C_dir%5C_x%7D%3D%5Cbegin%7Bcases%7D%200%2C%20%26%20%5Ctext%7Bsame%20coords%20on%20x%20axis%7D.%5C%5C%201%2C%20%26%20%5Ctext%7Bfood%20on%20snake%20head%20left%7D.%20%5C%5C%202%2C%20%26%20%5Ctext%7Bfood%20on%20snake%20head%20right%7D.%20%5Cend%7Bcases%7D)

![equation](https://latex.codecogs.com/svg.latex?%5Cfn_cs%20%5Csmall%20%5Ctext%7BFood%5C_dir%5C_y%7D%3D%5Cbegin%7Bcases%7D%200%2C%20%26%20%5Ctext%7Bsame%20coords%20on%20y%20axis%7D.%5C%5C%201%2C%20%26%20%5Ctext%7Bfood%20on%20snake%20head%20top%7D.%20%5C%5C%202%2C%20%26%20%5Ctext%7Bfood%20on%20snake%20head%20bottom%7D.%20%5Cend%7Bcases%7D)

![equation](https://latex.codecogs.com/svg.latex?%5Cfn_cs%20%5Csmall%20%5Ctext%7BAdjoining%5C_body%5C_top%7D%20%3D%5Cbegin%7Bcases%7D%201%2C%20%26%20%5Ctext%7Badjoining%20top%20square%20has%20snake%20body%7D.%5C%5C%200%2C%20%26%20%5Ctext%7Botherwise%7D.%20%5Cend%7Bcases%7D)
![equation](https://latex.codecogs.com/svg.latex?%5Cfn_cs%20%5Csmall%20%5Ctext%7BAdjoining%5C_body%5C_bottom%7D%20%3D%5Cbegin%7Bcases%7D%201%2C%20%26%20%5Ctext%7Badjoining%20bottom%20square%20has%20snake%20body%7D.%5C%5C%200%2C%20%26%20%5Ctext%7Botherwise%7D.%20%5Cend%7Bcases%7D)

![equation](https://latex.codecogs.com/svg.latex?%5Cfn_cs%20%5Csmall%20%5Ctext%7BAdjoining%5C_body%5C_left%7D%20%3D%5Cbegin%7Bcases%7D%201%2C%20%26%20%5Ctext%7Badjoining%20left%20square%20has%20snake%20body%7D.%5C%5C%200%2C%20%26%20%5Ctext%7Botherwise%7D.%20%5Cend%7Bcases%7D)
![equation](https://latex.codecogs.com/svg.latex?%5Cfn_cs%20%5Csmall%20%5Ctext%7BAdjoining%5C_body%5C_right%7D%20%3D%5Cbegin%7Bcases%7D%201%2C%20%26%20%5Ctext%7Badjoining%20right%20square%20has%20snake%20body%7D.%5C%5C%200%2C%20%26%20%5Ctext%7Botherwise%7D.%20%5Cend%7Bcases%7D)


# Network
#### Input Data :
###### **(Batch_size, 8)**

#### Layers  : 
###### **FC(1024)** &rarr; **ReLU** &rarr; **FC(1024)** &rarr; **ReLU** &rarr; **FC(1024)** 

