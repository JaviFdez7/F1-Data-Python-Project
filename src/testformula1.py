#-*- coding:utf-8 -*-
'''
Created on 12 ene. 2021

@author: jfc_007
'''

''' Nota: el BLOQUE 7, se desarrollará a lo largo de este archivo .py '''

'''En primer lugar deberemos importar las funciones realizadas y explicadas
   en funcionesformula1 para poder trabajar con ellas'''

from funcionesformula1 import *




''' BLOQUE 1 '''

'''1- Leemos la primera de las funciones que nos dará paso a la lectura de
   los elementos de archivo csv'''
   
registros= leer_formula("../data/formula11.csv")

'''A continuación leeremos los 3 primeros registros,
   los 3 últimas y visualizaremos en la consola el número total de registros
   existentes dentro del archivo csv'''
   
print("Número de registros leídos:", len(registros))
print("Los tres primeros registros leídos:", registros[:3])
print("Los tres últimos registros leídos:", registros[-3:])





''' BLOQUE 2 '''

''' 2- Test de la primera función del bloque 2 '''

primer_puesto= leer_nombre_de_primer_puesto(registros)
print("\nLos pilotos que han quedado al menos una vez en primera posición son: ")
print(primer_puesto)


''' 3- Test de la segunda función del bloque 2 '''

''' Primera comprobación'''
año= 2017
campeones_granpremio_por_año=lista_por_año_con_ganador_y_granpremio(registros, año)
print("\nLos pilotos ganadores de cada gran premio en el año ", año, " son:") 
print(campeones_granpremio_por_año)

''' Segunda comprobación'''
año= 2011
campeones_granpremio_por_año=lista_por_año_con_ganador_y_granpremio(registros, año)
print("\nLos pilotos ganadores de cada gran premio en el año ", año, " son:") 
print(campeones_granpremio_por_año)






''' BLOQUE 3 '''

''' 4- Test de la primera función del bloque 3 ''' 

''' Primera comprobación'''
año=2009
suma_p_año= suma_de_puntuacion_por_año(registros,año)
print("\nLa suma total de la valoración dada por los espectadores a cada gran premio de la temporada ", año, " es:")
print(suma_p_año)

''' Segunda comprobación'''
año=2018
suma_p_año= suma_de_puntuacion_por_año(registros,año)
print("\nLa suma total de la valoración dada por los espectadores a cada gran premio de la temporada ", año, " es:")
print(suma_p_año)


''' 5- Test de la segunda función de bloque 3 '''

''' Primera comprobación'''
año=2012
promedio_p_año=media_de_puntuacion_dado_por_año(registros, año)
print("\nEl promedio de las valoraciones dadas por los espectadores en el año ", año, " es:")
print(promedio_p_año)

''' Segunda comprobación'''
año=2016
promedio_p_año=media_de_puntuacion_dado_por_año(registros, año)
print("\nEl promedio de las valoraciones dadas por los espectadores en el año ", año, " es:")
print(promedio_p_año)





''' BLOQUE 4 '''

''' 6- Test de la función del bloque 4 '''

''' Primera comprobación'''
año=2008
val_mas_alta_año=puntuacion_mas_alta_de_x_año(registros, año)
print("\nLa carrera con mayor valoración del año ", año, " es:")
print(val_mas_alta_año)

''' Segunda comprobación'''
año=2015
val_mas_alta_año=puntuacion_mas_alta_de_x_año(registros, año)
print("\nLa carrera con mayor valoración del año ", año, " es:")
print(val_mas_alta_año)





''' BLOQUE 5 '''

''' 7- Test de la función del bloque 5 '''

''' Primera comprobación'''
numero=4
print("\nPasamos el parámetro numero con el cual ordenamos el número de puntuaciones más bajas que queremos\nque se muestren en pantalla, en este caso: ", numero)
punt_mas_bajas=n_puntuaciones_mas_baja(registros, numero)
respuesta_pl_o_sing= para_respuesta_del_test_plurar_singular_0(numero)
print(punt_mas_bajas)

''' Segunda comprobación'''
numero=1
print("\nEn este caso el número que pasamos como parámetro será: ", numero)
punt_mas_bajas=n_puntuaciones_mas_baja(registros, numero)
respuesta_pl_o_sing= para_respuesta_del_test_plurar_singular_0(numero)
print(punt_mas_bajas)




''' BLOQUE 6 '''

''' 8- Test de la primera función del bloque 6 '''

''' Primera comprobación'''
año= 2013
datos_rec_segun_año_con_clavegp= diccionario_en_año_n_con_clavegranpremio_con_su_registro(registros, año)
print("\nLos datos recopilados (año, podio, valoración) según la carrera, en el año ", año, " son:")
print(datos_rec_segun_año_con_clavegp)

''' Segunda comprobación'''
año= 2010
datos_rec_segun_año_con_clavegp= diccionario_en_año_n_con_clavegranpremio_con_su_registro(registros, año)
print("\nLos datos recopilados (año, podio, valoración) según la carrera, en el año ", año, " son:")
print(datos_rec_segun_año_con_clavegp)


''' 9- Test de la segunda función del bloque 6 '''

dic_piloto_posicion12_con_val_gp= diccionario_piloto_por_registro_en_x_piloto(registros)
print("\nLos pilotos que han quedado en primera o segunda posición con sus respectivas valoraciones y gran premio son: ")
print(dic_piloto_posicion12_con_val_gp)

''' He implementado una función más simple que carece de diccionario, pero nos devuelve el mismo resultado según el piloto
    dado como parámetro. Y nos devuelve una lista para comprobar que el resultado devuelto está correcto. Como ajuste 
    prederterminado, introduzco a Hamilton ya que es el primero que se nos delvuelve en el diccionario, así se podrá 
    comprobar a la par. Se puede cambiar el parámetro y devolverá el resultado del resto de pilotos que cumplan
    las características de la función. '''
    
piloto= "Hamilton"
prueba= comprobacion(registros, piloto)
print("Comprobación: ", prueba)

