import csv
from collections import namedtuple
from datetime import datetime

FrecuenciaNombre = namedtuple('FrecuenciaNombre', 'año,nombre,frecuencia,genero')

def leer_frecuencias_nombres(ruta): 
    '''
    Recibe la ruta de un fichero CSV codificado en UTF-8, y devuelve una lista de tuplas de tipo 
    FrecuenciaNombre(int, str, int, str) conteniendo todos los datos almacenados en el fichero.
    '''
    with open(ruta, encoding = 'utf-8') as f: 
        lector = csv.reader(f)
        next(lector)
        
        res =[]
        
        for año, nombre, frecuencia, genero in lector:
            año = int(año)
            frecuencia = int(frecuencia)
            tupla = FrecuenciaNombre(año,nombre,frecuencia,genero)
            res.append(tupla)
        return res
    
    return FrecuenciaNombre
    
def filtrar_por_genero(frecuencias, genero):
    '''
    Recibe una lista de tuplas de tipo FrecuenciaNombre y un género de tipo str, y 
    devuelve una lista de tuplas de tipo FrecuenciaNombre con los registros del género recibido como parámetro.
    '''
    res = []
    for p in frecuencias:
        if p.genero == genero:
            res.append(frecuencias)
    return res

def calcular_nombres(frecuencias, genero):

    '''
    recibe una lista de tuplas de tipo FrecuenciaNombre y
    un género de tipo str, y devuelve un conjunto {str} con los nombres del género 
    recibido como parámetro. El género puede ser 'Hombre', 'Mujer' o tener un valor None,
    en cuyo caso se incluyen en el conjunto todos los nombres. El valor por defecto del género es None.
    '''
    nombre_genero = set()
    for p in frecuencias:
        if p.genero == None or p.genero == genero:
            nombre_genero.add(p.nombre)
    return nombre_genero

def calcular_nombres_ambos_generos(frecuencias): 
    '''
    recibe una lista de tuplas de tipo FrecuenciaNombre, 
    y devuelve un conjunto {str} con los nombres que han sido utilizados en ambos géneros.
    '''
    
    hombres = calcular_nombres(frecuencias, "Hombre")
    mujeres = calcular_nombres(frecuencias, "Mujer")

    nombre_en_ambos = set()
    
    for p in frecuencias:
        if p.nombre in hombres and p.nombre in mujeres:
            nombre_en_ambos.add(p.nombre)
    return nombre_en_ambos
        
def calcular_nombres_compuestos(frecuencias, genero):
    '''
    recibe una lista de tuplas de tipo FrecuenciaNombre
    y un género de tipo str, y devuelve un conjunto {str} con los nombres que contienen 
    más de una palabra. El género puede ser 'Hombre', 'Mujer' o tener un valor None, 
    en cuyo caso se incluyen en el conjunto todos los nombres. El valor por defecto del género es None.
    '''
    nombre_genero = set()
    for p in frecuencias:
        if (p.genero == None or p.genero == genero) and len(p.nombre) >= 2:
            nombre_genero.add(p.nombre)
    return nombre_genero

def calcular_frecuencia_media_nombre_años(frecuencias, nombre, año_i, año_f): 

    '''
    recibe una lista de tuplas de tipo FrecuenciaNombre,
    un nombre, un año inicial y un año final y calcula la frecuencia media del nombre dado como
    parámetro en el rango de años [año_inicial, año_final) formado por el año inicial y el año
    final dados como parámetro. Si no se puede calcular la media devuelve 0.
    '''
    res = []
    nombres = 0
    veces = 0
    for p in frecuencias:
        nombres += 1
        if (p.nombre == nombre) and (año_i <= p.año < año_f): 
            veces += 1
    return nombres/veces
        
    


        
        
        