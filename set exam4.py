from asyncore import write


a= {1,2,3,4,5}
b={4,5,6,7,8}
print(a|b)# else we write a.union (b)
print(b|a)# else we write a union (a)



# set intersection

print (a&b) #else we write a.intersection(b)
d=a.intersection(b)
print(d)

# set difference 
print (a-b)or a.difference(b)

# set symmetric difference

print(a*b)# else we write a.symmetric difference 



