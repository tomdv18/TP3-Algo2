#!/usr/bin/python3
import sys
from grafo import Grafo
from genericas import bfs
import random



def parseo_archivo(ruta,grafo_likes,grafo_canciones_en_playlist, lista_usuarios):
    dict_canciones_paylist = {}
    playlist_actual = None
    canciones_playlist = []
    with open(ruta,'r') as archivo:
        archivo.readline() # salteo header
       
        for linea in archivo:
            linea = linea.rstrip('\n').split('\t')
            
            usuario = linea[1]
            lista_usuarios.append(linea[1])
            cancion = linea[2]
            artista = linea[3]
            playlist = (linea[4],linea[5])
            genero = linea[6]

            cancion_y_artista =" - ".join((cancion, artista))


            parseo_grafo_likes(grafo_likes, usuario, cancion_y_artista, artista, playlist, genero)
            if playlist[1] not in dict_canciones_paylist:
                dict_canciones_paylist[playlist[1]] = []
            dict_canciones_paylist[playlist[1]].append(cancion_y_artista)
    return dict_canciones_paylist
            


def parseo_grafo_likes(grafo, usuario, cancion, artista, playlist,genero):
    if not grafo.vertice_pertenece(usuario):
        grafo.agregar_vertice(usuario)
    if not grafo.vertice_pertenece(cancion):
        grafo.agregar_vertice(cancion)

    if not grafo.son_adyacentes(usuario, cancion):
        grafo.agregar_arista(usuario, cancion, playlist)

def parseo_grafo_canciones_en_playlist______dict(grafo, dict):
    for playlist,canciones in dict.items(): 
        for cancion in canciones:
            if not grafo.vertice_pertenece(cancion):
                grafo.agregar_vertice(cancion)
            for cancion_a_unir in canciones:
                if not grafo.vertice_pertenece(cancion_a_unir):
                    grafo.agregar_vertice(cancion_a_unir)
                if not grafo.son_adyacentes(cancion_a_unir,cancion) and cancion_a_unir != cancion:
                    grafo.agregar_arista(cancion_a_unir,cancion,playlist)


def imprimir_camino(grafo,lista, origen):
    salida = ""
    tope = len(lista)
    vertice_quitado1 = lista.pop(tope - 1)
    tope -= 1
    salida += vertice_quitado1
    while (tope > 0):
        salida += " --> aparece en playlist --> "
        vertice_quitado2 = lista.pop(tope-1)
        tope -= 1
        (id, nombre) = grafo.obtener_peso(vertice_quitado1, vertice_quitado2)
        salida += nombre + " --> de --> " + vertice_quitado2 + " --> tiene una playlist --> "  
        vertice_quitado1 = lista.pop(tope-1)
        tope -= 1
        (id, nombre) = grafo.obtener_peso(vertice_quitado2, vertice_quitado1)
        salida += nombre + " --> donde aparece --> " + vertice_quitado1
    print (salida)

def camino_mas_corto(grafo, origen, destino, lista_usuarios):
    if not grafo.vertice_pertenece(origen) or origen in lista_usuarios:
        print("Tanto el origen como el destino deben ser canciones")
        return
    if not grafo.vertice_pertenece(destino) or destino in lista_usuarios:
        print("Tanto el origen como el destino deben ser canciones")
        return
    padres, orden = bfs(grafo, origen, destino)
    lista = []
    lista.append(destino)
    vertice_ant = destino
    if not destino in padres:
        print("No se encontro recorrido")
        return
    vertice_act = padres[destino]
    lista.append(vertice_act)
    while vertice_act != origen:
        vertice_ant = vertice_act
        vertice_act = padres[vertice_ant]
        lista.append(vertice_act)
    imprimir_camino(grafo,lista,orden)


def coeficiente_clustering_individual(grafo, cancion):
    coeficiente = 0.000
    lista = grafo.obtener_adyacentes(cancion)
    valor = len(lista)
    if (valor < 2):
        return coeficiente
    valor = valor * (valor - 1)
    contador = 0.000
    for v in lista:
        for w in lista:
            if w != v:
                if grafo.son_adyacentes(v,w):
                    contador += 1.000
    coeficiente = (contador )/valor
    return coeficiente

def coeficiente_clustering(grafo, cancion = None):
    valor = 0.000
    if (cancion != None):
        if not grafo.vertice_pertenece(cancion):
            print("Esa cancion no existe en la base de datos")
            return
        valor = coeficiente_clustering_individual(grafo, cancion)
        print(f"{valor:.3f}")
        return
    lista = grafo.obtener_todos_vertices()
    i = 1
    for v in lista:
        valor = valor + coeficiente_clustering_individual(grafo, v)
    print(f"{valor/len(lista):.3f}")
    return


