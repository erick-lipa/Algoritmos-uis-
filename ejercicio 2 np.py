import numpy as np

def generar_datos_estudiantes(n):
    """Genera datos de prueba con código, nombre, carrera, promedio y año de ingreso."""
    np.random.seed(42)  # Para reproducibilidad
    codigos = np.arange(10001, 10001 + n)
    nombres = np.array([f"Estudiante_{i}" for i in range(n)])
    carreras = np.random.randint(1, 20, n)  # Suponiendo 20 códigos de carrera
    promedios = np.round(np.random.uniform(2.5, 5.0, n), 2)
    anios_ingreso = np.random.randint(1980, 2025, n)
    
    return np.column_stack((codigos, nombres, carreras, promedios, anios_ingreso))

def listar_estudiantes_carrera(estudiantes, codigo_carrera):
    """Lista estudiantes de una carrera con promedio >= 4."""
    filtrados = estudiantes[(estudiantes[:, 2].astype(int) == codigo_carrera) & (estudiantes[:, 3].astype(float) >= 4.0)]
    
    print("\nEstudiantes con promedio >= 4 en la carrera", codigo_carrera)
    for est in filtrados:
        print(f"Código: {est[0]}, Nombre: {est[1]}")
    print(f"Total: {len(filtrados)}")

def listar_condicionales_pre90(estudiantes):
    """Lista estudiantes que ingresaron antes de 1990 y están condicionales (<3.0)."""
    filtrados = estudiantes[(estudiantes[:, 4].astype(int) < 1990) & (estudiantes[:, 3].astype(float) < 3.0)]
    
    print("\nEstudiantes condicionales que ingresaron antes de 1990:")
    for est in filtrados:
        print(f"Código: {est[0]}, Nombre: {est[1]}")
    print(f"Total: {len(filtrados)}")

# Generar datos ficticios para 6500 estudiantes
estudiantes = generar_datos_estudiantes(6500)

# Leer código de carrera a listar
codigo_carrera = int(input("Ingrese el código de la carrera a listar: "))
listar_estudiantes_carrera(estudiantes, codigo_carrera)

# Listar estudiantes condicionales antes de 1990
listar_condicionales_pre90(estudiantes)
