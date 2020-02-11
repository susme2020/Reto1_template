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
from ADT import list as lt
from DataStructures import listiterator as it


"""
Se define la estructura de un catálogo de libros.
El catálogo tendrá tres listas, una para libros, otra para autores 
y otra para géneros
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de peliculas. Retorna el catalogo inicializado.
    """
    catalog = {'movies':None, 'directors':None, 'actors': None, 'movies_by_vote_count': None, 'movies_by_vote_average': None, 'genres': None}
    catalog['movies'] = lt.newList('ARRAY_LIST')
    catalog['directors'] = lt.newList('ARRAY_LIST')
    catalog['actors'] = lt.newList('ARRAY_LIST')
    catalog['movies_by_vote_count'] = lt.newList('ARRAY_LIST')
    catalog['movies_by_vote_average'] = lt.newList('ARRAY_LIST')
    catalog['genres'] = lt.newList('ARRAY_LIST')
    return catalog


def newActor (movie, row):
    """
    Crea una nueva estructura para almacenar los actores de una pelicula 
    """
    actor = {'name':'', 'movies_id':'', 'movie_titles':'', 'movie_count': '', 'movie_average': '', 'directors': {}}
    actor ['name'] = row['director_name']
    actor ['movies_id'] = lt.newList('ARRAY_LIST')
    lt.addLast(actor ['movies_id'], movie['id'])
    actor ['movie_titles'] = lt.newList('ARRAY_LIST')
    lt.addLast(actor['movie_titles'], movie['title'])
    actor ['movie_count'] = 1
    actor ['movie_average'] = movie['vote_average']
    director_name = row['director_name']
    actor['directors'][director_name] = {'name': director_name, 'count': 1}
    return actor

def updateActor(catalog, pos_actor, pos_movie, director):
    """
    Actualiza la lista de actores
    """
    movie = catalog['movies'][pos_movie]
    actor = catalog['actors'][pos_actor]
    lt.addLast(actor['movies_id'], movie['id'])
    lt.addLast(actor['movie_titles'], movie['title'])
    actor['movie_count'] += 1
    actor['movie_average'] += movie['vote_average']
    directores_por_actor = actor['directors']
    existe = directores_por_actor.get(director)
    if existe != None:
        existe['count'] += 1
    else:
        directores_por_actor[director] = {'name': director, 'count': 1}

def addActor (catalog, row, pos_movie):
    """
    Adiciona un actor a la lista de actores
    """
    movie = catalog['movies'][pos_movie]
    a = newActor(movie, row)
    lt.addLast(catalog['actors'], a)

def newDirector (movie, row):
    """
    Esta estructura almancena los directores de una pelicula.
    """
    director = {'name':'', 'movies_id':'', 'movie_titles':'', 'movie_count': '', 'movie_average': ''}
    director ['name'] = row['director_name']
    director ['movies_id'] = lt.newList('ARRAY_LIST')
    lt.addLast(director ['movies_id'], movie['id'])
    director ['movie_titles'] = lt.newList('ARRAY_LIST')
    lt.addLast(director['movie_titles'], movie['title'])
    director ['movie_count'] = 1
    director ['movie_average'] = movie['vote_average']
    return director

def updateDirector(catalog, pos_director, pos_movie):
    """
    Actualiza la lista de directores
    """
    movie = catalog['movies'][pos_movie]
    director = catalog['directors'][pos_director]
    lt.addLast(director['movies_id'], movie['id'])
    lt.addLast(director['movie_titles'], movie['title'])
    director['movie_count'] += 1
    director['movie_average'] += movie['vote_average']

def addDirector (catalog, row, pos_movie):
    """
    Adiciona un director a la lista de directores
    """
    movie = catalog['movies'][pos_movie]
    d = newDirector(movie, row)
    lt.addLast(catalog['directors'], d)

def newGenre (movie, row):
    """
    Crea una nueva estructura para almacenar los géneros de películas
    """
    genre = {'name':'', 'movies_id':'', 'movie_titles':'', 'movie_count': '', 'movie_average': ''}
    genre ['name'] = row['director_name']
    genre ['movies_id'] = lt.newList('ARRAY_LIST')
    lt.addLast(genre ['movies_id'], movie['id'])
    genre ['movie_titles'] = lt.newList('ARRAY_LIST')
    lt.addLast(genre['movie_titles'], movie['title'])
    genre ['movie_count'] = 1
    genre ['movie_average'] = movie['vote_average']
    return genre

def updateGenre(catalog, pos_actor, pos_movie, director):
    """
    Actualiza la lista de actores
    """
    movie = catalog['movies'][pos_movie]
    genre = catalog['actors'][pos_actor]
    lt.addLast(genre['movies_id'], movie['id'])
    lt.addLast(genre['movie_titles'], movie['title'])
    genre['movie_count'] += 1
    genre['movie_average'] += movie['vote_average']

def addGenre(catalog, row, pos_movie):
    """
    Adiciona un actor a la lista de actores
    """
    movie = catalog['movies'][pos_movie]
    g = newGenre(movie, row)
    lt.addLast(catalog['genres'], g)

def endDirectorslist(directores):
    for director in directores:
        director ['movie_average'] = director ['movie_average'] / director ['movie_count'] 

def endActorslist(actor):
    actor ['movie_average'] = actor ['movie_average'] / actor ['movie_count']

def endGenreslist(genre):
    genre ['movie_average'] = genre ['movie_average'] / genre ['movie_count']

# Funciones de consulta

def getMoviesByDirector (catalog, dir_name):
    """
    Retorna las peliculas a partir del nombre del director
    """
    return []