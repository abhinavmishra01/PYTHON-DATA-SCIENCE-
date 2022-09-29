from traceback import print_list


print("place:",msg.find('place'))
print("place:",msg.find('place'))#-1 means not find

val = msg.find('answer')
if val == -1:
   print('word not found')
else:
  print(f'word found at {val}index')

print('is:', msg.find('is'))
print('is:', msg.index ('is'))

print('is:', msg.find('is',3)) #3 is the start point for searching



 