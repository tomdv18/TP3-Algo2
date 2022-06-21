"""
ESTE ARCHIVO TIENE FUNCIONES GENERICAS QUE DESPUES PODRIAMOS ADAPTAR DE ALGUNA FORMA
"""
from collections import deque
import heapq


def dfs(grafo, v, visitados, padres, origen):
	for w in grafo.adyacentes(v):
		if w not in visitados:
			visitados.add(w)
			padres[w] = v
			orden[w] = orden[v] + 1
			dfs(grafo, w, visitados, padres, orden)


def dfs_completo(grafo):
	visitados = set ()
	padres = {}
	orden = {}
	for v in grafo:
		if v not in visitados:
			visitados.add(v)
			padres[v] = None
			orden[v] = 0
			dfs(grafo, v, visitados, padres, orden)
	return padres, orden

def bfs(grafo, origen, limite = None):
	visitados = set ()
	padres = {}
	orden = {}
	padres[origen] = None
	orden[origen] = 0
	visitados.add(origen)
	q = deque()
	q.append(origen)
	while ((len(q)) != 0):
		#print(orden)
		v = q.popleft()
		if (v == limite):
			return padres, orden 

		
		for w in grafo.obtener_adyacentes(v):
			if w not in visitados:
				padres[w] = v
				orden[w] = orden[v] + 1
				visitados.add(w)
				q.append(w)
	
	return padres, orden 

	


"""
Si el grafo no es 100 porciento conexo, quedarian vertices con distancia infinita
"""
def camino_minimo_dijkstra(grafo, origen):
	distancia = {}
	padre = {}
	for v in grafo:
		distancia[v] = inf
	distancia[origen] = 0
	padre[origen] = None
	heap = []
	heapq.heappush(heap, (origen, 0))
	while (len(heap) != 0):
		v = heapq.heappop(heap)
		for w in grafo.adyacentes(v):
			if (distancia[w] + grafo.obtener_peso(v, w) < distancia[w]):
				distancia[w] = distancia[v] + grafo.peso(v,w)
				padre[w] = v
				heap.heappush(heap, (w, distancia[w]))

	return padre, distancia

