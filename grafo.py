import random

class Grafo:
    def __init__(self, es_dirigido = False):
        self.vertices = {}
        self.cant_vertices = 0
        self.cant_aristas = 0
        self.es_dirigido = es_dirigido
        
    def __len__(self):
        return self.cant_vertices

    def __iter__(self):   
        return iter(self.vertices)

    def __str__(self):
        imp = ""
        for id, v in self.vertices.items():
            imp += f"{id}: "
            for ad in v.keys():
                imp += f"{ad} "
              
            imp += "\n"
        return imp

    def vertice_pertenece(self, id_vertice):
        return id_vertice in self.vertices 

    def agregar_vertice(self,id_vertice):
        if self.vertice_pertenece(id_vertice):
            raise ValueError("Ya existe un vertice con ese id en elgrafo")
        self.vertices[id_vertice] = {}
        self.cant_vertices += 1

    def borrar_vertice(self,id_vertice):
        if not self.vertice_pertenece(id_vertice):
            raise ValueError("No se puede eliminar un vertice que no pertenece al grafo")

        #primero saco aristas que conectan al vertice y despues el vertice

        for x in self.vertices:
            if id_vertice in self.vertices[x]:
                self.vertices[x].pop(id_vertice)

        self.vertices.pop(id_vertice)
        self.cant_vertices -= 1


    def son_adyacentes(self,id_inicio,id_fin):
        return id_fin in self.vertices[id_inicio].keys()

    def agregar_arista(self, id_inicio, id_fin, peso=None):
        if not self.vertice_pertenece(id_inicio) or not self.vertice_pertenece(id_fin):
            raise ValueError("No se puede crear arista porque alguno de los dos vertices introducidos no pertenece al grafo")
        if self.son_adyacentes(id_inicio,id_fin):
            raise ValueError("Esa arista ya esta en el grafo")
        if peso == None:
            raise ValueError("Agregar un peso")

        if id_inicio == id_fin:
            raise ValueError("No se puede crear una arista que una el mismo vertice")



        self.vertices[id_inicio][id_fin] = peso
        
        if not self.es_dirigido:
            self.vertices[id_fin][id_inicio] = peso

            self.cant_aristas += 1
        """self.cant_aristas += 1
		"""
           
    def borrar_arista(self, id_inicio, id_fin):

        if not self.vertice_pertenece(id_inicio) or not self.vertice_pertenece(id_fin):
            raise ValueError("No se puede eliminar arista porque alguno de los dos vertices introducidos no pertenece al grafo")

        if not self.son_adyacentes(id_inicio,id_fin):
                raise ValueError("Esa arista no esta en el grafo")

        self.vertices[id_inicio].pop(id_fin) #dudoso si estoy popeando bien aca o es self.vertices[id_inicio][id_fin].pop(id_fin) ?

        self.cant_aristas -= 1

        if not self.es_dirigido:
            self.vertices[id_fin].pop(id_inicio) #dudoso si estoy popeando bien aca o es self.vertices[id_fin][id_inicio].pop(id_inicio) ?
        


    def obtener_peso(self,id_inicio,id_fin):
        if not self.vertice_pertenece(id_inicio) or not self.vertice_pertenece(id_fin):
            raise ValueError("No se puede obtener peso porque alguno de los dos vertices introducidos no pertenece al grafo")

        if not self.son_adyacentes(id_inicio,id_fin):
                raise ValueError("Esa arista no esta en el grafo")

        return self.vertices[id_inicio][id_fin]

        
    def obtener_todos_vertices(self):
        lista_vertices = []
        for x in self.vertices.keys():
            lista_vertices.append(x)
        return lista_vertices

    def obtener_adyacentes(self, id_vertice):
        if not self.vertice_pertenece(id_vertice):
            raise ValueError("El vertice no existe")
        lista_adyacentes = []
        return self.vertices[id_vertice].keys()
        """lista_adyacentes.append(x)
        return lista_adyacentes"""


    def obtener_cantidad_aristas(self):
        return self.cant_aristas

    def obtener_vertice_random(self):
        #devuelve id de vertice random
        random.choice(self.vertices.keys())
