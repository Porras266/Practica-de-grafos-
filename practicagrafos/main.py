from practica import Grafo

# prueba de Implementacion 



# === INTERACCIÓN CON EL USUARIO ===

def crear_grafo_desde_usuario():
    tipo = input("¿El grafo es dirigido? (s/n): ").strip().lower()
    dirigido = tipo == 's'
    #  instancia del Grafo según la respuesta
    g = Grafo(es_dirigido=dirigido)

    print("\n=== Agregar vértices ===")
    vertices = input("Introduce los vértices separados por comas (ej. A,B,C,D,E): ")
    for v in vertices.split(','):
        g.agregar_vertice(v.strip())



    # Solicita las aristas una por una hasta que se escriba "fin"
    print("\n=== Agregar aristas ===")
    while True:
        entrada = input("Introduce una arista (formato: u,v) o escribe 'fin' para terminar: ")
        if entrada.lower() == 'fin':
            break
        try:
            u, v = entrada.split(',')
            g.agregar_arista(u.strip(), v.strip())
        except:
            print("Formato incorrecto. Usa: u,v")

    print("\n=== Consultar vecinos ===")
    while True:
        vertice = input("Introduce un vértice para ver sus vecinos (o 'fin'): ")
        if vertice.lower() == 'fin':
            break
        print("Vecinos de", vertice, ":", g.obtener_vecinos(vertice.strip()))

    print("\n=== Verificar aristas ===")
    while True:
        entrada = input("Introduce dos vértices para verificar arista (formato: u,v) o 'fin': ")
        if entrada.lower() == 'fin':
            break
        try:
            u, v = entrada.split(',')
            existe = g.existe_arista(u.strip(), v.strip())
            print(f"¿Existe arista ({u.strip()}, {v.strip()})?:", existe)
        except:
            print("Formato incorrecto. Usa: u,v")

# Ejecutar el programa
if __name__ == "__main__":
    crear_grafo_desde_usuario()



