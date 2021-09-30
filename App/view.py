"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import time

default_limit = 1000
sys.setrecursionlimit(default_limit*10)


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
def initCatalog():
    return controller.initCatalog()

def loadData(catalog):
    """
    Carga los artistas y las obras en la estructura de datos
    """
    controller.loadData(catalog)

    

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronológicamente los artistas ")
    print("3- Listar cronológicamente las adquisiciones")
    print("4- Clasificar las obras de un artista por técnica")
    print("5- Clasificar las obras por la nacionalidad de sus creadores")
    print("6- Transportar obras de un departamento ")
    print("0- Salir")


def printArtistbyYear(artists):
    size = lt.size(artists)
    if size:
        print(' Estos son los 3 primeros: ')
        i=1
        while i<=3:
            artist=lt.getElement(artists,i)
            print('Nombre: ' + artist['DisplayName'] + '  Año de nacimiento: ' +
                  artist['BeginDate'] + '  Año de fallecimiento: ' + artist['EndDate']+ ' Nacionalidad: ' + artist['Nationality']  + '  Genero: ' +
                  artist['Gender'])
            i+=1
        print (' Estos son los 3 últimos: ')
        j=size
        a=1
        while a<=3:
            artist=lt.getElement(artists,j)
            print('Nombre: ' + artist['DisplayName'] + '  Año de nacimiento: ' +
                  artist['BeginDate'] + '  Año de fallecimiento: ' + artist['EndDate']+ ' Nacionalidad: ' + artist['Nationality']  + '  Genero: ' +
                  artist['Gender'])
            j-=1
            a+=1
    else:
        print('No se encontraron artistas')
        
         

def printartistandfreq(MostUsedMedium):
    i = 1

    while i <= 5:
        element =  lt.getElement(MostUsedMedium, i)
        tecnica = element["Medium"]
        frecuencia = element["Freq"]

        i+=1

        print(str(tecnica)+": "+str(frecuencia))


def printMUMList(catalog, MUMList):
    i = 1
    
    while i <= 3:
        print(i)
        artwork = lt.getElement(MUMList, i)

        print('Titulo: ' + artwork['Title'])
        print(" ")
        print('Artista(s): ')

        CA = artwork["ConstituentID"]
        CA2=CA.lstrip("[")
        CA3 = CA2.rstrip("]")
        coAutors = CA3.split(", ")
        
        j=0

        for A in coAutors:
            autorID = coAutors[j]
            ArtistName = controller.ArtistNameByID (catalog, autorID)

            print(ArtistName)

            j+=1

        print(" ")
        print('Fecha de creación: ' + artwork['Date'])
        print(" ")
        print('Técnica(s) usada(s): ' + artwork['Medium'])
        print(" ")
        print("Dimensiones: " + artwork["Dimensions"])
        print(" ")

        i+=1


def print5MostArtworks (catalog, obras, zippedIDandPrice):  
    i=1

    while i <= 5:
        artwork = lt.getElement(obras, i)

        print(i)
        print(" ")
        print('Titulo: ' + artwork['Title'])
        print(" ")
        print('Artista(s): ')

        CA = artwork["ConstituentID"]
        CA2=CA.lstrip("[")
        CA3 = CA2.rstrip("]")
        coAutors = CA3.split(", ")
        
        j=0

        for A in coAutors:
            autorID = coAutors[j]
            ArtistName = controller.ArtistNameByID (catalog, autorID)

            print(ArtistName)

            j+=1

        print(" ")
        print("Clasificación: " + artwork["Classification"])
        print(" ")
        print('Fecha de creación: ' + artwork['Date'])
        print(" ")
        print('Técnica(s) usada(s): ' + artwork['Medium'])
        print(" ")
        print("Dimensiones: " + artwork["Dimensions"])
        print(" ")
        print("Costo asociado al transporte: " + str(zippedIDandPrice[artwork["ObjectID"]]) + " USD.")

        i+=1


