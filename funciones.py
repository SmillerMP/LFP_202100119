
def inicialMayus(texto):
    convertido = texto[0].upper() + texto[1:].lower()
    return convertido




def actores(listaGeneral, listaEspecifica):
    for x in listaGeneral:
        for y in x.get_actores():
            y = y.strip()        
            if listaEspecifica.count(y) == 0:
                listaEspecifica.append(y)

    return listaEspecifica


def peliculasFilt(listaGeneral, listaEspecifica, dato):
    for x in listaGeneral:
        for y in x.get_actores():

            if y.strip() == dato:
                listaEspecifica.append(x.get_pelicula())

    return listaEspecifica


def year(listaGeneral, listaEspecifica):
    for x in listaGeneral:     

        if listaEspecifica.count(x.get_anoPelicula()) == 0:
            listaEspecifica.append(x.get_anoPelicula())

    listaEspecifica = listaEspecifica.sort()

    return listaEspecifica


def filtradoYear(listaGeneral, listaTempPeliculas, listaGenero, year):
    for x in listaGeneral:

        if x.get_anoPelicula() == year:
            listaTempPeliculas.append(x.get_pelicula())
            listaGenero.append(x.get_generoPelicula())

    return listaTempPeliculas, listaGenero



def generoFilt(listaGeneral, listaEspecifica):
    for x in listaGeneral:     

        if listaEspecifica.count(x.get_generoPelicula()) == 0:
            listaEspecifica.append(x.get_generoPelicula())

    return listaEspecifica




def imprimirFiltrado(lista, contador):
    for x in lista:
        print(str(contador) + ". ", x)
        contador += 1