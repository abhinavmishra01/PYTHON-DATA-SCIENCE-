
def word_counter(s):
    words =s.split()
    return len (words)

print(word_counter('This is an example'))
print(word_counter('Welcome to the code of python'))
print(word_counter("screnshot se kuch nhi hota"))
print(word_counter('rules and convention likh lo!!!'))

# call area and circumference

#1.direct
print(area(10,10))

#2.user input
a= int (input('enter length:'))
b= int (input('enter the breadth:'))
out= area(a,b)
print('area=>>', out)

# 3. shorter user input

out= 