


def getcubes(limit=10):
 
 for i in range (1, limit +1):
     yield i**3
      
def primes(start=2, stop=10):
    for num in range (start,stop):
      for i in range(2,num):
        if num%1==0:
            break
      else:
            yield num
            
for p in primes(stop=100):
     print(p)

    
     for val in getcubes():
     
      print(val)
     
for val in getcubes(4):
    print(val)
    
for val in getcubes(5):
    print(val)
    
     
        
             
    