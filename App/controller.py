'''
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
 '''

import config as cf
import model
import csv
from ADT import list as lt
from DataStructures import listiterator as it
from Sorting import mergesort as sort
from time import process_time 


'''
El controlador se encarga de mediar entre la vista y el modelo.
'''


# Funcionaes utilitarias

def printList (lst):
    iterator = it.newIterator(lst)
    while  it.hasNext(iterator):
        element = it.next(iterator)
        result = ''.join(str(key) + ': ' + str(value) + ',  ' for key, value in element.items())
        print (result)

def compareratings (movie1, movie2):
    return ( float(movie1['vote_average']) > float(movie2['vote_average']))

def equal(nombre_elemento, elemento):
    return (nombre_elemento == elemento['name'])

def less_by_subelement_count(elemento1, elemento2):
    return (elemento1['vote_count'] < elemento2['vote_count'])

def less_by_subelement_average(elemento1, elemento2):
    return (elemento1['vote_average'] < elemento2['vote_average'])

# Funciones para la carga de datos 

def loadMovies (catalog):
    '''
    Carga las peliculas del archivo.  Por cada libro se cargan sus directores
    
    '''
    t1_start = process_time() #tiempo inicial
    moviesfile = cf.data_dir + 'themoviesdb/SmallMoviesDetailsCleaned.csv'
    
    dialect = csv.excel()
    dialect.delimiter=';'
    with open(moviesfile, encoding='utf-8') as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        for row in spamreader: 
            lt.addLast (catalog['movies'], row)
    t1_stop = process_time() #tiempo final
    print('Tiempo de ejecución carga peliculas',t1_stop-t1_start,' segundos')



def loadDirectors(catalog):
    '''
    Carga todos los directores
    '''
    t1_start = process_time() #tiempo inicial
    castingfile = cf.data_dir + 'themoviesdb/MoviesCastingRaw-small.csv'
    
    dialect = csv.excel()
    dialect.delimiter=';'
    with open(castingfile, encoding='utf-8') as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        movie_counter = 1
        for row in spamreader:
            director_name = row['director_name']
            pos = lt.isPresent(director_name, catalog['directors'], equal)
            if pos != 0:
                model.updateDirector(catalog, pos, movie_counter)
            else:
                model.addDirector(catalog, row, movie_counter)
            movie_counter += 1
    t1_stop = process_time() #tiempo inicial
    print('Tiempo de ejecución carga directores',t1_stop-t1_start,' segundos')
    model.endDirectorslist(catalog['directors'])


def loadActors(catalog):
    '''
    Carga todos los actores
    '''
    t1_start = process_time() #tiempo inicial
    castingfile = cf.data_dir + 'themoviesdb/MoviesCastingRaw-small.csv'
    
    dialect = csv.excel()
    dialect.delimiter=';'
    with open(castingfile, encoding='utf-8') as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        movie_counter = 1
        casting = ['actor1_name', 'actor2_name', 'actor3_name', 'actor4_name', 'actor5_name']
        for row in spamreader:
            for actor in casting:
                actor_name = row[actor]
                if not actor_name == 'none':
                    director_name = row['director_name']
                    pos = lt.isPresent(actor_name, catalog['actors'], equal)
                    if pos != 0:
                        model.updateActor(catalog, pos, movie_counter, director_name)
                    else:
                        model.addActor(catalog, row, movie_counter)
            movie_counter += 1
    t1_stop = process_time() #tiempo inicial
    print('Tiempo de ejecución carga actores',t1_stop-t1_start,' segundos')
    endActorslist_controller(catalog)

def loadGenres (catalog):
    '''
    Carga el catálogo de géneros del archivo. Por cada género se cargan sus libros
    
    '''
    t1_start = process_time() #tiempo inicial
    movies = catalog['movies']
    for movie in movies:
        genre_name = movie['genres']
        pos = lt.isPresent(genre_name, catalog['genres'], equal)
        if pos != 0:
            model.updateGenre(catalog, movie, pos)
        else:
            model.addGenre(catalog, movie)
    t1_stop = process_time() #tiempo final
    print('Tiempo de ejecución carga peliculas',t1_stop-t1_start,' segundos')
    endGenreslist_controller(catalog)

def initCatalog ():
    '''
    Llama la funcion de inicializacion del catalogo del modelo.
    '''
    catalog = model.newCatalog()
    return catalog



def loadData (catalog):
    '''
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    '''
    loadMovies(catalog)
    loadDirectors(catalog)
    loadActors(catalog)
    loadGenres(catalog)
    sortMovies(catalog)
    

# Funciones llamadas desde la vista y enviadas al modelo

def getMoviesByDirector(catalog, dir_name):
    return model.getMoviesByDirector(catalog, dir_name)

def getMoviesByActor(catalog, act_name):
    return model.getMoviesByActor(catalog, act_name)

def getMoviesByGenre(catalog, gen_name):
    return model.getMoviesByGenre(catalog, gen_name)

def getBestMovies(catalog, number):
    movies = catalog['movies_by_vote_average']
    bestmovies = lt.newList()
    for cont in range (1, number+1):
        movie = lt.getElement (movies, cont)
        lt.addLast (bestmovies, movie)
    return bestmovies

def getMostVotedMovies(catalog, number):
    movies = catalog['movies_by_vote_count']
    mostvotedmovies = lt.newList()
    for cont in range (1, number+1):
        movie = lt.getElement (movies, cont)
        lt.addLast (mostvotedmovies, movie)
    return mostvotedmovies

def getLeastVotedMovies(catalog, number):
    movies = catalog['movies_by_vote_count']
    leastvotedmovies = lt.newList()
    for cont in range (1, number+1):
        movie = lt.getElement (movies, cont)
        lt.addLast (leastvotedmovies, movie)
    return leastvotedmovies

def getWorstMovies(catalog, number):
    movies = catalog['movies_by_vote_average']
    size = lt.size(movies)
    worstmovies = lt.newList()
    for cont in range(size+1, size+1-number, -1):
        movie = lt.getElement (movies, cont)
        lt.addLast (worstmovies, movie)
    return worstmovies

def getBestMoviesByDirector(catalog, director_movies):
    return model.getBestMoviesByDirector(catalog, director_movies)

def find_most_times_director(actor):
    directores = actor['directors']
    mayor = 0
    director_mayor = None
    for director in directores:
        veces_director = directores[director]['count']
        if veces_director > mayor:
            mayor = veces_director
            director_mayor = directores[director]['name']
    if director_mayor != None:
        actor['mas_veces_director'] = {'name': director_mayor, 'count': mayor}
    
def endActorslist_controller(catalog):
    actores = catalog['actores']
    for actor in actores:
        model.endActorslist(actor)
        find_most_times_director(actor)

def endGenreslist_controller(catalog):
    genres = catalog['genres']
    for genre in genres:
        model.endGenreslist(genre)

def sortMovies(catalog):
    sort_by(catalog, less_by_subelement_count, 'movies_by_vote_count')
    sort_by(catalog, less_by_subelement_average, 'movies_by_vote_average')

def sort_by(catalog, compare_function, sub_catalog):
    movies = catalog['movies']
    lista = catalog[sub_catalog]
    iterator = it.newIterator(movies)
    while  it.hasNext(iterator):
        element = it.next(iterator)
        lt.addLast(lista,element)
    sort.sort(lista, compare_function)