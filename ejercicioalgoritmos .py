import numpy as np

# Generar votos aleatorios entre 0 y 5000 para los 30 candidatos
np.random.seed(42)  # Fijar la semilla para resultados reproducibles
votos = np.random.randint(0, 5001, 30)

# Crear un array con los números de los candidatos (del 1 al 30)
candidatos = np.arange(1, 31)

# Combinar los datos en una lista de tuplas y ordenarlos por los votos en orden descendente
resultados = sorted(zip(candidatos, votos), key=lambda x: x[1], reverse=True)

# Imprimir resultados ordenados
print("Candidato | Votos")
print("-----------------")
for candidato, voto in resultados:
    print(f"   {candidato:2d}     |  {voto:4d}")