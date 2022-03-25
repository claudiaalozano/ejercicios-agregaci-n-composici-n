import os

class ciudad:
    seleccion_ciudad = input("Seleccione la ciudad que desea eliminar (L.A/ N.Y)")
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
    def __init__(self , a, b , c):
        self.a = a
        self.b = b
        self.c = c
    def set_a(self,newyork):
        if del(newyork):
            del(a)
            

