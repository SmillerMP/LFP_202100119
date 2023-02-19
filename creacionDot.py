import os

def graficarGrafo(listaDePeliculas, listaTemp_Actores):
    
    grafo_dot = open("grafos.dot","w")
    grafo_dot.write('digraph { \n')
    grafo_dot.write('rankdir = LR \n' )
    grafo_dot.write('node[shape=record, fontname="Arial", fontsize=15] \n')

    for i in listaTemp_Actores:
        grafo_dot.write('actor' + str(listaTemp_Actores.index(i)) + '[color = black, fillcolor = olivedrab2, style = filled, label="'+ i + '"]\n')

    grafo_dot.write('\n\n')

    for j in listaDePeliculas:
        grafo_dot.write('peli' + str(listaDePeliculas.index(j)) + '[color = black, fillcolor = orange, style = filled, label="' + j.get_pelicula() + 
                        ' | { ' + j.get_anoPelicula() + ' | ' + j.get_generoPelicula() + '}"]\n')

    grafo_dot.write('\n\n')

    for x in listaTemp_Actores:
        for y in listaDePeliculas:
            for z in y.get_actores():

                if z.strip() == x:
                    grafo_dot.write("peli" + str(listaDePeliculas.index(y)) + '->' + "actor"+ str(listaTemp_Actores.index(x)) + '\n')

            
    grafo_dot.write("} \n")
    grafo_dot.close()

    os.system("dot.exe -Tpdf grafos.dot -o Grafo.pdf")




    