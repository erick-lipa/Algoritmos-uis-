#Erick Joan Lizarazo Pardo. 2231875 
#Juan Felipe Castellanos. 2231868

from bigtree import Node, print_tree, find_name, findall

# Crear la raíz del árbol (CEO)
ceo = Node("Juan Pérez", role="CEO", edad=45)

# Crear departamentos (nodos hijos)
finanzas = Node("María Gómez", role="Directora Finanzas", edad=38, parent=ceo)
ventas = Node("Carlos Ruiz", role="Director Ventas", edad=42, parent=ceo)
operaciones = Node("Laura Díaz", role="Directora Operaciones", edad=40, parent=ceo)

# Añadir empleados a finanzas
Node("Pedro Sánchez", role="Contador", edad=32, parent=finanzas)
Node("Ana López", role="Analista Financiero", edad=29, parent=finanzas)

# Añadir equipos a ventas
equipo_norte = Node("Equipo Norte", role="Equipo Regional", parent=ventas)
Node("Sofía Castro", role="Vendedor", edad=27, parent=equipo_norte)
Node("Diego Mora", role="Vendedor", edad=31, parent=equipo_norte)

equipo_sur = Node("Equipo Sur", role="Equipo Regional", parent=ventas)
Node("Marta Rojas", role="Gerente Ventas", edad=35, parent=equipo_sur)
Node("Andrés Soto", role="Vendedor", edad=28, parent=equipo_sur)

# Añadir personal a operaciones
Node("Roberto Jiménez", role="Jefe Logística", edad=37, parent=operaciones)
Node("Elena Navarro", role="Supervisora", edad=33, parent=operaciones)

# Visualizar el árbol
print_tree(ceo, attr_list=["role", "edad"])

# Buscar un nodo específico
print("\nBuscando a Marta Rojas:")
marta = find_name(ceo, "Marta Rojas")
print_tree(marta, attr_list=["role", "edad"])

# Buscar todos los vendedores
print("\nTodos los vendedores:")
vendedores = findall(ceo, lambda node: node.role == "Vendedor")
for v in vendedores:
    print(f"{v.name} ({v.role}), Edad: {v.edad}")

# Mostrar información de un nodo
print("\nInformación del CEO:")
print(f"Nombre: {ceo.name}")
print(f"Rol: {ceo.role}")
print(f"Edad: {ceo.edad}")
print(f"Hijos directos: {[child.name for child in ceo.children]}")