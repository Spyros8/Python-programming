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
found = False
if init_direct == 'n':
    while (found == False) & (0 <= ro_coordinate <= quadrant_condition2) & (0 <= col_coordinate <= quadrant_condition2):
        if (ro_coordinate == 0):
            print(f"I am currently at ({ro_coordinate}, {col_coordinate}), facing North")
            print("I have a wall in front of me")
            found = True
        else:
            print(f"I am currently at ({ro_coordinate}, {col_coordinate}), facing North")
            print(f"Moving one step forward")
            ro_coordinate = ro_coordinate - 1
elif init_direct == 's':
    while (found == False) & (0 <= ro_coordinate <= quadrant_condition2) & (0 <= col_coordinate <= quadrant_condition2):
        if (ro_coordinate == quadrant_condition2):
            print(f"I am currently at ({ro_coordinate}, {col_coordinate}), facing South")
            print("I have a wall in front of me")
            found = True
        else:
            print(f"I am currently at ({ro_coordinate}, {col_coordinate}), facing South")
            print(f"Moving one step forward")
            ro_coordinate = ro_coordinate + 1
            
elif init_direct == 'w':
    while (found == False) & (0 <= ro_coordinate <= quadrant_condition2) & (0 <= col_coordinate <= quadrant_condition2):
        if (col_coordinate == 0):
            print(f"I am currently at ({ro_coordinate}, {col_coordinate}), facing West")
            print("I have a wall in front of me")
            found = True
        else:
            print(f"I am currently at ({ro_coordinate}, {col_coordinate}), facing West")
            print(f"Moving one step forward")
            col_coordinate = col_coordinate - 1
elif init_direct == 'e':
    while (found == False) & (0 <= ro_coordinate <= quadrant_condition2) & (0 <= col_coordinate <= quadrant_condition2):
        if (col_coordinate == quadrant_condition2):
            print(f"I am currently at ({ro_coordinate}, {col_coordinate}), facing East")
            print("I have a wall in front of me")
            found = True
        else:
            print(f"I am currently at ({ro_coordinate}, {col_coordinate}), facing East")
            print(f"Moving one step forward")
            col_coordinate = col_coordinate + 1
else:
    pass

#Identify new quadrant robot rests in

#if (0 <= ro_coordinate <= quadrant_condition1) & (0 <= col_coordinate <= quadrant_condition1):
 #   print(f"My current location is ({ro_coordinate}, {col_coordinate}). I am in the top left quadrant")
#elif (0 <= ro_coordinate <= quadrant_condition1) & (quadrant_condition1 <= col_coordinate <= quadrant_condition2):
 #   print(f"My current location is ({ro_coordinate}, {col_coordinate}). I am in the top right quadrant")
#elif (quadrant_condition1 <= ro_coordinate <= quadrant_condition2) & (0 <= col_coordinate <= quadrant_condition1):
 #   print(f"My current location is ({ro_coordinate}, {col_coordinate}). I am in the bottom left quadrant")
#else:
 #   print(f"My current location is ({ro_coordinate}, {col_coordinate}). I am in the bottom right quadrant")