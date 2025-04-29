class Producto:
    def __init__(self, codigo, nombre, cantidad, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


class Nodo:
    def __init__(self, producto):
        self.producto = producto
        self.izquierda = None
        self.derecha = None


class ArbolInventario:
    def __init__(self):
        self.raiz = None

    # Insertar producto en el árbol
    def insertar(self, producto):
        if self.raiz is None:
            self.raiz = Nodo(producto)
        else:
            self._insertar(self.raiz, producto)

    def _insertar(self, nodo_actual, producto):
        if producto.codigo < nodo_actual.producto.codigo:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(producto)
            else:
                self._insertar(nodo_actual.izquierda, producto)
        elif producto.codigo > nodo_actual.producto.codigo:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(producto)
            else:
                self._insertar(nodo_actual.derecha, producto)
        else:
            print(f"Producto con código {producto.codigo} ya existe. No se insertó.")

    # Buscar producto por código
    def buscar(self, codigo):
        return self._buscar(self.raiz, codigo)

    def _buscar(self, nodo_actual, codigo):
        if nodo_actual is None:
            return None
        if codigo == nodo_actual.producto.codigo:
            return nodo_actual.producto
        elif codigo < nodo_actual.producto.codigo:
            return self._buscar(nodo_actual.izquierda, codigo)
        else:
            return self._buscar(nodo_actual.derecha, codigo)

    # Actualizar cantidad de stock
    def actualizar_cantidad(self, codigo, nueva_cantidad):
        producto = self.buscar(codigo)
        if producto:
            producto.cantidad = nueva_cantidad
            print(f"Cantidad actualizada: {producto}")
        else:
            print(f"Producto con código {codigo} no encontrado.")

    # Eliminar un producto del árbol
    def eliminar(self, codigo):
        self.raiz = self._eliminar(self.raiz, codigo)

    def _eliminar(self, nodo_actual, codigo):
        if nodo_actual is None:
            return None
        if codigo < nodo_actual.producto.codigo:
            nodo_actual.izquierda = self._eliminar(nodo_actual.izquierda, codigo)
        elif codigo > nodo_actual.producto.codigo:
            nodo_actual.derecha = self._eliminar(nodo_actual.derecha, codigo)
        else:
            # Nodo encontrado
            if nodo_actual.izquierda is None:
                return nodo_actual.derecha
            elif nodo_actual.derecha is None:
                return nodo_actual.izquierda

            # Nodo con dos hijos
            min_valor_nodo = self._minimo_nodo(nodo_actual.derecha)
            nodo_actual.producto = min_valor_nodo.producto
            nodo_actual.derecha = self._eliminar(nodo_actual.derecha, min_valor_nodo.producto.codigo)
        return nodo_actual

    def _minimo_nodo(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual

    # Mostrar el inventario (ordenado por código)
    def mostrar_inventario(self):
        print("Inventario de Productos:")
        self._inorden(self.raiz)

    def _inorden(self, nodo_actual):
        if nodo_actual:
            self._inorden(nodo_actual.izquierda)
            print(nodo_actual.producto)
            self._inorden(nodo_actual.derecha)


# Parte de prueba
if __name__ == "__main__":
    inventario = ArbolInventario()

    # Insertar productos
    inventario.insertar(Producto(1001, "Camisa", 50, 80000))
    inventario.insertar(Producto(1005, "Pantalón", 30, 120000))
    inventario.insertar(Producto(1003, "Chaqueta", 20, 200000))
    inventario.insertar(Producto(1002, "Zapatos", 40, 150000))
    inventario.insertar(Producto(1004, "Bufanda", 60, 50000))

    # Mostrar inventario
    inventario.mostrar_inventario()

    print("\nBuscando el producto con código 1003:")
    producto_encontrado = inventario.buscar(1003)
    if producto_encontrado:
        print(producto_encontrado)
    else:
        print("Producto no encontrado.")

    print("\nActualizando cantidad del producto con código 1002:")
    inventario.actualizar_cantidad(1002, 35)

    print("\nEliminando producto con código 1005:")
    inventario.eliminar(1005)

    print("\nInventario actualizado:")
    inventario.mostrar_inventario()