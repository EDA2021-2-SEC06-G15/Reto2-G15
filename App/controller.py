"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import csv
from DISClib.ADT import list as lt


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo del museo

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArtists(catalog)
    loadArtworks(catalog)
    

def loadArtists(catalog):
    """
    Carga los artistas del archivo. 
    """
    artistsfile = cf.data_dir + 'Datos/Artists-utf8-small.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)
    
def loadArtworks(catalog):
    """
    Carga las obras del archivo. 
    """
    artworksfile = cf.data_dir + 'Datos/Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artworksfile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)

# Funciones de ordenamiento

def sortArtists(Artists):
    
    Sorted = model.sortArtist(Artists)
    return (Sorted)

def sortArtworks(artworks):
    
    Sorted = model.sortArtworks(artworks)
    return (Sorted)
  

        
def SortNacionalidades(nacionalidades):
    Sorted = model.SortNacionalidades(nacionalidades)
    return (Sorted)


     
# Funciones de consulta sobre el catálogo

def getArtistsbyYear(catalog, year1, year2):
    """
    Retorna los artistas entre los años dados
    """
    ArtistbyYear = model.getArtistsbyYear(catalog, year1, year2)
    Artistsort =sortArtists(ArtistbyYear)
    return(Artistsort)


def getArtworksbyDate(catalog, date1, date2):
    """
    Retorna las obras entre las fechas dadas
    """
    ArtworksbyYear = model.getArtworksbyDate(catalog, date1, date2)
    
    return(ArtworksbyYear)

def PurchaseArtworks(obras):
    """
    Retorna las obras adquiridas por compra
    """
    purchased = model.PurchaseArtworks(obras)
    return(purchased)


def CountArtists(obras):
    """
    Retorna los autores de una lista de obras
    """
    Artists = model.CountArtists(obras)
    return(Artists)


def ArtworksByArtist(catalog, artistname):

    artistID = model.ArtistID (catalog, artistname)
    artworkslist = model.ArtworksByID (catalog, artistID)
    
    return artworkslist 


def MediumInArtwork(artworksByID):
    
    mediums = model.MediumInArtworks(artworksByID)

    return mediums


def FreqMediums(mediums, Artworkslist):

    freq = model.freqMedium (mediums, Artworkslist)

    return freq


def MostUsedMedium(freq, Mediums):

    MostUsedMedium=model.MostUsedMedium(freq, Mediums)

    return MostUsedMedium


def MUMList(MostUsedMedium, Artworkslist):
    MUMList = model.MUMList(MostUsedMedium, Artworkslist)

    return MUMList

def TopNacionalidades(catalog):
    Top = model.TopNacionalidades(catalog)

    return Top

def MayorNacionalidad(catalog, top1):
    Obras = model.MayorNacionalidad(catalog, top1)
    return Obras

def ArtworksByDepto (catalog, Depto):
    artworks = model.ArtworksByDepto (catalog, Depto)

    return artworks


def tamanoObras (artworksByDepto):
    tamanoobras = model.tamanoObras(artworksByDepto)

    return tamanoobras

def precioObras (dimensiones, pesoObras):
    precioobras = model.precioObras(dimensiones, pesoObras)

    return precioobras

def pesoObras (artworksByDepto):
    pesoobras = model.pesoObras (artworksByDepto)

    return pesoobras

def sumaTotal(lista):
    precio = model.sumaTotal(lista)

    return precio


def obrasPorFecha (artworks):
    obras = model.obrasPorFecha(artworks)

    return obras

def obrasporcosto (artworksByDepto, zippedIDandPrice2):
    obrasPorCosto = model.obrasporcosto (artworksByDepto, zippedIDandPrice2)

    return obrasPorCosto

def ArtistNameByID (catalog, autorID):
    artistname = model.ArtistNameByID (catalog, autorID)

    return artistname

def ArtworksByIDItself (artworksByDepto, artworkID):
    artworks = model.ArtworksByIDItself (artworksByDepto, artworkID)

    return artworks


def zipper (lt1, lt2):
    size = lt.size(lt1)
    IDartworks = lt.newList()

    for i in range(1, size+1):
        artwork = lt.getElement(lt1, i)
        ID = artwork["ObjectID"]

        lt.addLast(IDartworks, ID)
    
    zipped = model.zipper(IDartworks, lt2)

    return zipped


def zipper2 (lt1, lt2):
    size = lt.size(lt1)
    IDartworks = lt.newList()

    for i in range(1, size+1):
        artwork = lt.getElement(lt1, i)
        ID = artwork["ObjectID"]

        lt.addLast(IDartworks, ID)
    
    zipped = model.zipper2(IDartworks, lt2)

    return zipped