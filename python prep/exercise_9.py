#exhaustive search algorithm by going through all candidate solutions and check whether it is correct


#number_in = float(input("Please enter a number: "))

#if number_in < 0:
    #number_in = abs(number_in)
#else:
 #   pass

#print(number_in)

#for i in range(0, int(number_in + 1)):
 #   if 
  #  print(i)
n = float(input("Please enter a positive number: "))

step_size = 0.000001
tolerance = 0.0001

root = 0
found = False
while not found and root <= n:
    #set a tolerance level  to get value
    if abs(root*root - n) < tolerance:
        print(root)
		#exit() [will be discussed in one of the lectures in order to reduce the search space]
        found = True
    else:
        root = root + step_size
