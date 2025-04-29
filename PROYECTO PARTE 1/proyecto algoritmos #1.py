class Ruta:
    def __init__(self, origen, destino, distancia_km, tiempo_horas, costo_combustible, costo_peajes, tiempo_extra_lluvia):
        self.origen = origen
        self.destino = destino
        self.distancia_km = distancia_km
        self.tiempo_horas = tiempo_horas
        self.costo_combustible = costo_combustible
        self.costo_peajes = costo_peajes
        self.tiempo_extra_lluvia = tiempo_extra_lluvia

    def __str__(self):
        return (f"Ruta de {self.origen} a {self.destino}:\n"
                f"Distancia: {self.distancia_km} km, "
                f"Tiempo: {self.tiempo_horas} horas, "
                f"Costo Combustible: ${self.costo_combustible}, "
                f"Costo Peajes: ${self.costo_peajes}, "
                f"Tiempo Extra por Lluvia: {self.tiempo_extra_lluvia} horas")

class Nodo:
    def __init__(self, ruta):
        self.ruta = ruta
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None

    def contar_elementos(self):
        contador = 0
        actual = self.cabeza
        while actual is not None:
            contador += 1
            actual = actual.siguiente
        return contador

    def imprimir_lista(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.ruta)
            print("-" * 40)
            actual = actual.siguiente

    def agregar_inicio(self, ruta):
        nuevo_nodo = Nodo(ruta)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def ordenar_lista(self):
        # Ordenar por origen alfabéticamente usando burbuja
        if self.cabeza is None:
            return
        
        cambiado = True
        while cambiado:
            cambiado = False
            actual = self.cabeza
            while actual.siguiente is not None:
                if actual.ruta.origen > actual.siguiente.ruta.origen:
                    actual.ruta, actual.siguiente.ruta = actual.siguiente.ruta, actual.ruta
                    cambiado = True
                actual = actual.siguiente

    def buscar_ruta(self, origen, destino):
        self.ordenar_lista()
        actual = self.cabeza
        while actual is not None:
            if actual.ruta.origen == origen and actual.ruta.destino == destino:
                return actual.ruta
            actual = actual.siguiente
        return None

# Parte de prueba
if __name__ == "__main__":
    lista = ListaEnlazada()

    
    ruta1 = Ruta("Bogotá", "Medellín", 415, 8, 100000, 50000, 2)
    ruta2 = Ruta("Cali", "Popayán", 138, 2.5, 40000, 20000, 0.5)
    ruta3 = Ruta("Barranquilla", "Santa Marta", 94, 1.5, 30000, 15000, 0.3)

    lista.agregar_inicio(ruta1)
    lista.agregar_inicio(ruta2)
    lista.agregar_inicio(ruta3)

    print("Lista de rutas registradas:")
    lista.imprimir_lista()

    print("Cantidad de rutas:", lista.contar_elementos())

    print("\nBuscando ruta de Bogotá a Medellín:")
    resultado = lista.buscar_ruta("Bogotá", "Medellín")
    if resultado:
        print("Ruta encontrada:\n", resultado)
    else:
        print("Ruta no encontrada.")