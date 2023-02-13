

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
    
    def set_pelicula(self, actores):
        self.actores = actores
    
    def set_pelicula(self, anoPelicula):
        self.anoPelicula = anoPelicula

    def set_pelicula(self, generoPelicula):
        self.generoPelicula = generoPelicula


## posiblemente pasar esto hacia main
def cargaDeArchivo(lista):

    # Se abre el archivo para poder unicamente leerlo
    ruta = input("Ingrese la ruta ABASOLUTA del arhivo: ")
    archivo = open(ruta, "r")
    lineas = archivo.readlines()

    
    for i in lineas:
        # Se utiliza el ; para separar cada dato
        i = i.split(";")
        contador = 0

        # Variablesl temporales que seran de ayuda para guardar cada dato de la linea en la clase peliculas
        temporal_nombrePelicula = None
        temporal_actores = None
        temporal_anoPelicula = None
        temporal_generoPelicula = None

        # Recorre cada objeto sepado en cada linea
        for x in i:               
                 
            match contador:

                case 0:
                    
                    temporal_nombrePelicula = x

                case 1:
                    x = x.split(",")
                    temporal_actores = x

                case 2:
                    temporal_anoPelicula = x

                case 3:
                    temporal_generoPelicula = x

            contador += 1

        # Hace uso de la clase peliculas y agrega los atributos       
        datos = peliculas(temporal_nombrePelicula, temporal_actores, temporal_anoPelicula ,temporal_generoPelicula) 
        
        # Agrega al final de la lista los datos
        lista.append(datos)


    archivo.close()
    
        





