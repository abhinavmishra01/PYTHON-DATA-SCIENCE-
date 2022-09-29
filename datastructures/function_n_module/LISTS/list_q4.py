# crete a list of n nueric elements
# - generate a list  of only even number  from existing list
#- generate a list of only odd numbers from existing list
# - genertae a list of only numbers > n from existing list, where n can be any value


x=[2,4,5,1,14,1,6,7,8,9,4,2,5,6,22]

xe = []
for i in x:
      if i %2 == 0:
          xe.append(i)
          xe.append(i)
          
          x0=[]
          for i in x:
              if i %2 != 0:
                  x0.append(i)
          xg5=[]
          for i in x:
              if i >5:
                  xg5.append(i)
                  
                  
                  print(x)
                  print(xe) 
                  print(xg5)
    