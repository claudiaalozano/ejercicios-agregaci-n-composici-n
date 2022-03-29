class Yin: pass
class Yang: 
    def __del__(self): 
        print("Yang destruido") 
 
yin = Yin() 
yang = Yang() 
yin.yang = yang 
 
print(yang) 

#esto es main
print(yang is yin.yang) 
True  
del(yang)
print("?") 


#Yang destruido