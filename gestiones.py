
from funciones import *

class peliculas:
    
    def __init__(self, nombrePelicula, actores, anoPelicula, generoPelicula):
        self.nombrePelicula = nombrePelicula
        self.actores = actores
        self.anoPelicula = anoPelicula
        self.generoPelicula = generoPelicula


    # Metodos Get
    def get_pelicula(self):
        return self.nombrePelicula
    
    def get_actores(self):
        return self.actores
    
    def get_anoPelicula(self):
        return self.anoPelicula
    
    def get_generoPelicula(self):
        return self.generoPelicula
    
    
    # Metodos SET
    def set_pelicula(self, nombrePelicula):
        self.nombrePelicula = nombrePelicula
    
    def set_actores(self, actores):
        self.actores = actores
    
    def set_anoPelicula(self, anoPelicula):
        self.anoPelicula = anoPelicula

    def set_generoPelicula(self, generoPelicula):
        self.generoPelicula = generoPelicula


## posiblemente pasar esto hacia main
def cargaDeArchivo(lista):

    # Se abre el archivo para poder unicamente leerlo
    ruta = input("Ingrese la ruta ABASOLUTA del arhivo: ")
    archivo = open(ruta, "r")
    lineas = archivo.readlines()

    repetido = False
    contadorRepetidos= 0
    contadorNoRepetidos = 0
    
    for i in lineas:
        # Se utiliza el ; para separar cada dato
        i = i.split(";")
        contador = 0

        # Variablesl temporales que seran de ayuda para guardar cada dato de la linea en la clase peliculas
        temporal_nombrePelicula = None
        temporal_actores = None
        temporal_anoPelicula = None
        temporal_generoPelicula = None

        # Recorre cada objeto separado en cada linea
        for x in i:               
            
            # Guarda el valor de x sin espacios adelante o atras y sin saltos de linea
            sinEspacios = x.strip()

            match contador:
                
                case 0:
                    temporal_nombrePelicula = sinEspacios
                    

                case 1:
                    #x = x.split(",")
                    sinEspacios = sinEspacios.split(",")
                    temporal_actores = sinEspacios
                    

                case 2:
                    temporal_anoPelicula = sinEspacios

                case 3:
                    temporal_generoPelicula = sinEspacios
  
            contador += 1

       

        for y in lista:
            if y.get_pelicula() == temporal_nombrePelicula:

                lista[lista.index(y)].set_pelicula(temporal_nombrePelicula)
                lista[lista.index(y)].set_actores(temporal_actores)
                lista[lista.index(y)].set_anoPelicula(temporal_anoPelicula)
                lista[lista.index(y)].set_generoPelicula(temporal_generoPelicula)
                repetido = True
                contadorRepetidos += 1


                     
        if repetido == False:

            # Hace uso de la clase peliculas y agrega los atributos       
            datos = peliculas(temporal_nombrePelicula, temporal_actores, temporal_anoPelicula ,temporal_generoPelicula) 
            
            # Agrega al final de la lista los datos
            lista.append(datos)
            contadorNoRepetidos += 1
            

        repetido = False

    # Muestra en pantalla los elementos cargados o repetidos
    if contadorRepetidos > 0:
        print("\nSe han econtrado " + str(contadorRepetidos) + 
              " repetidos. y se cargaron " + str(contadorNoRepetidos) + 
              " elementos correctamente")
        
    else:
        print("\nSe cargaron " + str(contadorNoRepetidos) + 
              " elementos orrectamente")

    archivo.close()
    
        





