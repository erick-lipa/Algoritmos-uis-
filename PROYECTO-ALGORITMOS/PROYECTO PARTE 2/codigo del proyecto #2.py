class NodoLista:
    def __init__(self, ciudad_origen, ciudad_destino, distancia_km, tiempo_hr, costo_combustible, peajes):
        self.ciudad_origen = ciudad_origen
        self.ciudad_destino = ciudad_destino
        self.distancia_km = distancia_km
        self.tiempo_hr = tiempo_hr
        self.costo_combustible = costo_combustible
        self.peajes = peajes
        self.siguiente = None

class ListaViajes:
    def __init__(self):
        self.inicio = None

    def lista_vacia(self):
        return self.inicio is None

    def contar_elementos(self):
        contador = 0
        actual = self.inicio
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    def imprimir_lista(self):
        actual = self.inicio
        if not actual:
            print("La lista está vacía.")
            return
        while actual:
            print(f"Origen: {actual.ciudad_origen} -> Destino: {actual.ciudad_destino}")
            print(f"Distancia: {actual.distancia_km} km | Tiempo: {actual.tiempo_hr} hrs")
            print(f"Costo de Combustible: ${actual.costo_combustible} | Peajes: ${actual.peajes}")
            print("-" * 40)
            actual = actual.siguiente

    def agregar_inicio(self, ciudad_origen, ciudad_destino, distancia_km, tiempo_hr, costo_combustible, peajes):
        nuevo = NodoLista(ciudad_origen, ciudad_destino, distancia_km, tiempo_hr, costo_combustible, peajes)
        nuevo.siguiente = self.inicio
        self.inicio = nuevo

    def buscar_viaje(self, ciudad_origen, ciudad_destino):
        viajes = []
        actual = self.inicio
        while actual:
            viajes.append(actual)
            actual = actual.siguiente

        viajes.sort(key=lambda x: (x.ciudad_origen.lower(), x.ciudad_destino.lower()))

        inicio = 0
        fin = len(viajes) - 1
        while inicio <= fin:
            medio = (inicio + fin) // 2
            viaje = viajes[medio]
            if viaje.ciudad_origen == ciudad_origen and viaje.ciudad_destino == ciudad_destino:
                return viaje
            elif (viaje.ciudad_origen, viaje.ciudad_destino) < (ciudad_origen, ciudad_destino):
                inicio = medio + 1
            else:
                fin = medio - 1
        return None

class NodoArbol:
    def __init__(self, ciudad):
        self.ciudad = ciudad
        self.izquierda = None
        self.derecha = None

class ArbolCiudadesVisitadas:
    def __init__(self):
        self.raiz = None

    def insertar(self, ciudad):
        self.raiz = self._insertar_rec(self.raiz, ciudad)

    def _insertar_rec(self, nodo, ciudad):
        if nodo is None:
            return NodoArbol(ciudad)
        if ciudad.lower() < nodo.ciudad.lower():
            nodo.izquierda = self._insertar_rec(nodo.izquierda, ciudad)
        elif ciudad.lower() > nodo.ciudad.lower():
            nodo.derecha = self._insertar_rec(nodo.derecha, ciudad)
        return nodo

    def buscar(self, ciudad):
        return self._buscar_rec(self.raiz, ciudad)

    def _buscar_rec(self, nodo, ciudad):
        if nodo is None:
            return False
        if ciudad.lower() == nodo.ciudad.lower():
            return True
        elif ciudad.lower() < nodo.ciudad.lower():
            return self._buscar_rec(nodo.izquierda, ciudad)
        else:
            return self._buscar_rec(nodo.derecha, ciudad)

    def imprimir_inorden(self):
        self._inorden_rec(self.raiz)

    def _inorden_rec(self, nodo):
        if nodo:
            self._inorden_rec(nodo.izquierda)
            print(f"Ciudad visitada: {nodo.ciudad}")
            self._inorden_rec(nodo.derecha)

#  Parte de Prueba 

if __name__ == "__main__":
    lista_viajes = ListaViajes()
    ciudades_visitadas = ArbolCiudadesVisitadas()

    # Agregar algunos viajes de ejemplo
    lista_viajes.agregar_inicio("Bogotá", "Medellín", 415, 8, 120000, 60000)
    lista_viajes.agregar_inicio("Bogotá", "Cali", 464, 9, 130000, 70000)
    lista_viajes.agregar_inicio("Medellín", "Cartagena", 642, 12, 160000, 80000)

    # Agregar ciudades visitadas
    ciudades_visitadas.insertar("Bogotá")
    ciudades_visitadas.insertar("Medellín")
    ciudades_visitadas.insertar("Cali")
    ciudades_visitadas.insertar("Cartagena")

    print("\n--- Lista de Viajes ---")
    lista_viajes.imprimir_lista()

    print("\n--- Buscar Viaje ---")
    busqueda = lista_viajes.buscar_viaje("Bogotá", "Cali")
    if busqueda:
        print(f"Viaje encontrado: {busqueda.ciudad_origen} -> {busqueda.ciudad_destino}")
    else:
        print("Viaje no encontrado.")

    print("\n--- Ciudades Visitadas (en orden) ---")
    ciudades_visitadas.imprimir_inorden()

    print("\n--- Buscar Ciudad Visitada ---")
    ciudad_a_buscar = "Cali"
    if ciudades_visitadas.buscar(ciudad_a_buscar):
        print(f"{ciudad_a_buscar} fue visitada.")
    else:
        print(f"{ciudad_a_buscar} no fue visitada.")