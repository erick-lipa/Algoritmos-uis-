class Ruta:
    def __init__(self, destino, distancia_km, tiempo_horas, costo_combustible, costo_peajes, tiempo_extra_lluvia):
        self.destino = destino
        self.distancia_km = distancia_km
        self.tiempo_horas = tiempo_horas
        self.costo_combustible = costo_combustible
        self.costo_peajes = costo_peajes
        self.tiempo_extra_lluvia = tiempo_extra_lluvia

    def __str__(self):
        return (f"Destino: {self.destino} | Distancia: {self.distancia_km} km | Tiempo: {self.tiempo_horas} h | "
                f"Costo Combustible: ${self.costo_combustible} | Costo Peajes: ${self.costo_peajes} | "
                f"Tiempo Extra por Lluvia: {self.tiempo_extra_lluvia} h")

class Grafo:
    def __init__(self):
        # Diccionario donde clave es ciudad (nodo) y valor es lista de rutas (aristas)
        self.grafo = {}

    def agregar_ciudad(self, ciudad):
        if ciudad not in self.grafo:
            self.grafo[ciudad] = []
            print(f"Ciudad '{ciudad}' agregada al grafo.")
        else:
            print(f"La ciudad '{ciudad}' ya existe en el grafo.")

    def eliminar_ciudad(self, ciudad):
        if ciudad in self.grafo:
            # Eliminar la ciudad del grafo
            self.grafo.pop(ciudad)
            # Eliminar rutas que tengan como destino esta ciudad
            for origen in self.grafo:
                self.grafo[origen] = [ruta for ruta in self.grafo[origen] if ruta.destino != ciudad]
            print(f"Ciudad '{ciudad}' y sus rutas asociadas eliminadas.")
        else:
            print(f"La ciudad '{ciudad}' no se encuentra en el grafo.")

    def agregar_ruta(self, origen, destino, distancia_km, tiempo_horas, costo_combustible, costo_peajes, tiempo_extra_lluvia):
        if origen not in self.grafo:
            print(f"El origen '{origen}' no existe, se agrega automáticamente.")
            self.agregar_ciudad(origen)
        if destino not in self.grafo:
            print(f"El destino '{destino}' no existe, se agrega automáticamente.")
            self.agregar_ciudad(destino)

        # Verificar si ya existe una ruta igual para evitar duplicados
        for ruta in self.grafo[origen]:
            if ruta.destino == destino:
                print(f"Ruta de {origen} a {destino} ya existe. Actualizando datos...")
                ruta.distancia_km = distancia_km
                ruta.tiempo_horas = tiempo_horas
                ruta.costo_combustible = costo_combustible
                ruta.costo_peajes = costo_peajes
                ruta.tiempo_extra_lluvia = tiempo_extra_lluvia
                return

        nueva_ruta = Ruta(destino, distancia_km, tiempo_horas, costo_combustible, costo_peajes, tiempo_extra_lluvia)
        self.grafo[origen].append(nueva_ruta)
        print(f"Ruta de {origen} a {destino} agregada.")

    def eliminar_ruta(self, origen, destino):
        if origen in self.grafo:
            rutas_previas = len(self.grafo[origen])
            self.grafo[origen] = [ruta for ruta in self.grafo[origen] if ruta.destino != destino]
            if len(self.grafo[origen]) < rutas_previas:
                print(f"Ruta de {origen} a {destino} eliminada.")
            else:
                print(f"No se encontró ruta de {origen} a {destino} para eliminar.")
        else:
            print(f"No existe la ciudad origen '{origen}' en el grafo.")

    def buscar_ruta_directa(self, origen, destino):
        if origen not in self.grafo:
            print(f"Ciudad origen '{origen}' no existe en el grafo.")
            return None
        for ruta in self.grafo[origen]:
            if ruta.destino == destino:
                return ruta
        return None

    def imprimir_grafo(self):
        print("Grafo de ciudades y rutas:")
        for ciudad, rutas in self.grafo.items():
            print(f"\nCiudad: {ciudad}")
            if rutas:
                for ruta in rutas:
                    print(f"  -> {ruta}")
            else:
                print("  (Sin rutas)")

# Ejemplo de uso
if __name__ == "__main__":
    asistente = Grafo()

    # Agregar ciudades
    asistente.agregar_ciudad("Bogotá")
    asistente.agregar_ciudad("Medellín")
    asistente.agregar_ciudad("Cali")

    # Agregar rutas
    asistente.agregar_ruta("Bogotá", "Medellín", 415, 8, 100000, 50000, 2)
    asistente.agregar_ruta("Medellín", "Cali", 420, 7, 95000, 40000, 1.5)
    asistente.agregar_ruta("Bogotá", "Cali", 464, 9, 130000, 70000, 2)

    # Imprimir grafo
    asistente.imprimir_grafo()

    # Buscar ruta directa
    print("\nBuscando ruta directa de Bogotá a Medellín:")
    ruta = asistente.buscar_ruta_directa("Bogotá", "Medellín")
    if ruta:
        print(ruta)
    else:
        print("Ruta no encontrada.")

    # Eliminar una ruta
    print("\nEliminando ruta de Medellín a Cali...")
    asistente.eliminar_ruta("Medellín", "Cali")

    asistente.imprimir_grafo()

    # Eliminar ciudad
    print("\nEliminando ciudad Cali...")
    asistente.eliminar_ciudad("Cali")

    asistente.imprimir_grafo()