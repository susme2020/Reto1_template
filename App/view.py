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
        print (' Estas son las mejores peliculas: ')
        iterator = it.newIterator(movies)
        while  it.hasNext(iterator):
            movie = it.next(iterator)
            print ('Titulo: ' + movie['original_title'] + '  Fecha: ' + movie['release_date'] + ' Rating: ' + movie['vote_average'])
    else:
        print ('No se encontraron peliculas')

"""
Menu principal
"""
while True:
    printMenu()
    inputs =input('Seleccione una opción para continuar\n')
    datos_cargados = False

    if int(inputs[0])==1: # 1- Cargar información del reto
        print("Cargando información de los archivos ....")
        catalog = initCatalog ()
        loadData (catalog)
        print ('Peliculas cargadas: ' + str(lt.size(catalog['movies'])))
        print ('Directores cargados: ' + str(lt.size(catalog['directors'])))
        print ('Géneros cargados: ' + str(lt.size(catalog['genres'])))
        datos_cargados = True

    elif int(inputs[0])==2: # 2- Películas con buena votacion (≥6) por Director
        if not datos_cargados:
            print("Debe cargar los datos primero")
        else:
            a = 1

    elif int(inputs[0])==3: # 3- Películas con mejores votaciones (mejor promedio de votos)
        if not datos_cargados:
            print("Debe cargar los datos primero")
        else:
            a = 1

    elif int(inputs[0])==4: # 4- Las x películas con peores votaciones (peor promedio de votos)
        if not datos_cargados:
            print("Debe cargar los datos primero")
        else:
            label = input ("Nombre del Actor a buscar: ")

    elif int(inputs[0])==5: # 5- Películas con mayor número de votos
        if not datos_cargados:
            print("Debe cargar los datos primero")
        else:
            a = 1

    elif int(inputs[0])==6: # 6- Las x películas con menor número de votos
        if not datos_cargados:
            print("Debe cargar los datos primero")
        else:
            a = 1

    elif int(inputs[0])==7: # 7- Películas por Director
        if not datos_cargados:
            print("Debe cargar los datos primero")
        else:
            dir_name = input("Nombre del director a buscar: ")
            movies = controller.getMoviesByDirector (catalog, dir_name)
            print(movies)
    
    elif int(inputs[0])==8: # 8- Películas por Actor
        if not datos_cargados:
            print("Debe cargar los datos primero")
        else:
            a = 1

    elif int(inputs[0])==9: # 9- Películas por Género
        if not datos_cargados:
            print("Debe cargar los datos primero")
        else:
            a = 1

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