class cat:
    
    # attributes, fields,class members, propreties
    color ='black'
    breed =' persian'
    age= 2
    # methods functions
    def eat(self):
        print('cat is eating ')
        
    def eat (self):
           print ('cat is playing')
    def description (self):
        
        print(f'cat is {self.age} years old')
        print(f'cat is {self.color} in color')
        print(f'cat is {self, bread} bread ')
        
        # object
        tom= cat()# to call the constructor the class
        
        tom.eat()
        tom.play()
        tom.description()
        
        tom.age=3
        tom.bread='streat  cat' 
        tom.color= 'grey'      
       
    print("color",tom.color)
    print("age",tom.age)
       
    tom.description()
       
        
    