def print5MostExpArtworks (catalog, obrasporcosto, artworksByDepto):  
    i=1

    while i <= 5:
        artworkIDandCost = lt.getElement(obrasporcosto, i)

        artworkID = artworkIDandCost["ObjectID"]
        artworkPrice = artworkIDandCost["Price"]
        

        obra =  controller.ArtworksByIDItself (artworksByDepto, artworkID)

        artwork = lt.getElement(obra, 1)

        print(i)
        print(" ")
        print('Titulo: ' + artwork['Title'])
        print(" ")
        print('Artista(s): ')

        CA = artwork["ConstituentID"]
        CA2=CA.lstrip("[")
        CA3 = CA2.rstrip("]")
        coAutors = CA3.split(", ")
        
        j=0

        for A in coAutors:
            autorID = coAutors[j]
            ArtistName = controller.ArtistNameByID (catalog, autorID)

            print(ArtistName)

            j+=1

        print(" ")
        print("Clasificación: " + artwork["Classification"])
        print(" ")
        print('Fecha de creación: ' + artwork['Date'])
        print(" ")
        print('Técnica(s) usada(s): ' + artwork['Medium'])
        print(" ")
        print("Dimensiones: " + artwork["Dimensions"])
        print(" ")
        print("Costo asociado al transporte: " + str(artworkPrice) + " USD.")

        i+=1

def printTop10(nacionalidades):
    size = lt.size(nacionalidades)
    
    print(' Top 10 de Nacionalidades con mayor cantidad de obra: ')
    i=1
    while i<=10:
        nacionalidad=lt.getElement(nacionalidades,i)
        print('Nacionalidad: ' + nacionalidad['Nationality'] + '  Cantidad de obras: ' + str(nacionalidad['Cantidad']))
        i+=1

def PrintObrasTop(Obras):
    size = lt.size(Obras)
    print(' Estos son los 3 primeros: ')
    i=1
    while i<=3:
        obra=lt.getElement(Obras,i)
        print('Titulo: ' + obra['Title'] + '  ID de el/los Artista/s: ' + obra['ConstituentID'] + '  Fecha de Fabricaci+on: ' + obra['Date']+ 
                ' Medio: ' + obra['Medium']  + '  Dimensiones: ' +  obra['Dimensions'])
        i+=1
    print (' Estos son los 3 últimos: ')
    j=size
    a=1
    while a<=3:
        obra=lt.getElement(Obras,i)
        print('Titulo: ' + obra['Title'] + '  ID de los Artistas: ' + obra['ConstituentID'] + '  Fecha de Fabricacion: ' + obra['Date']+ 
                ' Medio: ' + obra['Medium']  + '  Dimensiones: ' +  obra['Dimensions'])
        j-=1
        a+=1
    
    
        
def PrintCatalog(catalog):
    i=1
    while i<=3:
        artist=lt.getElement(catalog['artists'],i)
        print('Nombre: ' + artist['DisplayName'] + '  Año de nacimiento: ' + artist['BeginDate'] + 
                '  Año de fallecimiento: ' + artist['EndDate']+ ' Nacionalidad: ' + artist['Nationality']  + '  Genero: ' +
                  artist['Gender'])
        i+=1
    j=1
    while j<=3:
        obra=lt.getElement(catalog['artworks'],j)
        print('Titulo: ' + obra['Title'] + '  ID de los Artistas: ' + obra['ConstituentID'] + '  Fecha de Fabricacion: ' + obra['Date']+ 
                ' Medio: ' + obra['Medium']  + '  Dimensiones: ' +  obra['Dimensions'])
        j+=1

