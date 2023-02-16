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

    print("------------------   MENU   ------------------\n\n")
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
            while True:
                   
                print("------------   GESTION DE PELICULAS   ------------ \n\n")
                print(" 1.  Mostrar películas \n 2.  Mostrar actores \n 3.  Salir ")
                submenu = int(input("\n Ingrese el numero de la opcion y presione enter: "))
                

                match submenu:
                    
                    # Muestra de todos los datos de la pelicula
                    case 1:
                        # Recorre la lista entera de peliculas para imprimir los datos de cada una
                        for x in listaDePeliculas:
                              print("\nNombre del la Pelicula: ", x.get_pelicula(), 
                                    "\nActores: ", x.get_actores() ,"\nAño de Estreno: ", 
                                    x.get_anoPelicula() ,"\nGenero de la Pelicula: ", 
                                    x.get_generoPelicula())


                    # Muestra de datos, Actores de pelicula
                    case 2:
                        contador = 1
                        # Muestra las peliculas disponibles para que el usuario ingrese de que pelicula quiere conocer los actores
                        for x in listaDePeliculas:
                            print(contador, ".  ", x.get_pelicula())
                            contador += 1

                        opcionActores = int(input("\nSelecciona de que Pelicula deseas ver los actores: "))
                        
                        contador = 1
                        # Recorre la lista de actores y los muestra de una manera agradable
                        for x in listaDePeliculas[opcionActores-1].get_actores():
                            print("Actor", str(contador) + ":  ", x)
                            contador += 1
                        

                    case 3:
                        break
      
                input()
        
        case 3:
            while True:

                print("------------   FILTRADO   ------------ \n\n")
                print(" 1.  Filtrado por actor \n 2.  Filtrado por año \n 3.  Filtrado por género \n 4.  Salir")
                submenu = int(input("\n Ingrese el numero de la opcion y presione enter: "))

                match submenu:

                    case 1:
                        contador = 1
                        find = False

                        # Guarda el nombre del actor
                        actor  = str(input("\n Ingrese el nombre del actor que desea buscar: "))

                        # Utiliza la funcion para escribir el nombre del actor correctamente
                        #actor = inicialMayus(actor)
   

                        # Recorre la lista de peliculas
                        for x in listaDePeliculas:

                            # Recorre la lista de acoteres para cada una de las peliculas
                            for y in x.get_actores():

                                # compora si el actor que se busca esta en la lista de actores 
                                # por consiguiente imprime la pelicula donde es parte el actor
                                if y == actor and contador == 1:
                                    print("Aparece en las siguientes peliculas: \n")
                                    print(str(contador) + ".  ", x.get_pelicula())
                                    contador += 1
                                    find = True

                                elif y == actor and contador > 1:
                                    print(str(contador), ".  ", x.get_pelicula())
                                    contador += 1
                                    find = True
                        
                        if find == False:
                            print("\nNo se a encotrado ninguna pelicula donde participe:", actor)


                    # Filtrado por año
                    case 2:
                        contador = 1
                        find = False

                        # Guarda el nombre del actor
                        year  = str(input("\n Ingrese el año que desea filtrar: "))

                        # Recorre la lista de peliculas 
                        for x in listaDePeliculas:

                            if x.get_anoPelicula() == year and contador == 1:
                                print("En " + str(year) + "se publicaron las siguientes peliculas: \n")
                                print(str(contador) + ".  \n", "Pelicula:", x.get_pelicula(), "\n Genero:", x.get_generoPelicula())
                                contador += 1 
                                find = True

                            elif x.get_anoPelicula() == year and contador > 1:
                                    print(str(contador) + ".  \n", "Pelicula:", x.get_pelicula(), "\n Genero:", x.get_generoPelicula())
                                    contador +=1
                                    find = True
                      
                        if find == False:
                            print("\nNo se a encotrado ninguna pelicula de este año:", year)


                    # Filtrado por genero
                    case 3:

                        contador = 1
                        find = False

                        # Guarda el nombre del actor
                        genero  = str(input("\n Ingrese el año que desea filtrar: "))

                        # Recorre la lista de peliculas 
                        for x in listaDePeliculas:
                                                                    
                            if x.get_generoPelicula()  == genero and contador == 1:
                                print("Se encontraron las siguientes peliculas del genero" + genero + ": \n")
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
                            

            
        case 5:
            break
                
