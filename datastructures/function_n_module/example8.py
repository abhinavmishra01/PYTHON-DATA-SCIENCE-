from ast import Lambda
from unicodedata import name


x=[2,3,5,6,21,41,15]
output=list(map(lambda i : i**2 , x))
output1=tuple(map(lambda i: i**2 , x))

print(output)
print(output1)

x1=[2,5,3,6,7,4,8,3,7,46]
s1=list(map(lambda i : i-5,x1))
print(s1)

y=[2,3,1,2,3,5,6,3,3,1,2]
x1y=list(map(lambda a,b: a+b, x,y))
print(x1y)

y3= set(map(lambda i :i>3,x1))
print(y3)

y4=set(filter(lambda i:i>3,x))
print(y3)


name=['Raj Singh','Vijay Singh', 'Ram Singh', 'Ravi Kumar']

name_Singh=list(filter(lambda n:n .endswith('Singh'),name))
print(name_Singh)
name_singh=list(filter (lambda  n:n.startswith('R'),name))
print(name_singh)
