import os

def graficarGrafo(listaDePeliculas, listaTemp_Actores):

    
    grafo_dot = open("grafos.dot", "w")
    grafo_dot.write('digraph { \n')
    grafo_dot.write('rankdir = LR \n' )
    grafo_dot.write('node[shape=record, fontname="Arial", fontsize=15] \n')

    # Cambia el diseño para cada uno de los nodos actores
    # recorre la lista temporal en la que se guarda cada 1 de los actores en memoria
    for i in listaTemp_Actores:
        grafo_dot.write('actor' + str(listaTemp_Actores.index(i)) + '[color = black, fillcolor = olivedrab2, style = filled, label="'+ i + '"]\n')

    grafo_dot.write('\n\n')

    # Cambia el diseño para las peliculas, y agrega la informacion necesaria, como el genero y año
    for j in listaDePeliculas:
        grafo_dot.write('peli' + str(listaDePeliculas.index(j)) + '[color = black, fillcolor = orange, style = filled, label="' + j.get_pelicula() + 
                        ' | { ' + j.get_anoPelicula() + ' | ' + j.get_generoPelicula() + '}"]\n')

    grafo_dot.write('\n\n')


    """
    Los actores pueden existir en varias peliculas, pero es importante que en la creacion de los nodos
    tanto las peliculas como los actores aparezcan una sola vez, para que se cree de manera correcta las conexiones
    entre peliculas y actores

    Por lo explicado anteriormente, se hace uno de la lista de actores, luego se recorre la lista de peliculas, y 
    un ultimo bucle en la lista de actores que posee cada pelicula, en caso de que se encuente una coincidencia, 
    entre la lista de actores con la lista de actores presente en la lista de peliculas, agregara el nodo
    de la pelicula y el actor
    """
    for x in listaTemp_Actores:
        for y in listaDePeliculas:
            for z in y.get_actores():

                if z.strip() == x:
                    grafo_dot.write("peli" + str(listaDePeliculas.index(y)) + '->' + "actor"+ str(listaTemp_Actores.index(x)) + '\n')

            
    grafo_dot.write("} \n")
    grafo_dot.close()


    os.system("dot.exe -Tpdf grafos.dot -o  Reporte.pdf")




    