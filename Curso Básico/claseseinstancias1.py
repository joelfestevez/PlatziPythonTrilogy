#Este programa da como resultado la distancia entre dos coordenadas
class Coordenada:

	def __init__(self, x, y):  #hasta aquí lo que esta después de self, solo son parametros.
		self.x = x
		self.y = y
		# Aquí estamos inicializando las variables de instancia

    def distancia(self, otra_coordenada):  #el parametro otra_coordenada es una instancia, que hara uso del molde en la primer clase de inicializacion, la cual usaremos despues, tomar atencion.
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2

        return (x_diff +y_diff)**0.5
        #estos solo son una representación matemática de lo que hará el programa (lo explicare después)

#mi caso yo prefiero usar comillas dobles, depende de ustedes.
if __name__ == "__main__": 
    coord_1 = Coordenada(3, 30)
	coord_2 = Coordenada(4, 8)
	#estas dos expresiones son instancias que usan el molde que es el primer método de inicializacion.
    print(coord_1.distancia(coord_2))
    #"coord_1" hace uso de la primer instancia, mientras que coord_2 al estar dentro del metodo distancia, ocupa el lugar de otra_coordenada. (entender esta parte es muy importante)
    #print(isinstance(coord_1, Coordenada)) #Nos ayuda a verificar instancias de la clase