class Yin: pass
class Yang: 
    def __del__(self): 
        print("Yang destruido") 
 
yin = Yin() 
yang = Yang()
 

#esto es main
print(yang) 

del(yang)

print("?") 

#Yang destruido

#He eliminado la variable ying.yan porque en el print (yang is yin.yang) se está repitiendo lo mismo dos veces, ya que anteriormente se ha puesto "yin.yang = yang" y "print(yang)" 