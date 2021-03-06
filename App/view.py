"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller 
import csv
from ADT import list as lt
from DataStructures import listiterator as it

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones  y  por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("Bienvenido al Reto 1")
    print("1- Cargar información del reto")

    print("--- Requerimiento 1, Buenas películas ---")
    print("2- Películas con buena votacion (≥6) por Director")

    print("--- Requerimiento 2, Votos ---")
    print("3- Películas con mejores votaciones (mejor promedio de votos)")
    print("4- Las x películas con peores votaciones (peor promedio de votos)")
    print("5- Películas con mayor número de votos")
    print("6- Las x películas con menor número de votos")

    print("--- Requerimiento 3, Directores ---")
    print("7- Películas por Director") # debe incluir número de películas y voto promedio

    print("--- Requerimiento 4, Actores ---")
    print("8- Películas por Actor") # debe incluir total de películas, promedio de votos y director que más veces lo ha elegido

    print("--- Requerimiento 5, Géneros ---")
    print("9- Películas por Género") # debe incluir el promedio de votos y cuántas películas tiene asociadas

    print("10- Top x de Películas (por vote_average)")
    print("0- Salir")


def initCatalog ():
    """
    Inicializa el catalogo de peliculas
    """
    return controller.initCatalog()


def loadData (catalog):
    """
    Carga las peliculas en la estructura de datos
    """
    controller.loadData(catalog)

def printBestMovies (movies):
    size = lt.size(movies)
    if size:
        print (' Estas son las mejores películas: ')
        iterator = it.newIterator(movies)
        while  it.hasNext(iterator):
            movie = it.next(iterator)
            print ('Título: ' + movie['original_title'] + '  Fecha: ' + movie['release_date'] + ' Rating: ' + movie['vote_average'])
    else:
        print ('No se encontraron peliculas')

def printMostVotedMovies (movies):
    size = lt.size(movies)
    if size:
        print (' Estas son las películas más votadas: ')
        iterator = it.newIterator(movies)
        while  it.hasNext(iterator):
            movie = it.next(iterator)
            print ('Título: ' + movie['original_title'] + '  Fecha: ' + movie['release_date'] + ' Rating: ' + movie['vote_average'])
    else:
        print ('No se encontraron peliculas')

def printLeastVotedMovies (movies):
    size = lt.size(movies)
    if size:
        print (' Estas son las películas menos votadas: ')
        iterator = it.newIterator(movies)
        while  it.hasNext(iterator):
            movie = it.next(iterator)
            print ('Título: ' + movie['original_title'] + '  Fecha: ' + movie['release_date'] + ' Rating: ' + movie['vote_average'])
    else:
        print ('No se encontraron peliculas')

def printWorstMovies (movies):
    size = lt.size(movies)
    if size:
        print (' Estas son las peores películas: ')
        iterator = it.newIterator(movies)
        while  it.hasNext(iterator):
            movie = it.next(iterator)
            print ('Título: ' + movie['original_title'] + '  Fecha: ' + movie['release_date'] + ' Rating: ' + movie['vote_average'])
    else:
        print ('No se encontraron peliculas')
        

"""
Menu principal
"""
datos_cargados = False
while True:
    printMenu()
    inputs =input('Seleccione una opción para continuar\n')

    if int(inputs[0])==1: # 1- Cargar información del reto
        print("Cargando información de los archivos ....")
        catalog = initCatalog ()
        loadData (catalog)
        print ('Peliculas cargadas: ' + str(lt.size(catalog['movies'])))
        print ('Directores cargados: ' + str(lt.size(catalog['directors'])))
        print ('Actores cargados: ' + str(lt.size(catalog['actors'])))
        print ('Géneros cargados: ' + str(lt.size(catalog['genres'])))
        datos_cargados = True

    elif int(inputs[0])==2: # 2- Películas con buena votacion (≥6) por Director
        if not datos_cargados:
            print("Debe cargar los datos primero")
        else:
            dir_name = input("Nombre del director a buscar: ")
            movies = controller.getMoviesByDirector (catalog, dir_name)[1] # getMoviesByDirector retorna una tupla, el primer dato es el nombre del director y el segundo es su lista de títulos de películas
            if movies[0] == None:
                print("No se pudo encontrar el director que busca :(")
            else:
                tupla = controller.getMoviesByDirector (catalog, dir_name)
                movies = tupla[1]
                director = tupla[0]
                print(director, "dirigió ", lt.size(movies), " películas con promedio mayor o igual a 6\nTales peículas son las siguientes:\n")
                for movie in movies:
                    print(movie)

    elif int(inputs[0])==3: # 3- Películas con mejores votaciones (mejor promedio de votos)
        if not datos_cargados:
            print("Debe cargar los datos primero")
        else:
            number = input ("Buscando las TOP ?: ")
            movies = controller.getBestMovies (catalog, int(number))
            printBestMovies (movies)

    elif int(inputs[0])==4: # 4- Las x películas con peores votaciones (peor promedio de votos)
        if not datos_cargados:
            print("Debe cargar los datos primero")
        else:
            number = input ("Buscando las TOP ?: ")
            movies = controller.getWorstMovies (catalog, int(number))
            printWorstMovies (movies)

    elif int(inputs[0])==5: # 5- Películas con mayor número de votos
        if not datos_cargados:
            print("Debe cargar los datos primero")
        else:
            number = input ("Buscando las TOP ?: ")
            movies = controller.getMostVotedMovies (catalog, int(number))
            printMostVotedMovies(movies)

    elif int(inputs[0])==6: # 6- Las x películas con menor número de votos
        if not datos_cargados:
            print("Debe cargar los datos primero")
        else:
            number = input ("Buscando las TOP ?: ")
            movies = controller.getLeastVotedMovies (catalog, int(number))
            printLeastVotedMovies(movies)

    elif int(inputs[0])==7: # 7- Películas por Director
        if not datos_cargados:
            print("Debe cargar los datos primero")
        else:
            dir_name = input("Nombre del director a buscar: ")
            tupla = controller.getMoviesByDirector (catalog, dir_name)
            movies = tupla[1]
            director = tupla[0]
            print(director, " dirigió ", lt.size(movies), " películas con los siguientes títulos: \n")
            for movie in movies:
                print(movie)
    
    elif int(inputs[0])==8: # 8- Películas por Actor
        if not datos_cargados:
            print("Debe cargar los datos primero")
        else:
            act_name = input("Nombre del actor a buscar: ")
            tupla = controller.getMoviesByActor (catalog, act_name)
            movies = tupla[1]
            actor = tupla[0]
            print(actor, " actuó en ", lt.size(movies), " películas con los siguientes títulos: \n")
            for movie in movies:
                print(movie)

    elif int(inputs[0])==9: # 9- Películas por Género
        if not datos_cargados:
            print("Debe cargar los datos primero")
        else:
            gen_name = input("Nombre del género a buscar: ")
            tupla = controller.getMoviesByGenre (catalog, gen_name)
            movies = tupla[1]
            genre = tupla[0]
            print("Hay ", lt.size(movies), " películas del género de ", genre, "\nTítulos: \n")
            for movie in movies:
                print(movie)

    elif int(inputs[0])==10: # 10- Top x de Películas
        if not datos_cargados:
                print("Debe cargar los datos primero")
        else:
            number = input ("Buscando las TOP ?: ")
            movies = controller.getBestMovies (catalog, int(number))
            printBestMovies (movies)

    else:
        sys.exit(0)
sys.exit(0)