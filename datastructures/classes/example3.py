


class fruit:
    def _init_(self,name,color):
        self.name=name
        self.color=color
        
        def info(self):
            print("FRUIT")
            print(f'{self.name}')
            print(f'{self.color}')
            
            
            class mango(fruits):
                
                def _init_(self,name,color,taste,size):
                     
                       
                   super()._init_(name,color)
                self.taste=taste
                self.size=size
                
                f=fruits('orange','orange')
                m=fruits('daseri mango','greenish mango','sweet', 'medium')
                
                f.info()
                m.info()
                     