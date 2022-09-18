#-*- coding:utf-8 -*-
'''
Created on 12 ene. 2021

@author: jfc_007
'''

''' Este proyecto, se llevará a cabo complementándose con el enunciado adjuntado
    junto al desarrollo del mismo. Ahí encontrará los enunciados propuestos, y la 
    información necesaria para entender el procedimiento que se ha seguido
    para llevar a cabo el proyecto. Para introducirle en la temática de mi trabajo, 
    nos basamos en las calificaciones que le dan los aficionados a 
    las diversas carreras que se han disputado desde el año 2008 hasta el año 2018. Además
    encontramos los 3 primeros puestos de cada carrera'''

'''En primer lugar, leeremos el archivo csv del cual sacaremos la información
   que se va a utilizar durante el proyecto. Para ello debemos importar varios
   elementos que nos permitirán realizarlo.'''

from collections import namedtuple
import csv

''' A continuación introducimos los nombres con los que llamaremos tanto al conjunto
    de elementos, cómo a cada elemento, separados por comas entre sí, que tenemos dentro 
    del archivo con el que vamos a trabajar '''

formula1 = namedtuple('form', 'año,granpremio,posicion1,posicion2,posicion3,valoracion')

''' BLOQUE 1 '''

''' 1- Realizamos la lectura del archivo csv con la siguiente función: '''

def leer_formula(fichero):
    res = list()
    with open(fichero, 'rt', encoding='utf-8') as f:
        lector=csv.reader(f)
        next(lector)
        for reg in lector:
            res.append(formula1(int(reg[0]), reg[1], reg[2], reg[3], reg[4], float(reg[5])))
        return res
    
    
    
    
''' BLOQUE 2 '''
   
''' 2- Implementamos la primera función del bloque 2, que nos nombrará todos los pilotos 
    ganadores de al menos una carrera: '''
   
def leer_nombre_de_primer_puesto(datos):
    return {r.posicion1 for r in datos}

''' 3- Implementamos la segunda función de este bloque que nos dirá todos los ganadores
    junto al gran premio en el que salió victorioso de un año dado como parámetro'''

def lista_por_año_con_ganador_y_granpremio(datos, año):
    return [(r.granpremio, r.posicion1) for r in datos if año==r.año]




''' BLOQUE 3 '''

''' 4- Implementamos la primera función del bloque 3, que consistirá en la suma de las puntuaciones
    en un año determinado'''

def suma_de_puntuacion_por_año(datos, año):
    suma=0
    for r in datos:
        if año==r.año:
            suma+=r.valoracion
    return suma

''' 5- Implementamos la segunda función del bloque 3, que consistirá en realizar el promedio de
    las puntuaciones dadas en un año determinado. '''

def media_de_puntuacion_dado_por_año(datos, año):
    res=0
    suma=0
    contador=0
    for r in datos:
        if año==r.año:
            suma+=r.valoracion
            contador+=1
        if contador>0:
            res=suma/contador
    return res





''' BLOQUE 4 '''

''' 6- Implementamos la única función que contiene este bloque, que consistirá en devolver la
    puntuación más alta de un año dado como parámetro. Además en el caso de que el año
    no entre en el intervalo de años que contiene nuestro archivo csv [2008,2018] devolverá
    el valor None. '''

def puntuacion_mas_alta_de_x_año(datos, año):
    aux= None
    if 2008<=año<=2018:
        aux= max([r.valoracion for r in datos if año==r.año])
    return aux





''' BLOQUE 5 '''

''' 7- Implementamos la única función que contiene este bloque, que consistirá en devolver las
    n puntuaciones más bajas junto al gran premio,siendo n un parámetro que le pasamos 
    a la función.'''

def n_puntuaciones_mas_baja(datos,n):
    return sorted([(r.granpremio, r.valoracion) for r in datos], key=lambda e:e[1], reverse=False)[:n]
    
''' He parametrizado las respuestas para que dependiendo del valor que se le dé a "n"
    (parámetro del número de puntuaciones más bajas que queremos que aparezcan en pantalla), 
    dé diferentes respuestas acorde a la pluralidad, singularidad o que su valor sea 0. '''
    
def para_respuesta_del_test_plurar_singular_0(n):
    if n>=2:
        res= print("Los", n ,"grandes premios con las puntuaciones más bajas son: ")
    elif n==1:
        res= print("El gran premio con la puntuación más baja es: ")
    elif n==0:
        res= print("El parámetro 0 no devuelve nigún resultado")
    return res
        
        
    
    
''' BLOQUE 6 '''

''' 8- Implementamos la primera función que contiene el bloque 6, que consistirá en crear un diccionario
    que tendrá como clave los grandes premios de un año dado como parámetro, y lo relacionará con los
    valores que contiene dicha clave correspondientes formando la siguientes estructura:
    {'granpremio':(año,posicion1,posicion2,posicion3,valoracion)}'''

def diccionario_en_año_n_con_clavegranpremio_con_su_registro(datos, año):
    res = dict()
    for r in datos:
        if año ==r.año:
            res[r.granpremio] = [(r.año,r.posicion1,r.posicion2,r.posicion3,r.valoracion)]
    return res


''' 9- Implementamos la segunda función que contiene el bloque 6, que consistirá en crear un diccionario
    que relacione los pilotos que han quedado entre las dos primeras posiciones con el gran premio
    y la valoración. '''

def diccionario_piloto_por_registro_en_x_piloto(datos):
    aux = dict()
    for r in datos:
        if r.posicion1 not in aux:
            aux[r.posicion1] = [(r.granpremio,r.valoracion)]
        elif r.posicion2 not in aux:
            aux[r.posicion2] = [(r.granpremio,r.valoracion)]
        else:
            aux[r.posicion1]+= [(r.granpremio,r.valoracion)]
            aux[r.posicion2]+= [(r.granpremio,r.valoracion)]
            
    res= dict()
    for clave,valor in aux.items():
        res[clave]=sorted(valor, key=lambda a:a[1], reverse=True)
    return res

''' Función para comprobar que el resultado está bien. Como el primer pilot que nos aparece en pantalla es
    Hamilton, miraremos las carreras en las que ha quedado primero o segundo, junto a su valoración,
    e iremos comparando el resultado para comprobar que esté correcto. También se podrá hacer con el
    resto de pilotos. '''

def comprobacion(datos, piloto):
    res= [(r.granpremio,r.valoracion) for r in datos if  r.posicion2 == piloto  or r.posicion1 == piloto]
    return sorted(res, key=lambda a:a[1], reverse=True)


