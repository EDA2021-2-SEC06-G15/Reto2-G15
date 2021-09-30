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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import quicksort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo del museo. Crea una lista vacia para guardar
    todos los artistas, adicionalmente, crea una lista vacia para las obras de arte.
    Retorna el catalogo inicializado.
    """
    catalog = {'artists': None,
               'artworks': None}

    """
    Esta lista contiene todo los datos encontrados
    en los archivos de carga.  Estos datos no estan
    ordenados por ningun criterio.  Son referenciados
    por los indices creados a continuacion.
    """

    catalog['artists'] = lt.newList('SINGLE_LINKED',
                                    cmpfunction=compareartistyears)
    catalog['artworks'] = lt.newList('SINGLE_LINKED',
                                    cmpfunction=compareartworkyearsmonthday)

    """
    A continuacion se crean indices por diferentes criterios
    para llegar a la informacion consultada.  Estos indices no
    replican informacion, solo referencian los libros de la lista
    creada en el paso anterior.
    """

    """
    Este indice crea un map cuya llave es el identificador del libro
    """


    catalog['Medium'] = mp.newMap(10000,
                                   maptype='CHAINING',
                                   loadfactor=0.75,
                                   comparefunction=compareMapMediums)

    
    return catalog

def newMedium(name):
    """
    Crea una nueva estructura para modelar los medios de una obra
    Se crea una lista para guardar las tecnicas de dicha obra
    """
    medium = {'name': "",
              "artworks": None,}
    medium['name'] = name
    medium['books'] = lt.newList('SINGLE_LINKED', compareMediumsByName)
    return medium

# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):
    """
    Adiciona un artista a la lista de artistas
    """
    a = newArtist(artist['DisplayName'], artist['ConstituentID'], artist['Nationality'], artist['Gender'], artist['BeginDate'], artist['EndDate'])
    lt.addLast(catalog['artists'], a)

def addArtwork(catalog, artwork):
    """
    Adiciona una obra a la lista de obras
    """
    art = newArtwork(artwork['Title'], artwork['ObjectID'], artwork['ConstituentID'], artwork['Medium'], artwork['Circumference (cm)'], 
                    artwork['Depth (cm)'], artwork['Diameter (cm)'], artwork['Height (cm)'], artwork['Length (cm)'], artwork['Weight (kg)'], 
                    artwork['Width (cm)'], artwork['Seat Height (cm)'], artwork['Duration (sec.)'], artwork['Date'], artwork['DateAcquired'],artwork['CreditLine'], artwork['Dimensions'], artwork['Department'], artwork['Classification'])
    
    lt.addLast(catalog['artworks'], artwork)
    mp.put(catalog['Medium'], artwork['ObjectID'], artwork)
    mediums = artwork['Medium'].split(",")  # Se obtienen las tecnicas
    for m in mediums:
        addMedium(catalog, m.strip(), artwork) #Se agrega la tecnica
    

def addMedium(catalog, medium, artwork):
    """
    Esta función adiciona un tecnica usadas
    en la obra.
    """
    mediums = catalog['Medium']
    existmedium = mp.contains(mediums, medium)
    if existmedium:

        if existmedium:
            entry = mp.get(mediums, medium)
            author = me.getValue(entry)
        else:
            author = newMedium(medium)
            mp.put(mediums, medium, author)
        lt.addLast(author['books'], artwork)

# Funciones para creacion de datos
def newArtist(name, id, nacionality, gender, begin, end):
    """
    Esta estructura almancena los artistas utilizados.
    """
    artist = {'DisplayName': '', 'ConstituentID': '', 'Nationality': '','Gender': '','BeginDate': '','EndDate': '' }
    artist['DisplayName'] = name
    artist['ConstituentID'] = id
    artist['Nationality'] = nacionality
    artist['Gender'] = gender
    artist['BeginDate'] = begin
    artist['EndDate'] = end
    return artist

def newArtwork(name, id, constituentid, medium, circunferencia, profundidad, diametro, altura, largo, peso, ancho, altura_asiento, duracion, 
                fecha, fecha_compra, adquisicion, dimensions, departamento, clasificacion):
    """
    Esta estructura almancena las obras utilizadas.
    """
    artwork = {'Title': '', 'ObjectID': '', 'ConstituentID': '', 'Medium': '','Circumference (cm)': '','Depth (cm)': '','Diameter (cm)': '',
                'Height (cm)': '','Length (cm)': '','Weight (kg)': '','Width (cm)': '','Seat Height (cm)': '','Duration (sec.)': '',
                'Date': '','DateAcquired': '','CreditLine': '','Department':'','Classification':''}
    artwork['Title'] = name
    artwork['ObjectID'] = id
    artwork['ConstituentID'] = constituentid
    artwork['Medium'] = medium
    artwork['Dimensions'] = dimensions
    artwork['Circumference (cm)'] = circunferencia
    artwork['Depth (cm)'] = profundidad
    artwork['Diameter (cm)'] = diametro
    artwork['Height (cm)'] = altura
    artwork['Length (cm)'] = largo
    artwork['Weight (kg)'] = peso
    artwork['Width (cm)'] = ancho
    artwork['Seat Height (cm)'] = altura_asiento
    artwork['Duration (sec.)'] = duracion
    artwork['Date'] = fecha
    artwork['DateAcquired'] = fecha_compra
    artwork['CreditLine'] = adquisicion
    artwork['Department'] = departamento
    artwork['Classification'] = clasificacion
    
    return artwork

# Funciones de consulta


def getArtistsbyYear(catalog, year1, year2):
    
    artists = catalog['artists']
    ArtistsbyYear = lt.newList()
    size = lt.size(artists)
    for cont in range(1,size+1):
        artist = lt.getElement(artists, cont)
        year=artist['BeginDate']
        if year1<=int(year)<=year2:
            lt.addLast(ArtistsbyYear, artist)
       
    return ArtistsbyYear

def getArtworksbyDate(catalog, date1, date2):
    
    artworks = catalog['artworks']

    ArtworksByYear = lt.newList()
    delete = lt.newList()
    ids = lt.newList()
   
    size = lt.size(artworks)

    fecha1 = date1.split("-")
    fecha2 = date2.split("-") 

    for cont in range(1,size+1):
        artwork = lt.getElement(artworks, cont)
        date = artwork['DateAcquired'].split("-")

        if (fecha1[0])<=(date[0])<=(fecha2[0]):
            lt.addLast(ArtworksByYear, artwork)

    size2 = lt.size(ArtworksByYear)
    
    
    for cont in range(1,size2+1):
        artwork = lt.getElement(ArtworksByYear,cont)
        id = artwork['ObjectID']
        lt.addLast(ids, id)
        

    for cont in range(1,size2+1):
        artwork = lt.getElement(ArtworksByYear, cont)
        date = artwork['DateAcquired'].split("-")

        if fecha1[0]==date[0]:
            if date[1]<fecha1[1]:
                id = artwork['ObjectID']
                pos = lt.isPresent(ids, id)
                lt.addLast(delete,pos)

        if fecha2[0]==date[0]:
            if date[1]>fecha1[1]:
                id = artwork['ObjectID']
                pos = lt.isPresent(ids, id)
                lt.addLast(delete,pos)

        if fecha1[0]==date[0] and fecha1[1==date[1]]:
            if date[2]<=fecha1[2]:
                id = artwork['ObjectID']
                pos = lt.isPresent(ids, id)
                lt.addLast(delete,pos)
        
        if fecha2[0]==date[0] and fecha2[1==date[1]]:
            if date[2]>=fecha1[2]:
                id = artwork['ObjectID']
                pos = lt.isPresent(ids, id)
                lt.addLast(delete,pos)    

    size3 = lt.size(delete)

    ArtworksByDate = lt.newList()

    for cont in range(1,size2+1):        
        elemento = lt.getElement(ArtworksByYear, cont)
        presente = lt.isPresent(delete, cont)
        if presente == 0:
            lt.addLast(ArtworksByDate,elemento)
        


    return ArtworksByDate

def PurchaseArtworks(obras):

    purchased = lt.newList()
    size = lt.size(obras)
    for count in range(1, size+1):
        obra = lt.getElement(obras, count)
        adquisicion = obra["CreditLine"]
        if adquisicion == "Purchase":
            lt.addLast(purchased, obra)

    return purchased


def CountArtists(obras):

    size = lt.size(obras)
    lista = lt.newList()

    for count in range (1,size+1):
        obra = lt.getElement(obras, count)
        sinconrchete1 = obra["ConstituentID"].lstrip("[")
        sinconrchete2 = sinconrchete1.rstrip("]")
        artists = sinconrchete2.split(",")
        size2 = len(artists)
        

        for n in range(0, size2):
            artist = artists[n]
            pos = lt.isPresent(lista, artist)

            if pos == 0:
                lt.addLast(lista, artist)
    return (lista)

            
        

def ArtistID (catalog, artistname):

    artists = catalog['artists']     
    i=0
    flag=True

    while i <= lt.size(artists) and flag == True:
        artist = lt.getElement(artists, i)
        
        Name = artist['DisplayName'] 
        
        if Name == artistname:
            artistID = artist["ConstituentID"]
            flag=False
            return artistID
    
        i+=1

        if i > lt.size(artists):
            return("No se he encontrado el artista especificado")



def ArtworksByID (catalog, artistID):
    
    artworks = catalog["artworks"]
    artworksByID = lt.newList()
    i=1
    
    while i <= lt.size(artworks):
        artwork = lt.getElement(artworks, i)
        catalogID = artwork["ConstituentID"]
        
        if artistID in catalogID:
            lt.addLast(artworksByID, artwork)
        
        i+=1    

    return artworksByID


def ArtworksByIDItself (artworksByDepto, artworkID):
    
    artworks = artworksByDepto
    artworksByID = lt.newList("")
    i=1
    
    while i <= lt.size(artworks):
        artwork = lt.getElement(artworks, i)
        catalogID = artwork["ObjectID"]
        
        if artworkID in catalogID:
            lt.addLast(artworksByID, artwork)
        
        i+=1    

    return artworksByID


def ArtistNameByID (catalog, artistID):
    
    Artists = catalog["artists"]
    i=1
    
    while i <= lt.size(Artists):
        artist = lt.getElement(Artists, i)
        ID = artist["ConstituentID"]
        
        if ID == artistID:
            name = artist["DisplayName"]
            i=1+lt.size(Artists)

            return name

        i+=1    

def ArtistListByID (catalog, artistID):
    
    Artists = catalog["artists"]
    size = lt.size(Artists)

    for cont in range(1, size+1):
        artists = lt.getElement(Artists, cont)
        if artistID == artists["ConstituentID"]:
            return artists
    
        
def freqMedium (Mediums, Artworkslist):

    MediumListReps=lt.newList()
    size=lt.size(Artworkslist)

    for n in range(1,size+1):
        
        artwork = lt.getElement(Artworkslist, n)
        
        Medium=artwork["Medium"]

        lt.addLast(MediumListReps, Medium)

    freq = lt.newList()
    
    size2 = lt.size(Mediums)
    size3 = lt.size(MediumListReps)

    for Medium in range(1, 1+size2):
        y=lt.getElement(Mediums, Medium)
        i=0

        for count in range(1, 1+size3):
            x=lt.getElement(MediumListReps, count)

            if y == x:
                i+=1
        
        lt.addLast(freq, i)

    return freq


def MediumInArtworks (artworksByID):
    
    mediums = lt.newList()
    i=0
    
    while i <= lt.size(artworksByID):
        artwork = lt.getElement(artworksByID, i)
        Medium = artwork["Medium"]
        pos=lt.isPresent(mediums, Medium)

        if pos == 0:
            lt.addLast(mediums, Medium)

        i+=1  
   
    return (mediums)



def MUMList(MostUsedMedium, Artworkslist):

    MUMList = lt.newList('ARRAY:LIST')
    size = lt.size(Artworkslist)

    for i in range(1, 1+size):
        Artwork = lt.getElement(Artworkslist, i)
        Medium = Artwork["Medium"]

        if Medium == lt.getElement(MostUsedMedium, 1)["Medium"]:
            lt.addLast(MUMList, Artwork)
            

    return MUMList  

def TopNacionalidades(catalog):

    ArtWorks = catalog["artworks"]
    Nacionalidades = lt.newList()
    TotalArtists = lt.newList()
    Nacionalidadessin = lt.newList()
    reps = lt.newList()

    size = lt.size(ArtWorks)
    
   
    for cont in range(1, size+1):
        obra = lt.getElement(ArtWorks, cont)
        
        sinconrchete1 = obra["ConstituentID"].lstrip("[")
        sinconrchete2 = sinconrchete1.rstrip("]")
        artists = sinconrchete2.split(",")
        size2 = len(artists)
        for n in range(0,size2):
            artistaid = artists[n]
            artist = ArtistListByID(catalog, artistaid)
            if artist is not None:
                Nacionalidad = artist["Nationality"]
                lt.addLast(Nacionalidades, Nacionalidad)
                pos = lt.isPresent(Nacionalidadessin, Nacionalidad)
                if pos == 0:
                    lt.addLast(Nacionalidadessin, Nacionalidad)       
    
    size4 = lt.size(Nacionalidades)
    size5 = lt.size(Nacionalidadessin)
    print ("Nacionalidades sin: " +str(size5)) 

    for x in range(1,size5+1):
        nacionalidad = lt.getElement(Nacionalidadessin, x)
        i = 0
        for y in range(1,size4+1):
            
            nacionalidad2 = lt.getElement(Nacionalidades, y)
            if nacionalidad == nacionalidad2:
                i+=1
        lt.addLast(reps, i)
    size6 = lt.size(reps)
    print ("Reps: "+str(size6))
    lista = zipNAcionalidades(Nacionalidadessin, reps)

    return lista

    
def MayorNacionalidad(catalog, top1):
    Artworks = catalog["artworks"]
    TotalArtworks = lt.newList()
    size = lt.size(Artworks)
    
    for cont in range(1,size+1):
        artwork = lt.getElement(Artworks, cont)
        sinconrchete1 = artwork["ConstituentID"].lstrip("[")
        sinconrchete2 = sinconrchete1.rstrip("]")
        artists = sinconrchete2.split(",")
        size2 = len(artists)
        Esta = False
        
        for n in range(0, size2):
            
            artistaid = artists[n]
            artist = ArtistListByID(catalog, artistaid)
            if artist is not None:
                Nacionalidad = artist["Nationality"]
                
                if Nacionalidad == top1:
                    Esta = True
                    
        if Esta is True:
            lt.addLast(TotalArtworks, artwork)
        Esta = False

    return (TotalArtworks)

        
    





    
def zipNAcionalidades (lt1, lt2):
    zipped = lt.newList()
    size = lt.size(lt1)

    for i in range(1, size+1):
        element1 = lt.getElement(lt1, i)
        element2 = lt.getElement(lt2, i)

        elementzip = {"Nationality": element1, "Cantidad": element2}

        lt.addLast(zipped, elementzip)
        
    return zipped






def ArtworksByDepto (catalog, Depto):
    
    artworks = catalog["artworks"]
    artworksByDepto = lt.newList()
    i=1
    
    while i <= lt.size(artworks):
        artwork = lt.getElement(artworks, i)
        catalogDepto = artwork["Department"]
        
        if Depto in catalogDepto:
            lt.addLast(artworksByDepto, artwork)
        
        i+=1    

    return artworksByDepto


def tamanoObras (artworksByDepto):
    size = lt.size(artworksByDepto)
    dimensionList = lt.newList()

    for i in range(1, 1+size):
        artwork = lt.getElement(artworksByDepto, i)

        circunferencia = artwork["Circumference (cm)"]
        profundidad = artwork["Depth (cm)"]
        diametro = artwork["Diameter (cm)"]
        altura = artwork["Height (cm)"]
        largo = artwork["Length (cm)"]
        ancho = artwork["Width (cm)"]

        dimensiones = 0   
        
        if altura != "":
            altura = float(altura)/100

            if circunferencia != "":
                circunferencia = float(circunferencia)/100
                dimensiones = (3.14159*(circunferencia/(2*3.14159))**2)*altura

            elif diametro != "":
                diametro = float(diametro)/100
                dimensiones = (3.14159*(diametro/(2))**2)*altura

            elif profundidad != "" and ancho != "":
                profundidad = float(profundidad)/100
                ancho = float(ancho)/100
                dimensiones = profundidad*ancho*altura

            elif profundidad != "" and ancho != "":
                largo = float(largo)/100
                ancho = float(ancho)/100
                dimensiones = profundidad*ancho*altura

            elif profundidad != "":
                profundidad = float(profundidad)/100
                dimensiones = profundidad*altura

            elif largo != "":
                largo = float(largo)/100
                dimensiones = largo*altura
            
            elif ancho != "":
                ancho = float(ancho)/100
                dimensiones = ancho*altura


        elif largo != "" and ancho != "":
            largo = float(largo)/100
            ancho = float(ancho)/100
            dimensiones = largo*ancho 

        elif circunferencia != "":
            circunferencia = float(circunferencia)/100
            dimensiones = (3.14159*(circunferencia/(2*3.14159))**2)

        elif diametro != "":
            diametro = float(diametro)/100
            dimensiones = (3.14159*(diametro/(2))**2)
        

        lt.addLast(dimensionList, dimensiones)

    return dimensionList


def pesoObras (artworksByDepto): 
    size = lt.size(artworksByDepto)
    pesoObras = lt.newList()

    for i in range(1, 1+size):
        artwork = lt.getElement(artworksByDepto, i)

        peso = artwork["Weight (kg)"]

        lt.addLast(pesoObras, peso)

    return pesoObras


def precioObras (dimensiones, pesoObras):
    size = lt.size(dimensiones)
    precioObras = lt.newList()

    for i in range(1, 1+size):
        
        peso = lt.getElement(pesoObras, i)
        dimension = lt.getElement(dimensiones, i)

        if dimension != 0:
            precio = dimension*72   

        if peso != "":
            peso = float(peso)

            if peso == 0 and dimension == 0:
                precio = 48        
            elif peso >= dimension:
                precio = peso*72
            elif peso < dimension:
                precio = dimension*72

        if peso == "" and dimension == 0:
            precio = 48
        
        lt.addLast(precioObras, precio)
        
    return precioObras

def sumaTotal(lista):
    size = lt.size(lista)
    total = 0
    
    for i in range(1, size+1):
        elemento = lt.getElement(lista, i)

        if elemento != "":
            total=total+float(elemento)
    
    return total
        
def obrasPorFecha (artworks):
    size = lt.size(artworks)
    artworksWithDate = lt.newList()
    
    for i in range(1, size+1):
        artwork = lt.getElement(artworks, i)
        date = artwork["Date"]

        if date != "":
            lt.addLast(artworksWithDate, artwork)
        
    sortedArtwoks = sortArtworksByDate(artworksWithDate)

    return sortedArtwoks

def obrasporcosto (artworksByDepto, zippedIDandPrice2):        
    sortedArtworks = sortArtworksByPrice(zippedIDandPrice2)

    return sortedArtworks


def zipper (lt1, lt2):
    zipped = {}
    size = lt.size(lt1)

    for i in range(1, size+1):
        element1 = lt.getElement(lt1, i)
        element2 = lt.getElement(lt2, i)

        zipped[element1] = element2
        
    return zipped

def zipper2 (lt1, lt2):
    zipped = lt.newList()
    size = lt.size(lt1)

    for i in range(1, size+1):
        element1 = lt.getElement(lt1, i)
        element2 = lt.getElement(lt2, i)

        elementzip = {"ObjectID": element1, "Price": element2}

        lt.addLast(zipped, elementzip)
        
    return zipped

def zipper3 (lt1, lt2):
    zipped = lt.newList()
    size = lt.size(lt1)

    for i in range(1, size+1):
        element1 = lt.getElement(lt1, i)
        element2 = lt.getElement(lt2, i)

        elementzip = {"Medium": element1, "Freq": element2}

        lt.addLast(zipped, elementzip)
        
    return zipped




# Funciones utilizadas para comparar elementos dentro de una lista

def compareartistyears(year1, year2):
    return (int(year1['BeginDate']) < int(year2['BeginDate']))


def compareartworkyearsinv(year1, year2):
    return (int(year1['Date']) < int(year2['Date']))

def compareartworkprices(price1, price2):
    return (float(price1["Price"]) > float(price2["Price"]))

def comparemediumsfreq (freq1, freq2):
    return (int(freq1["Freq"]) > int(freq2["Freq"]))

def compareartworkyearsmonthday(date1, date2):
    return (str(date1["DateAcquired"]) > date2["DateAcquired"])
    
def comparenacionalidades(reps1, reps2):
    return (int(reps1["Cantidad"]) > int(reps2["Cantidad"]))

def compareMapMediums(id, entry):
    """
    Compara dos tecnicas, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if ((id) == (identry)):
        return 0
    else:
        return -1

def compareMediumsByName(keyname, medium):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(medium)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1

# Funciones de ordenamiento

def sortArtist(artists):
    result=sa.sort(artists, compareartistyears)
    return(result)


def sortArtworksByDate (artworks):
    result = sa.sort(artworks, compareartworkyearsinv)
    return(result)
    

def sortArtworks(Artworks):
    result = sa.sort(Artworks, compareartworkyearsmonthday)

    return result


def sortArtworksByPrice(zippedIDandPrice):
    result = sa.sort(zippedIDandPrice, compareartworkprices)
    return result
    


def MostUsedMedium(freq, Mediums):

    zipped = zipper3(Mediums, freq)

    sorted = sa.sort(zipped, comparemediumsfreq)

    return sorted

def SortNacionalidades(nacionalidades):
    result = sa.sort(nacionalidades, comparenacionalidades)
    return result 

