""" 3) Write a program to solve a classic puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
How many rabbits and how many chickens do we have? 
create function: solve(numheads, numlegs): """

def solve(numheads,numlegs):
    for chickens in range (numheads+1):
        rabbits = numlegs - chickens 
        total_num_of_legs = (chickens * 2) + (rabbits * 4)
        if total_num_of_legs == numlegs:
            return chickens , rabbits
    
numlegs = 94
numheads = 35
answer = solve(numheads , numheads)
print (answer)
    


