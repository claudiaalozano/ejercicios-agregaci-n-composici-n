# ejercicios-agregaci-n-composici-n

Mi dirección de GitHub: https://github.com/claudiaalozano/ejercicios-agregaci-n-composici-n.git

## a. El día siguiente
Enunciado: modelar lo siguiente. Una empresa es propietaria de varios edificios y emplea a varios empleados. Un edificio está necesariamente ubicado en una ciudad y una ciudad está formada por varios edificios. Empresa, empleado, ciudad y edificio tienen cada uno un nombre. Estas ciudades incluyen New York, donde se encuentran los edificios A y B, y Los Ángeles, donde está el edificio C. Estos tres edificios son propiedad de YooHoo! que emplea a los Sres. Martin, Salim y la Sra. Xing.

Una vez definidas estas entidades, imagine que su programa es una película estadounidense de catástrofes, en la que se destruye New York. Implemente este evento para que todas las entidades del juego tengan en cuenta las consecuencias de este cataclismo.
```import os

class ciudad:
    def __init__(self, newyork, angeles):
        self.newyork = newyork
        self.angeles = angeles
    def set_Newyork (self, newyork, seleccion_ciudad):
        if seleccion_ciudad == "NY":
            print("Se ha eliminado New York.")
            del(newyork)
    def get_newyork (self):
        print( set.newyork)


    def set_angeles (self, angeles, seleccion_ciudad):
        
        if seleccion_ciudad == "L.A":
            print("Se ha eliminado Los Angeles.")
            del(angeles)
    def get_angeles(self):
        print(set.angeles)

class edificio(ciudad):
    
    def __init__(self , ab , c):
        self.a_b = ab
        self.c = c
    def set_ab(self,newyork):
        if seleccion_ciudad == "N.W":
            del(ab)
            print("Con la caída de N.W, se ha destruído el edificio A y el B.")
    
    def get_ab(self): 
        print(set.ab)

    def set_c (self,angeles):
        if seleccion_ciudad == "L.A" :
            del(c)
            print("Con la caída de Los Ángeles, se ha destruido el edificio C.")
    def get_c (self):
        print(set.c)

class personas(ciudad):

    def __init__(self, YooHoo):
        self.YooHoo= YooHoo

    def set_YooHoo (self, seleccion_ciudad):
        if seleccion_ciudad == "L.A":
            print("Se han destruido los edificios de la ciudad: " , seleccion_ciudad)
        else:
            print("Se han destruido los edificios de la ciudad: " , seleccion_ciudad)

    


seleccion_ciudad = input("Seleccione la ciudad que desea eliminar (L.A/ N.Y): ")
```

## b. ¿Inmortal?
Enunciado: Teniendo en cuenta el siguiente código, explique por qué el mensaje Yang destruido, se muestra después del signo de interrogación. ¿Qué hay que hacer para que aparezca antes?
```class Yin: pass
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
```

## c. Alternativa a la herencia múltiple
En el último ejercicio de la sección sobre la herencia, se mostraron los límites de la herencia múltiple: acoplamientos de clases cuyo vínculo no es tan obvio, atajos tomados en el código que tienen mucho riesgo de error. Este ejercicio utiliza otro enfoque del problema: la asociación (ya sea composición o agregación). 

Enunciado: comenzando con el mismo código que el ejercicio sobre herencia múltiple, cree una clase que agrupe el comportamiento común entre las clases Ventana y ParedCortina.

Enunciado: modifique las clases Ventana y ParedCortina para que usen esta nueva clase-interfaz Cristal.

Enunciado: modifique el código para que el programa funcione de nuevo.
```
class Cristal: #clase padre
    pass

class Pared(Cristal): #clase hija
    #Constructor
    def __init__(self, orientacion):
        self.orientacion = orientacion
        
class Ventana(Cristal): #clase hija
    #Constructor
    def __init__(self, orientacion, superficie):
        super().__init__(orientacion)
        self.superficie = superficie
    
    def get_area(self):
        return self.superficie

class Casa(Cristal): #clase hija
    #Constructor
    def __init__(self, paredes, orientacion, superficie):
        super().__init__(orientacion, superficie)
        self.paredes = paredes
    
    def superficie_acristalada(self):
        return sum(self.paredes.superficie)



pared_norte = Pared("NORTE") 
pared_oeste = Pared("OESTE") 
pared_sur = Pared("SUR") 
pared_este = Pared("ESTE") 
    # Instanciación de las ventanas 
ventana_norte = Ventana(pared_norte, 0.5) 
ventana_oeste = Ventana(pared_oeste, 1) 
ventana_sur = Ventana(pared_sur, 2) 
ventana_este = Ventana(pared_este, 1) 
    # Instanciación de la casa con las 4 paredes 
casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este]) 
    #print(casa.superficie_acristalada()) 
```
