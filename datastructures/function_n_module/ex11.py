# keywords arguments - kwargs

def saveinfo(file='info.txt',**kwargs):
    with open(file,'a')as f:
        
        for k,v in kwargs.items():
        
            f.write(f'{k}->{v}\n')
            
        
            
saveinfo(mobile='VivoT15G', price=25000,
            expiry='2023', feature='kuch khas nhi')