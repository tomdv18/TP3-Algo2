from grafo import Grafo


#==============================================================================
# Empiezan las pruebas
# Quiza haaya qye hacer otro archivo, pero me es mas practico probar aca
# Talvez falte alguna prueba de volumen

def prueba_crear_grafo():
	grafo = Grafo ()
	cantidad = len(grafo)
	if cantidad == 0:
		print ("\033[1;37m " + "Grafo inicializado, cantidad correcta " +"\033[1;32m "+ "Ok")
	if cantidad != 0:
		print ("\033[1;37m " + "Grafo inicializado, cantidad correcta " + "\033[1;31m " + "Error" )
# No puedo entender bien porque esto no me funciona



def prueba_agregar_vertice():
	grafo = Grafo()
	vertice = 1
	grafo.agregar_vertice(vertice)
	pertenece = grafo.vertice_pertenece(vertice)
	if (pertenece):
		print ("\033[1;37m " + "Prueba vertice pertence correcta " +"\033[1;32m "+ "Ok")
	else:
		print ("\033[1;37m " + "Prueba vertice pertence correcta " +"\033[1;31m "+ "Error")
	cantidad = len(grafo)
	if cantidad == 1:
		print ("\033[1;37m " + "Vertice iniciado, cantidad correcta" +"\033[1;32m "+ "Ok")
	if cantidad != 1:
		print ("\033[1;37m " + "Vertice iniciado, cantidad correcta" +"\033[1;31m "+ "Error")



def prueba_agregar_quitar():
	grafo = Grafo()
	vertice = 1
	grafo.agregar_vertice(vertice)
	grafo.borrar_vertice(vertice)
	cantidad = len(grafo)
	if cantidad == 0:
		print ("\033[1;37m " + "Vertice quitado, cantidad correcta" +"\033[1;32m "+ "Ok")
	if cantidad != 0:
		print ("\033[1;37m " + "Vertice quitado, cantidad correcta" +"\033[1;31m "+ "Error")
	pertenece = grafo.vertice_pertenece(vertice)
	if (pertenece):
		print ("\033[1;37m " + "Vertice eliminado, ya no pertenece" +"\033[1;31m "+ "Error")
	else:
		print ("\033[1;37m " + "Vertice eliminado, ya no pertenece" +"\033[1;32m "+ "Ok")

def prueba_aniadir_arista():
	grafo = Grafo()
	vertice = 1
	vertice2 = 2
	grafo.agregar_vertice(vertice)
	grafo.agregar_vertice(vertice2)
	cantidad = len(grafo)
	if cantidad == 2:
		print ("\033[1;37m " + "Vertices agregados, cantidad correcta" +"\033[1;32m "+ "Ok")
	if cantidad != 2:
		print ("\033[1;37m " + "Vertice eliminado, cantidad correcta" +"\033[1;31m "+ "Error")
		return
	grafo.agregar_arista(vertice, vertice2, 1)
	lista = grafo.obtener_adyacentes(vertice)
	#Como forma de verificacion podriamos buscar en la lista al vertice
	if (vertice2 in lista):
		print ("\033[1;37m " + "Arista agregada, Vinculo correcto" +"\033[1;32m "+ "Ok")
	else:
		print ("\033[1;37m " + "Arista agregada, Vinculo correcto" +"\033[1;31m "+ "Error")


#Esta prueba verifica que si un grafo es dirigido
#Un vertice debe tener como adyacente a la otra arista
#pero la arista 2 no debe tener al primero:
def prueba_aniadir_arista_grafo_dirigido():
	verdadero = True
	grafo = Grafo(verdadero)
	vertice = 1
	vertice2 = 2
	grafo.agregar_vertice(vertice)
	grafo.agregar_vertice(vertice2)

	grafo.agregar_arista(vertice, vertice2, 1)
	lista = grafo.obtener_adyacentes(vertice)
	if (vertice2 in lista):
		print ("\033[1;37m " + "Arista dirigida agregada , Vinculo correcto" +"\033[1;32m "+ "Ok")
	else:
		print ("\033[1;37m " + "Arista dirigida agregada , Vinculo correcto" +"\033[1;31m "+ "Error")
	lista = grafo.obtener_adyacentes(vertice2)
	if (vertice in lista):
		print ("\033[1;37m " + "Arista dirigida agregada , Vinculo incorrecto" +"\033[1;31m "+ "Error")
	else:
		print ("\033[1;37m " + "Arista dirigida agregada , Vinculo correcto" +"\033[1;32m "+ "Ok")

	

def prueba_quitar_arista():
	grafo = Grafo()
	vertice = 1
	vertice2 = 2
	grafo.agregar_vertice(vertice)
	grafo.agregar_vertice(vertice2)
	grafo.agregar_arista(vertice, vertice2, 1)
	grafo.borrar_arista(vertice, vertice2)
	lista = grafo.obtener_adyacentes(vertice)
	if (vertice2 not in lista):
		print ("\033[1;37m " + "Arista eliminada correctamente" +"\033[1;32m "+ "Ok")
	else:
		print ("\033[1;37m " + "Arista eliminada correctamente" +"\033[1;31m "+ "Error")




