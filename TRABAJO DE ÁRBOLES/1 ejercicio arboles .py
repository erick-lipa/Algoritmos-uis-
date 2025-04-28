#Erick Joan Lizarazo Pardo. 2231875 
#Juan Felipe Castellanos. 2231868

import heapq
from collections import defaultdict

def calcular_frecuencias(texto):
    frecuencias = defaultdict(int)
    for caracter in texto:
        frecuencias[caracter] += 1
    return frecuencias

def construir_arbol(frecuencias):
    heap = [[peso, [caracter, ""]] for caracter, peso in frecuencias.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for par in lo[1:]:
            par[1] = '0' + par[1]
        for par in hi[1:]:
            par[1] = '1' + par[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    
    return heap[0]

def generar_codigos(nodos):
    return {caracter: codigo for caracter, codigo in nodos[1:]}

# Ejemplo de uso
texto = "ABRACADABRA"
frecuencias = calcular_frecuencias(texto)
arbol = construir_arbol(frecuencias)
codigos = generar_codigos(arbol)

print("Códigos de Huffman:")
for char, code in codigos.items():
    print(f"'{char}': {code}")
