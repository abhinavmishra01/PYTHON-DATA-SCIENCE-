
def  triangle_area(b,h=2):
     
     
  return  .5*b*h

  print (triangle_area(10))
  print(triangle_area(5,3))
  print(triangle_area(b=5))
  print(triangle_area(b=7,h=8))

def read(filepath=None):
    if filepath:
        with open (filepath)as f:
   
             return f.read()
    else:
            return' please provide a filepath'
        
    print(read('gl.py'))
           
           
    print(read())  
        