import os

class ciudad:
    seleccion_ciudad = input("Seleccione la ciudad que desea eliminar (L.A/ N.Y)")
    def __init__(self, newyork, angeles):
        self.newyork = newyork
        self.angeles = angeles
    def set_Newyork (self, newyork, seleccion_ciudad):
        self.newyork = newyork
        if seleccion_ciudad == "NY":
            print("Se ha eliminado New York.")
            del(newyork)
    def getNewyork (self):
        print( set.newyork)


    def angeles (self, angeles, seleccion_ciudad):
        self.angeles = angeles
        if seleccion_ciudad == "L.A":
            print("Se ha eliminado Los Angeles.")
        
