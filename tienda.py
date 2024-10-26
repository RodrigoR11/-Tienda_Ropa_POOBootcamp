# Clase Padre: Producto 
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self._nombre = nombre  
        self._precio = precio  
        self._cantidad = cantidad  

    # en esta parte se utiliza getter y setter para el encapsulamiento
    def obtener_nombre(self):
        return self._nombre

    def obtener_precio(self):
        return self._precio

    def obtener_cantidad(self):
        return self._cantidad

    def establecer_cantidad(self, cantidad):
        self._cantidad = cantidad

    def mostrar_info(self):
        print(f"Nombre: {self._nombre}, Precio: GS.{self._precio}, Stock: {self._cantidad}")

# Clase Hija: Ropa y hereda de la clase padre:Producto (aqui se utiliza herencia)
class Ropa(Producto):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self._talla = talla

    def obtener_talla(self):
        return self._talla

# tambien son clases hijas pero esta vez heredan la clase:Ropa (aqui se utiliza polimorfismo) 
class Camisa(Ropa):
    def mostrar_info(self):  
        super().mostrar_info()
        print(f"Talla: {self._talla} (Camisa)")

class Pantalon(Ropa):
    def mostrar_info(self):  
        super().mostrar_info()
        print(f"Talla: {self._talla} (Pantalon)")

class Zapato(Ropa):
    def __init__(self, nombre, precio, cantidad, talla, tipo):
        super().__init__(nombre, precio, cantidad, talla)
        self._tipo = tipo

    def mostrar_info(self):  
        super().mostrar_info()
        print(f"Talla: {self._talla}, Tipo: {self._tipo} (Zapato)")

# Clase: Inventario (aqui se utiliza abstracción)
class Inventario:
    def __init__(self):
        self.prendas = []

    def agregar_prenda(self, prenda):
        self.prendas.append(prenda)

    def mostrar_inventario(self):
        for idx, prenda in enumerate(self.prendas, start=1):
            print(f"{idx}. ", end="")
            prenda.mostrar_info()
            print("-" * 20)
            
# Clase Carrito: para gestionar las compras
class Carrito:
    def __init__(self):
        self.items = []

    def agregar_al_carrito(self, producto, cantidad):
        if cantidad <= producto.obtener_cantidad():
            self.items.append((producto, cantidad))
            producto.establecer_cantidad(producto.obtener_cantidad() - cantidad)
            print(f"********Se agregaron {cantidad} unidades de {producto.obtener_nombre()} al carrito.********")
        else:
            print("******** Cantidad no disponible en stock.********")

    def mostrar_resumen(self):
        total = 0
        print("*********Resumen de la compra*********")
        for item, cantidad in self.items:
            subtotal = item.obtener_precio() * cantidad
            print(f"{item.obtener_nombre()} - Cantidad: {cantidad} - Subtotal: GS.{subtotal}")
            total += subtotal
        print(f"**********Total a pagar: GS.{total}**********")

class Tienda:
    def __init__(self):
        self.inventario = Inventario()
        self.carrito = Carrito()
        self.poblar_inventario()

# En esta parte se agruegan productos al inventario
    def poblar_inventario(self):
        self.inventario.agregar_prenda(Camisa("Camisa de Hombre", 80000, 25, "M"))
        self.inventario.agregar_prenda(Camisa("Camisa de Mujer", 75000, 25, "S"))
        self.inventario.agregar_prenda(Pantalon("Pantalon de Hombre", 120000, 25, "L"))
        self.inventario.agregar_prenda(Pantalon("Pantalon de Mujer", 110000, 25, "M"))
        self.inventario.agregar_prenda(Zapato("Zapatos de Hombre", 200000, 25, "42", "Casual"))
        self.inventario.agregar_prenda(Zapato("Zapatos de Mujer", 150000, 25, "38", "Formal"))

    def mostrar_productos(self):
        print("******** Inventario de la tienda ********")
        self.inventario.mostrar_inventario()

    def agregar_al_carrito(self):
        while True:
            self.mostrar_productos()
            try:
                opcion = int(input("Seleccione el numero del producto que desea agregar al carrito (0 para salir): "))
                if opcion == 0:
                    break
                producto = self.inventario.prendas[opcion - 1]
                cantidad = int(input(f"Ingrese la cantidad de '{producto.obtener_nombre()}' a comprar: "))
                self.carrito.agregar_al_carrito(producto, cantidad)
            except (IndexError, ValueError):
                print("*****Opción invalida.(tiene que ser del 1 al 4 o tambien 0 para salir) Intente nuevamente.*****")

    def procesar_compra(self):
        self.carrito.mostrar_resumen()

if __name__ == "__main__":
    tienda = Tienda()
    print("¡Bienvenido a la Tienda de Ropa: Ropero Paraguayo!")
    
    tienda.agregar_al_carrito()
    tienda.procesar_compra()
