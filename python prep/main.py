from random import randrange
from random import choice
#Inputs

name = str(input("What is the name of the robot?: "))
ro_coordinate = int(randrange(-101, 101, 1))
col_coordinate = int(randrange(-101, 101, 1))
init_direct = str(choice(['n', 's', 'w', 'e']))

id = 1000
grid_size = 10

#Bounding quadrants

quadrant_condition1 = int(grid_size/2 - 1)
quadrant_condition2 = int(grid_size - 1)

relevant_grid_size = int(grid_size - 1)

#Making sure that coordinates are within grid system initially

if ro_coordinate < 0:
    ro_coordinate = 0
elif ro_coordinate > relevant_grid_size:
    ro_coordinate = relevant_grid_size
	
if col_coordinate < 0:
    col_coordinate = 0
elif col_coordinate > relevant_grid_size:
    col_coordinate = relevant_grid_size

message = f"Hello. My name is {name}. My ID is {id}."
print(message) 

#Identifying the quadrant the robot is in

if (0 <= ro_coordinate <= quadrant_condition1) & (0 <= col_coordinate <= quadrant_condition1):
    print(f"My current location is ({ro_coordinate}, {col_coordinate}). I am in the top left quadrant")
elif (0 <= ro_coordinate <= quadrant_condition1) & (quadrant_condition1 <= col_coordinate <= quadrant_condition2):
    print(f"My current location is ({ro_coordinate}, {col_coordinate}). I am in the top right quadrant")
elif (quadrant_condition1 <= ro_coordinate <= quadrant_condition2) & (0 <= col_coordinate <= quadrant_condition1):
    print(f"My current location is ({ro_coordinate}, {col_coordinate}). I am in the bottom left quadrant")
else:
    print(f"My current location is ({ro_coordinate}, {col_coordinate}). I am in the bottom right quadrant")

#Identifying the direction the robot is facing	

if init_direct == 'n':
    print("I am facing North")
elif init_direct == 's':
    print("I am facing South")
elif init_direct == 'e':
    print("I am facing East")
elif init_direct == 'w':
    print("I am facing West")

print("Moving one step forward")

#Executing movement within bounded region

if (init_direct == "n") & (0 < ro_coordinate):
    ro_coordinate = ro_coordinate + 1

elif (init_direct == "s") & (ro_coordinate < quadrant_condition2):
    ro_coordinate = ro_coordinate - 1

elif (init_direct == "w") & (0 < col_coordinate):
    col_coordinate = col_coordinate - 1

elif (init_direct == "e") & (col_coordinate < quadrant_condition2):
    col_coordinate = col_coordinate + 1
else:
    pass

#Identify new quadrant robot rests in

if (0 <= ro_coordinate <= quadrant_condition1) & (0 <= col_coordinate <= quadrant_condition1):
    print(f"My current location is ({ro_coordinate}, {col_coordinate}). I am in the top left quadrant")
elif (0 <= ro_coordinate <= quadrant_condition1) & (quadrant_condition1 <= col_coordinate <= quadrant_condition2):
    print(f"My current location is ({ro_coordinate}, {col_coordinate}). I am in the top right quadrant")
elif (quadrant_condition1 <= ro_coordinate <= quadrant_condition2) & (0 <= col_coordinate <= quadrant_condition1):
    print(f"My current location is ({ro_coordinate}, {col_coordinate}). I am in the bottom left quadrant")
else:
    print(f"My current location is ({ro_coordinate}, {col_coordinate}). I am in the bottom right quadrant")