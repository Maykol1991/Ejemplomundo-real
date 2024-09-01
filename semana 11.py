import json

# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    # Métodos para obtener y establecer atributos
    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio


# Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = {}  # Usamos un diccionario para almacenar los productos

    def añadir_producto(self, producto):
        if producto.id_producto in self.productos:
            print("Error: El producto ya existe en el inventario.")
        else:
            self.productos[producto.id_producto] = producto
            print(f"Producto {producto.nombre} añadido al inventario.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(f"Producto con ID {id_producto} eliminado del inventario.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        if id_producto in self.productos:
            if nueva_cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                self.productos[id_producto].actualizar_precio(nuevo_precio)
            print(f"Producto con ID {id_producto} actualizado.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        encontrados = [str(p) for p in self.productos.values() if p.nombre.lower() == nombre.lower()]
        if encontrados:
            print("Productos encontrados:")
            for producto in encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos_los_productos(self):
        if self.productos:
            print("Inventario completo:")
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

    # Funciones para almacenamiento en archivos
    def guardar_inventario(self, nombre_archivo):
        with open(nombre_archivo, 'w') as archivo:
            inventario_serializado = {id_producto: vars(producto) for id_producto, producto in self.productos.items()}
            json.dump(inventario_serializado, archivo)
            print(f"Inventario guardado en {nombre_archivo}.")

    def cargar_inventario(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as archivo:
                inventario_serializado = json.load(archivo)
                self.productos = {id_producto: Producto(**datos) for id_producto, datos in inventario_serializado.items()}
                print(f"Inventario cargado desde {nombre_archivo}.")
        except FileNotFoundError:
            print(f"Error: El archivo {nombre_archivo} no existe.")


# Interfaz de Usuario
def menu():
    inventario = Inventario()

    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Cargar inventario")
        print("8. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == '2':
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            id_producto = input("ID del producto a actualizar: ")
            nueva_cantidad = input("Nueva cantidad (deja en blanco si no deseas actualizar): ")
            nuevo_precio = input("Nuevo precio (deja en blanco si no deseas actualizar): ")
            inventario.actualizar_producto(id_producto, int(nueva_cantidad) if nueva_cantidad else None, float(nuevo_precio) if nuevo_precio else None)

        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == '5':
            inventario.mostrar_todos_los_productos()

        elif opcion == '6':
            nombre_archivo = input("Nombre del archivo para guardar el inventario: ")
            inventario.guardar_inventario(nombre_archivo)

        elif opcion == '7':
            nombre_archivo = input("Nombre del archivo para cargar el inventario: ")
            inventario.cargar_inventario(nombre_archivo)

        elif opcion == '8':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    menu()