def es_ciclo_posible(grafo, n ,cancion):
    if len(grafo) < n or len(grafo.obtener_adyacentes(cancion)) == 1 or not grafo.vertice_pertenece(cancion):
        return False
   
    return True

def _ciclo_canciones_BT(grafo,n,cancion,visitados,lista, actual, cancion_final):
    
    if ((actual != n) and (cancion_final == cancion) and (actual != 0)): #Si ya estoy en la cancion, pero no en la cantidad de canciones necesitadas. Termino (El ultimo and es para que no pase en la primera)
        return False
    if actual > n: #Si mi actual es mas grande del ciclo que necesito, termino
        return False
    if ((actual == n - 1) and not grafo.son_adyacentes(cancion_final, cancion)): #Si me falta uno para terminar el ciclo y entre mis adyacentes no esta el que busco
        return False
    if ((actual == n) and (cancion_final == cancion)): #Si ya estoy en la cancion, con la cantidad de canciones necesitadas. Termino verdadero
        lista.append(cancion)
        return True


    for v in grafo.obtener_adyacentes(cancion):
        if (v not in visitados): 
            visitados.add(v)
            se_pudo = _ciclo_canciones_BT(grafo,n,v,visitados,lista, actual + 1,cancion_final)
            if se_pudo == True:
                lista.append(cancion)
                return True
            else:		
                visitados.remove(v)
    return se_pudo
    	
def ciclo_canciones(grafo,n,cancion):
  
    if not es_ciclo_posible(grafo,n,cancion):
        print("No se encontro recorrido")
        return

    lista = []
    visitados = set()
    actual = 0
    estado =  _ciclo_canciones_BT(grafo,n,cancion,visitados,lista, actual, cancion)
    if estado == True:
        salida= ""
        for n in lista[::-1]:
            salida += n + " --> "
        print(salida.strip(" --> "))
    else:
        print("No se encontro recorrido")

def todas_en_rango(grafo,n,cancion):
    contador = 0

    bfs_resultado = bfs(grafo,cancion)
    dict_orden = bfs_resultado[1]

    for x in dict_orden.values():
        if x == n:
            contador+=1
    
    print(contador)

def page_rank(grafo,n):
    
    #n es la cantidad de iteraciones de pagerank, se suelen obtener resultados certeros con aprox 15 iteraciones
    page_rank_dict = {}
    lista_vertices = grafo.obtener_todos_vertices()
    cantidad = len(lista_vertices)
    for vertice in lista_vertices:
        page_rank_dict[vertice] = 1.0  / cantidad 
    for i in range(n):
        for v in lista_vertices:
            page_rank_dict[v] = pagerank_vertice(grafo, v, page_rank_dict, cantidad)


    return page_rank_dict
    

def pagerank_vertice(grafo,vertice,page_rank_dict, n):
    d = 0.85 #coeficiente de amortiguación predeterminado, debe ser ente 0 y 1

    suma_a_transferir = 0
    lista = grafo.obtener_adyacentes(vertice)
    for v in lista:
        lista_2 = grafo.obtener_adyacentes(v)
        suma_a_transferir += page_rank_dict[v] / len(lista_2)
    
    

    return ((1 - d) / n) + d * suma_a_transferir

def canciones_mas_importantes(grafo,n_canciones, page_rank_lista):
    page_rank_dict = page_rank(grafo,15) 
    return page_rank_dict
    	


def imprimir_rango(page_rank_lista, n_canciones, dict_usuarios):
    i = 0
    j = 0 
    while i != n_canciones:
        if not page_rank_lista[0][j] in dict_usuarios:
            if i == n_canciones-1:
                print(f"{page_rank_lista[0][j]}")
            else:
                print(f"{page_rank_lista[0][j]};",end=" ")
            i = i + 1
        j = j + 1 

def imprimir_rango_pp(page_rank_dict, n_canciones, dict_usuarios, lista_likeadas=None):
    i = 0
    j = 0 
    while i != n_canciones:
        if not page_rank_dict[j] in dict_usuarios and page_rank_dict[j] not in lista_likeadas:
            if i == n_canciones-1:
                print(f"{page_rank_dict[j]}")
            else:
                print(f"{page_rank_dict[j]};", end=" ")
            i = i + 1
        j = j + 1 

def imprimir_rango_usuarios_pp(page_rank_dict, n_canciones, dict_usuarios,lista_likeadas = None):
    i = 0
    j = 0 
    while i != n_canciones:
        if page_rank_dict[j] in dict_usuarios and page_rank_dict[j] not in lista_likeadas:
            if i == n_canciones-1:
                print(f"{page_rank_dict[j]}")
            else:
                print(f"{page_rank_dict[j]};",end=" ")
            i = i + 1
        j = j + 1 


