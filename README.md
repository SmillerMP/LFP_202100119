[![Github - SmillerMP](https://img.shields.io/badge/Github-SmillerMP-2ea44f)](https://github.com/SmillerMP)

# Datos

| Carnet | 202100119|
| ------ | ------ |
| Estudiante |Samuel Isaí Muñoz Pererira|
| Auxiliar | Pablo Daniel Rivas Marroquín|

#

# Manual de Usuario

## Menu Principal

- Carga de Archivos
- Gestion de Peliculas
- Filtrado
- Grafica
- Salir


#



## Regla General
Nunca sera necesario introducir texto a menos que se lo pida el programa, como la direccion para cargar el archivo, el programa esta diseñado para mostrar las opciones con numeros y que el usuario introduzca el numero de la opcion a usar o elegir.

Sera necesario pulsar la tecla ENTER varias veces durante el uso del programa, normalmente el programa pedira que realice esta operacion.

#

## 1. Carga de Archivos
Esta opcion permite cargar la URL o direccion absoluta del archivo, es importante que el archivo de entrada contenga el siguienete formato

```sh
nombre de la pelicula;actor1,actor2,actor3...;año de publicacion;genero de la pelicula
```

es recomendable que el archivo no contenga espacios entre las comas y punto y coma.Resaltar que es importante introducir la direccion absoluta del archivo, no la direccion relativa. Ya que puede ser que algunas veces no detecte correctamente la direccion relativa

#

## 2. Gestion de Peliculas
Se tienen los siguientes submenus:

1. Mostrar Peliculas: muestra todas las peliculas cargadas en memoria, juntos con su informacion adicional, actores, fecha de publicacion y genero.

2. Mostar Actores: genera una lista de todas las peliculas disponibles, el usuario debe ingresar el numero de la opcion que desea visualizar.

3. Mostrar cantidad de peliculas en memoria: muestra el numero de peliculas cargadas en memorias.

4. Salir: regresa al menu principal.

![Gestion](\Capturas\gestionPeliculas.png)

#

## 3. Filtrado
Se tienen los siguientes submenus:

1. Filtrado por Actor: muestra una lista de todos los actores en memoria, el usuario debe ingresa la opcion que desea visualizar y el programa devolvera una lista de peliculas donde participa el actor seleccionado.

2. Filtrado por Año: se muestra una lista de todos los años ordenada de manera ascendente, el usuario debe seleccionar la opcion y el programa devolvera las peliculas y el tipo de genero de estas, del año seleccionado.

3. Filtrado: Filtrado por Genero: muestra una lista de todos los generos disponibles cargados en memoria, el usuario selecciona el genero que desea visualizar, y el programa devuelve las peliculas del genero seleccionado.

4. Salir: regresa al menu principal.

![Filtrado](\Capturas\filtrado.png)

#

## 4. Grafica
Genera un archivo.dot en el cual sea crean todos los nodos entre los actores presentes en cada pelicula, y la pelicula y su informacion, no es necesario cargar otro archivo o direccion, ya que toda la informacion necesaria la toma desde la memoria que se cargo inicialmente en el programa.
El archivo final se crea en formato pdf con el nombre Reporte.

![Grafo](\Capturas\grafo.png)

#

## 5. Salir
Agradece el uso del programa :D

#