"""
Menu principal
"""

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        start_time = time.process_time()

        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print('Artistas cargados: ' + str(lt.size(catalog['artists'])))
        print('Obras cargadas: ' + str(lt.size(catalog['artworks'])))
        PrintCatalog(catalog)

        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000 
        print("Tiempo de ejecución: "+str(elapsed_time_mseg))

        
    elif int(inputs[0]) == 2:
        start_time = time.process_time()
        year1 = input("Ingrese el año inicial: ")
        year2 = input("Ingrese el año final: ")
        artists = controller.getArtistsbyYear(catalog, int(year1), int(year2))
        print('Hay ' + str(lt.size(artists))+ ' artistas entre ' + str(year1) +' y '+str(year2))
        printArtistbyYear(artists)

        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000 
        print("Tiempo de ejecución: "+str(elapsed_time_mseg))

    elif int(inputs[0]) == 3:
        start_time = time.process_time()

        date1 = input("Ingrese la fecha inicial (AAAA-MM-DD): ")
        date2 = input("Ingrese la fecha final (AAAA-MM-DD): ")
        obras = controller.getArtworksbyDate(catalog, date1, date2)
        print ("Hay un total de "+str(lt.size(obras))+" obras entre "+str(date1)+" y "+str(date2)+".")
        compradas = controller.PurchaseArtworks(obras)
        autores = controller.CountArtists(obras)
        print ("Con "+str(lt.size(autores))+" diferentes artistas y "+ str(lt.size(compradas))+" de ellas fueron compradas.")
        sorted = controller.sortArtworks(obras)
        PrintObrasTop(sorted)

        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000 
        print("Tiempo de ejecución: "+str(elapsed_time_mseg))
              

    elif int(inputs[0]) == 4:
        start_time = time.process_time()

        ArtistName = input("Ingrese el nombre del artista: ")
        Artworkslist = controller.ArtworksByArtist(catalog, ArtistName)
        totaldeobras = lt.size(Artworkslist)
        print("// ")
        print(str(ArtistName)+" tiene un total de "+str(totaldeobras)+" obras.")
        Mediums = controller.MediumInArtwork(Artworkslist)
        freq = controller.FreqMediums(Mediums, Artworkslist)
        print("// ")
        print(str(ArtistName)+" tiene un total de "+str(lt.size(Mediums))+" técnicas usadas.")
        MostUsedMedium = controller.MostUsedMedium(freq, Mediums)    
        print(" ")
        print("Las 5 técnicas más usadas son:")
        printartistandfreq(MostUsedMedium)
        print("// ")
        print("La técnica más usada por "+str(ArtistName)+" es: "+str(lt.getElement(MostUsedMedium, 1)["Medium"])+".")
        print(" ")
        List = controller.MUMList(MostUsedMedium, Artworkslist)
        print("Un ejemplo de 3 obras en las que se usó dicha técnica son: ")
        print(" ")
        printMUMList(catalog, List)
        print(" ")

        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000 
        print("Tiempo de ejecución: "+str(elapsed_time_mseg))

     
    elif int(inputs[0]) == 5:
        start_time = time.process_time()

        Nacionalidades = controller.TopNacionalidades(catalog)
        SortNacionalidad = controller.SortNacionalidades(Nacionalidades)
        print(lt.size(Nacionalidades))
        Top = lt.getElement(SortNacionalidad, 1)
        Top1 = Top["Nationality"]
        printTop10(SortNacionalidad)
        ObrasMayorNacionalidad = controller.MayorNacionalidad(catalog, Top1)
        print(lt.size(ObrasMayorNacionalidad))
        PrintObrasTop(ObrasMayorNacionalidad)

        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000 
        print("Tiempo de ejecución: "+str(elapsed_time_mseg))
  
    
    elif int(inputs[0]) == 6:
        start_time = time.process_time()

        dpto = input("Ingrese el departamento que desea consultar: ")
        artworksByDepto = controller.ArtworksByDepto (catalog, dpto)
        numeroDeObras = lt.size(artworksByDepto)
        print("// ")
        print("El MOMA va a transportar "+str(numeroDeObras)+" desde el departamento "+str(dpto)+".")
        print(" ")
        tamanoObras = controller.tamanoObras(artworksByDepto)
        pesoobras = controller.pesoObras(artworksByDepto)
        precioObras = controller.precioObras(tamanoObras, pesoobras)
        PrecioTotal = controller.sumaTotal(precioObras)
        pesoTotal = controller.sumaTotal(pesoobras)
        print("// ")
        print("El precio estimado para el transporte de estas obras es de: "+str(round(PrecioTotal, 3))+" USD.")
        print(" ")
        print("El peso estimado de estas obras es de: "+str(round(pesoTotal, 3))+" kg.")
        print(" ")
        obrasporfecha = controller.obrasPorFecha(artworksByDepto)
        zippedIDandPrice = controller.zipper(artworksByDepto, precioObras)
        zippedIDandPrice2 = controller.zipper2(artworksByDepto, precioObras)
        print("// ")
        print("Las 5 obras más antiguas a transportar son: ")
        print5MostArtworks(catalog, obrasporfecha, zippedIDandPrice)
        print(" ")
        print("// ")
        print("Las 5 obras más costosas de transportar son: ")
        obrasporcosto = controller.obrasporcosto(artworksByDepto, zippedIDandPrice2)
        print5MostExpArtworks(catalog, obrasporcosto, artworksByDepto)
        print(" ")

        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000 
        print("Tiempo de ejecución: "+str(elapsed_time_mseg))

    

    else:
        sys.exit(0)
sys.exit(0)


