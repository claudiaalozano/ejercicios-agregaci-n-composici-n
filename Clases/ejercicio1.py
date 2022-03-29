import os

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

class edificio:
    
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

class personas:

    def __init__(self, YooHoo):
        self.YooHoo = YooHoo

    def set.YooHoo (self):
        if seleccion_ciudad == "L.A" or seleccion_ciudad == "N.Y":
            print("Se han destruido los edificios de la ciudad: " , seleccion_ciudad)
    


seleccion_ciudad = input("Seleccione la ciudad que desea eliminar (L.A/ N.Y): ")