def prueba_grafo_pesado():
	grafo = Grafo()
	vertice = 1
	vertice2 = 2
	grafo.agregar_vertice(vertice)
	grafo.agregar_vertice(vertice2)
	grafo.agregar_arista(vertice, vertice2, 7)
	peso = grafo.obtener_peso(vertice, vertice2)
	if (peso == 7):
		print ("\033[1;37m " + "Peso de aristas correcto" +"\033[1;32m "+ "Ok")
	else:
		print ("\033[1;37m " + "Peso de aristas correcto" +"\033[1;31m "+ "Error")

def prueba_varias_aristas():
	grafo = Grafo()
	vertice = 1
	vertice2 = 7
	vertice3 = 2
	vertice4 = 5
	vertice5 = 18
	grafo.agregar_vertice(vertice)
	grafo.agregar_vertice(vertice2)
	grafo.agregar_vertice(vertice3)
	grafo.agregar_vertice(vertice4)
	grafo.agregar_vertice(vertice5)
	grafo.agregar_arista(vertice, vertice2,1)
	grafo.agregar_arista(vertice, vertice3,1)
	grafo.agregar_arista(vertice, vertice4,1)
	grafo.agregar_arista(vertice, vertice5,1)
	lista = grafo.obtener_adyacentes(vertice)
	pertenece = True
	if vertice2 not in lista:
		pertence = False
	if vertice3 not in lista:
		pertence = False
	if vertice4 not in lista:
		pertence = False
	if vertice5 not in lista:
		pertence = False
	if (pertenece == True):
		print ("\033[1;37m " + "Varios vertices agregados, todas conectados" +"\033[1;32m "+ "Ok")
	else:
		print ("\033[1;37m " + "Varios vertices agregados, todas conectados" +"\033[1;31m "+ "Error")

def prueba_enlistar_varias_aristas():
	grafo = Grafo()
	vertice = 1
	vertice2 = 7
	vertice3 = 2
	vertice4 = 5
	vertice5 = 18
	vertice6 = 2000
	vertice7 = 148
	vertice8 = 185
	vertice9 = 183
	vertice10 = 218
	grafo.agregar_vertice(vertice)
	grafo.agregar_vertice(vertice2)
	grafo.agregar_vertice(vertice3)
	grafo.agregar_vertice(vertice4)
	grafo.agregar_vertice(vertice5)
	grafo.agregar_vertice(vertice6)
	grafo.agregar_vertice(vertice7)
	grafo.agregar_vertice(vertice8)
	grafo.agregar_vertice(vertice9)
	grafo.agregar_vertice(vertice10)
	lista = grafo.obtener_todos_vertices()

	pertenece = True
	if vertice not in lista:
		pertence = False
	if vertice2 not in lista:
		pertence = False
	if vertice3 not in lista:
		pertence = False
	if vertice4 not in lista:
		pertence = False
	if vertice5 not in lista:
		pertence = False	
	if vertice6 not in lista:
		pertence = False	
	if vertice7 not in lista:
		pertence = False	
	if vertice8 not in lista:
		pertence = False	
	if vertice9 not in lista:
		pertence = False	
	if vertice10 not in lista:
		pertence = False
	if (pertenece == True):
		print ("\033[1;37m " + "Varios vertices agregados, todos parte del grafo" +"\033[1;32m "+ "Ok")
	else:
		print ("\033[1;37m " + "Varios vertices agregados, todos parte del grafo" +"\033[1;31m "+ "Error")



def prueba_imprimir():
	grafo = Grafo()
	vertice = 1
	vertice2 = 2
	vertice3 = 3
	vertice4 = 4
	vertice5 = 5

	grafo.agregar_vertice(vertice)
	grafo.agregar_vertice(vertice2)
	grafo.agregar_vertice(vertice3)
	grafo.agregar_vertice(vertice4)
	grafo.agregar_vertice(vertice5)
	grafo.agregar_arista(vertice, vertice2, 1)
	grafo.agregar_arista(vertice, vertice3, 1)
	grafo.agregar_arista(vertice2, vertice4, 1)
	str(grafo)

"""
Habria que agregar pruebas para usar el iterador
"""

"""
def prueba_colores():
	print ("\033[1;34m " + "Bokita el mas grande")
	print ("\033[1;33m " + "Bokita el mas grande")
	print ("\033[1;34m " + "Bokita el mas grande")

"""

def pruebas_estudiantes():
	prueba_crear_grafo()
	prueba_agregar_vertice()
	prueba_agregar_quitar()
	prueba_aniadir_arista()
	prueba_aniadir_arista_grafo_dirigido()
	prueba_quitar_arista()
	prueba_grafo_pesado()
	prueba_varias_aristas()
	prueba_enlistar_varias_aristas()
	print ("\033[1;37m ")
	prueba_imprimir()

pruebas_estudiantes()