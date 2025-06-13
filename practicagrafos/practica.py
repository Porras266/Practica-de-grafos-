"""Construcción y Operaciones Básicas de un Grafo 
Andres,Allysson y Nicole """

class Grafo:
    def __init__(self,es_dirigido=False):
        self.grafo = {}
        self.es_dirigido = es_dirigido

    def agregar_vertice(self,vertice):
        if vertice  not in self.grafo :
            self.grafo[vertice ] = []

    def agregar_arista (self,u,v,peso=1):
            self.agregar_vertice(u)
            self.agregar_vertice(v)

            # Añade la arista de u a v
            self.grafo[u].append((v, peso))
            

            # Si el grafo no es dirigido, también de v a u
            if not self.es_dirigido:
                self.grafo[v].append((u, peso))
                

    def obtener_vecinos(self,vertice):
         #Devuelve una lista de todos los vértices adyacentes a vertice.
         return self.grafo.get(vertice, [])
         
    def existe_arista(self,u,v):
    # Devuelve True si existe una arista entre u y v,False en caso contrario.
             if u in self.grafo:
                  for vecino, _ in self.grafo[u]:
                       if vecino == v:
                            return True 
             return False          

          

                     



         






      
