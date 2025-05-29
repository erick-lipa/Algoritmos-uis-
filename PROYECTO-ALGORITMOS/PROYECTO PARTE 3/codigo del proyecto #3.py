class Ruta:
    def _init_(self, destino, distancia_km, tiempo_horas, costo_combustible, costo_peajes, tiempo_extra_lluvia):
        self.destino = destino
        self.distancia_km = distancia_km
        self.tiempo_horas = tiempo_horas
        self.costo_combustible = costo_combustible
        self.costo_peajes = costo_peajes
        self.tiempo_extra_lluvia = tiempo_extra_lluvia

    def _str_(self):
        return (f"Destino: {self.destino} | Distancia: {self.distancia_km} km | Tiempo: {self.tiempo_horas} h | "
                f"Costo Combustible: ${self.costo_combustible} | Costo Peajes: ${self.costo_peajes} | "
                f"Tiempo Extra aproximado por Lluvia: {self.tiempo_extra_lluvia} h")

    def sumar(self, otra_ruta):
        if self.destino == otra_ruta.destino:
            self.distancia_km += otra_ruta.distancia_km
            self.tiempo_horas += otra_ruta.tiempo_horas
            self.costo_combustible += otra_ruta.costo_combustible
            self.costo_peajes += otra_ruta.costo_peajes
            self.tiempo_extra_lluvia += otra_ruta.tiempo_extra_lluvia

    def ruta_regreso(self):
        return Ruta(self.destino, 
                    self.distancia_km * 2, 
                    self.tiempo_horas * 2, 
                    self.costo_combustible * 2, 
                    self.costo_peajes * 2, 
                    self.tiempo_extra_lluvia * 2)

class Grafo:
    def _init_(self):
        self.grafo = {}

    def agregar_ciudad(self, ciudad):
        if ciudad not in self.grafo:
            self.grafo[ciudad] = []
            print(f"Ciudad '{ciudad}' agregada al grafo.")
        else:
            print(f"La ciudad '{ciudad}' ya existe en el grafo.")

    def eliminar_ciudad(self, ciudad):
        if ciudad in self.grafo:
            self.grafo.pop(ciudad)
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

    def planificar_viaje(self, ciudades):
        if len(ciudades) < 2:
            print("Se requieren al menos dos ciudades para planificar un viaje.")
            return

        total_distancia = 0
        total_tiempo = 0
        total_costo_combustible = 0
        total_costo_peajes = 0
        total_tiempo_extra = 0

        for i in range(len(ciudades) - 1):
            origen = ciudades[i]
            destino = ciudades[i + 1]
            ruta = self.buscar_ruta_directa(origen, destino)
            if ruta:
                total_distancia += ruta.distancia_km
                total_tiempo += ruta.tiempo_horas
                total_costo_combustible += ruta.costo_combustible
                total_costo_peajes += ruta.costo_peajes
                total_tiempo_extra += ruta.tiempo_extra_lluvia
            else:
                print(f"No se encontró ruta directa de {origen} a {destino}.")
                return

        print("\nResumen del viaje:")
        print(f"Distancia total: {total_distancia} km")
        print(f"Tiempo total: {total_tiempo} h")
        print(f"Costo total de combustible: ${total_costo_combustible}")
        print(f"Costo total de peajes: ${total_costo_peajes}")
        print(f"Tiempo extra por lluvia: {total_tiempo_extra} h")

        # Crear ruta de regreso
        print("\nCreando ruta de regreso...")
        for i in range(len(ciudades) - 1, 0, -1):
            origen = ciudades[i]
            destino = ciudades[i - 1]
            ruta_regreso = self.buscar_ruta_directa(origen, destino)
            if ruta_regreso:
                ruta_regreso_doble = ruta_regreso.ruta_regreso()
                print(f"Ruta de regreso de {origen} a {destino}: {ruta_regreso_doble}")
            else:
                print(f"No se encontró ruta de regreso de {origen} a {destino}.")

# Ejemplo de uso
if _name_ == "_main_":
    asistente = Grafo()

    # Agregar ciudades
    asistente.agregar_ciudad("Bogotá")
    asistente.agregar_ciudad("Medellín")
    asistente.agregar_ciudad("Cali")
    asistente.agregar_ciudad("Cartagena")
    asistente.agregar_ciudad("Bucaramanga")

    # Agregar rutas
    asistente.agregar_ruta("Bucaramanga", "Bogotá", 394, 7, 150000, 95000, 2)
    asistente.agregar_ruta("Bogotá", "Bucaramanga", 394, 7, 150000, 95000, 1.5)
    asistente.agregar_ruta("Bogotá", "Medellín", 415, 8, 100000, 50000, 2)
    asistente.agregar_ruta("Medellín", "Cali", 420, 7, 95000, 40000, 1.5)
    asistente.agregar_ruta("Cali", "Cartagena", 600, 10, 120000, 60000, 3)
    asistente.agregar_ruta("Cartagena", "Bogotá", 1040, 18, 200000, 80000, 4)
    asistente.agregar_ruta("Medellín", "Bogotá", 415, 8, 100000, 50000, 2)
    asistente.agregar_ruta("Cali", "Medellín", 420, 7, 95000, 40000, 1.5)
    asistente.agregar_ruta("Cartagena", "Cali", 600, 10, 120000, 60000, 3)
    asistente.agregar_ruta("Bogotá", "Cartagena", 1040, 18, 200000, 80000, 4)

    # Imprimir grafo
    asistente.imprimir_grafo()

    # Planificar viaje
    ciudades_viaje = ["Bucaramanga", "Bogotá", "Medellín", "Cali"]
    asistente.planificar_viaje(ciudades_viaje)

    # Eliminar una ruta
    print("\nEliminando ruta de Medellín a Cali...")
    asistente.eliminar_ruta("Medellín", "Cali")

    asistente.imprimir_grafo()

    # Eliminar ciudad
    print("\nEliminando ciudad Cali...")
    asistente.eliminar_ciudad("Cali")

    asistente.imprimir_grafo()