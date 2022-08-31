# create a list of  10 numbers and then 
# genertae a list which holds the square vals of original list
#generate a list which holds the cubes vals of original list 

from asyncio import create_subprocess_exec


x= [34,12,312,34,45,4,42,412,31,45]

x2=[]

for i in x:
    sqr = 1**2
    
    x2.append(sqr)
    
    print(x)
    print(x2) 
    
    for i in x:
        cube=i(x+3)
        
        x2.append(cube)
        
        print(x)
        print(x2)
        