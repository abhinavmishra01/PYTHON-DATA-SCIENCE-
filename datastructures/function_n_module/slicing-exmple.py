from fnmatch import fnmatchcase


name = 'abhinav mishra'
fname = name[:7]
lname =name[-6:]

print(fname,lname)
#reversed
rev_name=name[::-1]
print(rev_name)


#every even index charcater
even_name=name [::2]
#every odd index charcter
odd_name=name[1::2]
print(even_name,odd_name)