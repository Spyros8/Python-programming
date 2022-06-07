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
 
print(f"({ro_coordinate}, {col_coordinate})")

#Making robot move through grid system
#The while conditional statement is issue
if (init_direct == 'n'):

    while (0 <= ro_coordinate <= quadrant_condition2):
        if (0 == ro_coordinate):
            print("I have a wall in front of me")
            print("Turning 90 degrees clockwise")
            init_direct = 'e'
            print(f"I am currently at ({ro_coordinate}, {col_coordinate}), facing East")
            
            
        else:   
        
            print(f"I am currently at ({ro_coordinate}, {col_coordinate}), facing  North")
            print("Moving one step forward")
            ro_coordinate = ro_coordinate + 1
        break
            
elif (init_direct == 's'):

    while (0 <= ro_coordinate <= quadrant_condition2):
    
        if (ro_coordinate == quadrant_condition2):
        
            print("I have a wall in front of me")
            print("Turning 90 degrees clockwise")
            init_direct = 'w'
            print(f"I am currently at ({ro_coordinate}, {col_coordinate}), facing West")
            
            
        else:
        
            print(f"My current location is ({ro_coordinate}, {col_coordinate}), facing South")
            print(f"Moving one step forward")		
            ro_coordinate = ro_coordinate - 1
            
        break
            
elif (init_direct == 'e'):

    while (0 <= col_coordinate <= quadrant_condition2):
    
        if (col_coordinate == 0):
            print("I have a wall in front of me")
            print("Turning 90 degrees clockwise")
            init_direct = 's'
            print(f"I am currently at ({ro_coordinate}, {col_coordinate}), facing South")
            
            
        else:
        
            print(f"My current location is ({ro_coordinate}, {col_coordinate}), facing East")
            print("Moving one step forward")	
            col_coordinate = col_coordinate + 1
            
        break
            
elif (init_direct == 'w'):

    while (0 <= col_coordinate <= quadrant_condition2):
    
        if (col_coordinate == quadrant_condition2):
        
            print("I have a wall in front of me")
            print("Turning 90 degrees clockwise")
            init_direct = 'n'
            print(f"I am currently at ({ro_coordinate}, {col_coordinate}), facing North")
            
            
        else:
        
            print(f"My current location is ({ro_coordinate}, {col_coordinate}), facing West")
            print(f"Moving one step forward")		
            col_coordinate = col_coordinate - 1
        break
            
else:
    
    pass
#print("I have a wall in front of me!")