def page_rank_personalizado(grafo, canciones_likeadas,largo_rw,iteraciones):
    page_rank_per_dict = {}

    for i in range(iteraciones):
        for cancion in canciones_likeadas:
            actual = cancion
            camino = []
            camino.append((actual))

            for i in range(largo_rw):
                actual = random.choice(grafo.obtener_adyacentes(actual))
                camino.append(actual)
            
            valor_pr = 1 #ira cambiando con el for, empiezo con 1
            for v in camino:
                valor_pr = valor_pr / len(grafo.obtener_adyacentes(v))
                page_rank_per_dict[v] = page_rank_per_dict.get(v,0) + valor_pr

    return page_rank_per_dict


def recomendacion(grafo,n,lista,canciones_o_usuarios,lista_usuarios):
    page_rank_dict = page_rank_personalizado(grafo,lista,2000,100) 
    ordenar_mayor_a_menor = sorted(page_rank_dict, key=page_rank_dict.get, reverse=True)
    if canciones_o_usuarios == "canciones":
        imprimir_rango_pp(ordenar_mayor_a_menor,n,lista_usuarios,lista)
    else:
        imprimir_rango_usuarios_pp(ordenar_mayor_a_menor,n,lista_usuarios,lista)




def procesar_comando(grafo_likes,grafo_canciones_en_playlist,comando,parametros, page_rank_lista, lista_usuarios,dict_canciones_playlist):

    if comando == "camino":
        
        
        #Parámetros: origen y destino (separados por >>>>). Origen y destino son canciones. Se indica el autor en cada caso.

        param = parametros.split(" >>>> ")
        origen = param[0]
        destino = param[1]
        camino_mas_corto(grafo_likes, origen, destino, lista_usuarios)

    elif comando == "mas_importantes":
        
        #Parámetros: n, la cantidad de canciones más importantes a mostrar.

        n = int(parametros)

        if len(page_rank_lista) == 0:
            page_rank_dict = canciones_mas_importantes(grafo_likes, n, page_rank_lista)
            page_rank_prim =  sorted(page_rank_dict, key=page_rank_dict.get, reverse=True)
            page_rank_lista.append(page_rank_prim)

        imprimir_rango(page_rank_lista, n, lista_usuarios)
       
    elif comando == "recomendacion":

        param = parametros.split(" ")
        canciones_o_usuarios = param[0]
        n = int(param[1])
        canciones_likeadas_string = " ".join(param[2:])
        lista_canciones_likeadas = canciones_likeadas_string.split(" >>>> ")

        recomendacion(grafo_likes,n,lista_canciones_likeadas,canciones_o_usuarios,lista_usuarios)




    elif comando == "ciclo":
        if (len(grafo_canciones_en_playlist) == 0):
            parseo_grafo_canciones_en_playlist______dict(grafo_canciones_en_playlist, dict_canciones_playlist)

        param = parametros.split(" ")
        cancion = " ".join(param[1:])
        n = int(param[0])
      
       
        ciclo_canciones(grafo_canciones_en_playlist, n, cancion)

    elif comando == "rango":
        if (len(grafo_canciones_en_playlist) == 0):
            parseo_grafo_canciones_en_playlist______dict(grafo_canciones_en_playlist, dict_canciones_playlist)
        param = parametros.split(" ")
        n = int(param[0])
        cancion = " ".join(param[1:])
       
        todas_en_rango(grafo_canciones_en_playlist, n, cancion)


    elif comando == "clustering":

        if (len(grafo_canciones_en_playlist) == 0):
            parseo_grafo_canciones_en_playlist______dict(grafo_canciones_en_playlist, dict_canciones_playlist)     
        if not parametros:
            cancion = None
        else:
            cancion = parametros
       
        coeficiente_clustering(grafo_canciones_en_playlist,cancion)

    else:
        print("Entrada invalida, vuelva a intentar")



def main():
    
    grafo_likes = Grafo() #bipartito, relaciona si a un usuario le gusta una cancion (supongamos que a un usuario le gusta una cancion si armo una playlist con ella)
    grafo_canciones_en_playlist = Grafo() # relaciona canciones si aparecen en una misma playlist (al menos una playlist lista a ambas canciones).
    archivo_spotify = sys.argv[1]
    lista_usuarios = []
    page_rank_lista = []
    dict_canciones_playlist = parseo_archivo(archivo_spotify,grafo_likes,grafo_canciones_en_playlist, lista_usuarios)

    while True:
        try:
            entrada = input().rstrip('\n')
            entrada_split = entrada.split(' ')
        except EOFError:
            break
  
        comando = entrada_split[0]
        parametros = " ".join(entrada_split[1:])
        procesar_comando(grafo_likes,grafo_canciones_en_playlist,comando,parametros, page_rank_lista, lista_usuarios,dict_canciones_playlist)
 

main()
