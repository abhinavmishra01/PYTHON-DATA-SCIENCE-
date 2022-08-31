# create  a prime numbers list upto size n
# 2,3,5,7,11,

n=20
primes=[]

for i in range (2,n +1):
    for j in range(2,int(i**0.3)+1):
        if i %j==0:
            
            break
        else:
            primes.append(i)

print(primes)    