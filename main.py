from gestiones import *
from funciones import *
import os


listaDePeliculas = []


print("""
╔═════════════════════════════════════════════════╗
║                   BIENVENIDO...                 ║                                                
╚═════════════════════════════════════════════════╝

Presione enter para continuar...
""")
input()

opcion = 0

# Repetite esto hasta que encuentre un brake
while opcion != 5:
    #Limpiar la pantalla
    os.system ("cls") 
    submenu = 0

    print("------------------   MENU   ------------------\n")
    print("""
    1.  Cargar archivo de entrada
    2.  Gestionar películas
    3.  Filtrado
    4.  Gráfica
    5.  Salir
    """)
    opcion = int(input("\n Ingrese el numero de la opcion y presione enter: "))

    match opcion:

        # Caraga de archivos a memoria
        case 1:
            os.system ("cls") 
            print("------------   CARGAR ARCHIVO DE ENTRADA   ------------ \n\n")
            cargaDeArchivo(listaDePeliculas)
            input()

        # Muestra de datos
        case 2:

            os.system ("cls") 

            while True:
                   
                print("------------   GESTION DE PELICULAS   ------------ \n\n")
                print(" 1.  Mostrar películas \n 2.  Mostrar actores \n 3.  Mostar cantidad de peliculas en memoria  \n 4.  Salir ")
                submenu = int(input("\n Ingrese el numero de la opcion y presione enter: "))
                

                match submenu:
                    
                    
                    # Muestra de todos los datos de la pelicula
                    case 1:
                        os.system ("cls") 
                        # Recorre la lista entera de peliculas para imprimir los datos de cada una
                        for x in listaDePeliculas:
                              print("\nNombre del la Pelicula: ", x.get_pelicula(), 
                                    "\nActores: ", x.get_actores() ,"\nAño de Estreno: ", 
                                    x.get_anoPelicula() ,"\nGenero de la Pelicula: ", 
                                    x.get_generoPelicula())


                    # Muestra de datos, Actores de pelicula
                    case 2:
                        os.system ("cls") 
                        contador = 1
                        
                        # Muestra las peliculas disponibles para que el usuario ingrese de que pelicula quiere conocer los actores
                        for x in listaDePeliculas:
                            print(str(contador) + ". ", x.get_pelicula())
                            contador += 1

                        opcionActores = int(input("\nSelecciona de que Pelicula deseas ver los actores: "))
                        
                        contador = 1

                        print("\nActores en la pelicula " + str(listaDePeliculas[opcionActores-1].get_pelicula()) + ":")

                        # Recorre la lista de actores y los muestra de una manera agradable
                        for x in listaDePeliculas[opcionActores-1].get_actores():
                            print("Actor", str(contador) + ": ", x.strip())
                            contador += 1

                    
                    case 3:
                        os.system ("cls") 
                        print("Existen " + str(len(listaDePeliculas)) + " elementos cargados en memoria ahora mismo :)")
                        

                    case 4:
                        break

                input()


        # Opciones de Filtrado
        case 3:

            os.system ("cls") 

            while True:

                print("------------   FILTRADO   ------------ \n\n")
                print(" 1.  Filtrado por actor \n 2.  Filtrado por año \n 3.  Filtrado por género \n 4.  Salir")
                submenu = int(input("\n Ingrese el numero de la opcion y presione enter: "))

                match submenu:

                    # Filtrado por actor
                    case 1:
                        os.system("cls") 
                        contador = 1
                        find = False
                        listaDeActores = []
                        listaTemp_Peliculas = []


                        # Llama a la funcion actores que guarda en una lista todos los actores presentes en memoria
                        actores(listaDePeliculas, listaDeActores)

                        imprimirFiltrado(listaDeActores, contador)

                        # Guarda el nombre del actor
                        actor  = int(input("\nIngrese la opcion que desea ver: "))
                        actor = listaDeActores[actor-1]

                        peliculas(listaDePeliculas, listaTemp_Peliculas, actor)

                        contador = 1
                        for x in listaTemp_Peliculas:


                            # compora si el actor que se busca esta en la lista de actores 
                            # por consiguiente imprime la pelicula donde es parte el actor
                            if contador == 1:
                                print(actor, "aparece en las siguientes peliculas: \n")
                                print(str(contador) + ".",  x)
                                contador += 1
                                find = True

                            elif contador > 1:
                                print(str(contador) + ".", x)
                                contador += 1
                                find = True
                        
                        if find == False:
                            print("\nNo se a encotrado ninguna pelicula donde participe:", actor)




                    # Filtrado por año
                    case 2:
                        os.system ("cls") 
                        contador = 1
                        find = False

                        listaTemp_Year = []
                        listaTemp_Peliculas = []
                        listaTemp_Genero = []

                        year(listaDePeliculas, listaTemp_Year)

                        imprimirFiltrado(listaTemp_Year, contador)

                        yearOpcion  = int(input("\n Ingrese la opcion del año que desea filtrar: "))
                        yearOpcion = listaTemp_Year[yearOpcion-1]

                        filtradoYear(listaDePeliculas, listaTemp_Peliculas, listaTemp_Genero, yearOpcion)

                        contador = 1
                        # Recorre la lista temporal de peliculas
                        for x in listaTemp_Peliculas:
                            if contador == 1:
                                print("En " + str(yearOpcion) + " se publicaron las siguientes peliculas: \n")
                                print(str(contador) + ". \n", "Pelicula:", x, "\n Genero:", listaTemp_Genero[contador-1], "\n")
                                contador += 1 
                                find = True
                            

                            else:
                                print(str(contador) + ". \n", "Pelicula:", x, "\n Genero:", listaTemp_Genero[contador-1], "\n")
                                contador +=1
                                find = True

                            
                      
                        if find == False:
                            print("\nNo se a encotrado ninguna pelicula de este año:", year)


                    # Filtrado por genero
                    case 3:
                        os.system ("cls")    
                        find = False
                        listaTemp_Genero = []
                        listaTemp_Peliculas = []


                        generoFilt(listaDePeliculas, listaTemp_Genero)

                        contador = 1
                        imprimirFiltrado(listaTemp_Genero, contador)

                        # Guarda el nombre del actor
                        genero  = int(input("\n Ingrese la opcion del genero que desea filtrar: "))
                        genero = listaTemp_Genero[genero-1]

   
                        # Recorre la lista de peliculas 
                        for x in listaDePeliculas:
                                                                    
                            if  x.get_generoPelicula() == genero and contador == 1:
                                print("Se encontraron las siguientes peliculas del genero " + genero + ": \n")
                                print(str(contador) + ".", x.get_pelicula())
                                contador += 1 
                                find = True

                            elif x.get_generoPelicula()   == genero and contador > 1:
                                    print(str(contador) + ".", x.get_pelicula())
                                    contador +=1
                                    find = True
                      
                        if find == False:
                            print("\nNo se a encotrado ninguna pelicula de este genero:", genero)
  

                    case 4:
                        break

                input()
                os.system ("cls")  
                            
          
        case 5:
            break
                
