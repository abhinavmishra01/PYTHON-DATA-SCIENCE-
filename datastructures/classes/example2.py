


class Employee:

# constructor
 def  _init_(self,name,desig,dept,salar,skill=None):
    
        self.name=name
        self.desgination= desig
        self. department= dept    
        self. salary= salary
        self. skills = skills
        
        def do_task(self,task):
            


def info(self):
 print("Employee details")
print(f'name: {self.name}')
print(f'Department:{self.department}')
print(f'Designation:{self.degination}')
print(f'Salary:{self.salary}')
print(f'skills:{",",join(self.skill)}')

def add_skill(self,skillname):
    if self.skills is None:
        self.skills=[skill name]
        
    else:
        self.skills.append(skillname)
        
        e1= Employee('Raj', 'Assitant 2','Sales',40000,['Talking'])
        e2= Employee('Sonu', 'Staff Officer','Finance', 70000, ['management'])
         
        e1.info()
        e2.info()
        e1.do_task("Making some sales")
        e2.do_task('Firing employee')               