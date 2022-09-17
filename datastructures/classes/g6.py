
import pgzrun


Width=300
Height=500
Speed=3

class player(Actor):
    def move(self):
        if keyword.left:
            self.x-=speed
            
        if keyword.right:
            self.x+= speed
        if keyword.up:
            self.x -= speed
            
        if keyword.down:
            self.y += speed
            
            
    def boundry_check(self):
        if self.x>Width:
            self.x=0
        if self.x<0:
            self.x=Width
        if self.y>Height:       
           self.y=0
        if self.y<0:
            self.y=Height           
            
            self.y-= speed
            if keyword.down:
             self.y+=speed    
            
            def boundary_check(self):
                
                if self.x> Width:
                    self.x=0
                if self.x<0:
                   self.x= Width
                if self.y> Height:
                   self.y=0
                if self.y<0:
                    self.y=Height
                    
p = player('character_001',pos =(200,100))

def   draw():
      screensize.clear()
      p.draw()
def update():
    p.move()
    p.boundary_check()
    
    pgzrun.go()
                                              
   