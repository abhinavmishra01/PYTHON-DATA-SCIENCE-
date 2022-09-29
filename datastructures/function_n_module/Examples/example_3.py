 
data = " " # global variable
 
def data_appender(s):
      global data # this line tell data _appender that we have a global var data 
      if len(s)>0:
          data +=s
          
          # call 
          data_appender('hello')
          data_appender('World')
          data_appender('this is a simple function')
          data_appender('phele istenal kre phir vishwas kre')
          
          
          print(data)