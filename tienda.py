from abc import ABC, abstractmethod
from producto import Producto

class Tienda(ABC):
    """Clase abstracta que representa una tienda."""

    def __init__(self, nombre, costo_delivery):
        """Inicializa una nueva tienda.

        Args:
            nombre (str): El nombre de la tienda.
            costo_delivery (float): El costo de delivery de la tienda.
        """
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    @property
    def nombre(self):
        """str: El nombre de la tienda."""
        return self.__nombre

    @property
    def costo_delivery(self):
        """float: El costo de delivery de la tienda."""
        return self.__costo_delivery

    @property
    def productos(self):
        """list: Lista de productos de la tienda."""
        return self.__productos

    @abstractmethod
    def ingresar_producto(self, producto):
        """Método abstracto para ingresar un producto a la tienda."""
        pass

    @abstractmethod
    def listar_productos(self):
        """Método abstracto para listar los productos de la tienda."""
        pass

    @abstractmethod
    def realizar_venta(self, nombre_producto, cantidad):
        """Método abstracto para realizar una venta en la tienda."""
        pass

class Restaurante(Tienda):
    """Clase que representa un restaurante."""

    def ingresar_producto(self, producto):
        """Método para ingresar un producto al restaurante."""
        for p in self.productos:
            if p == producto:
                p.stock += producto.stock  # Sumar el stock si el producto ya existe
                break
        else:
            self.productos.append(producto)

    def listar_productos(self, tipo_tienda: int):
        """Método para listar los productos del restaurante."""
        if tipo_tienda == 3:
            resultado = "\n".join([f"{producto.nombre} - ${producto.precio}" for producto in self.productos])
            return resultado

    def realizar_venta(self, nombre_producto, cantidad):
        """Método para realizar una venta en el restaurante."""
        for p in self.productos:
            if p.nombre == nombre_producto:
                if p.stock >= cantidad:
                    p.stock -= cantidad
                    print(f"Venta realizada: {cantidad} unidades de {nombre_producto}")
                else:
                    print("No hay suficiente stock para realizar la venta")
                break
        else:
            print("El producto solicitado no está disponible")

class Supermercado(Tienda):
    """Clase que representa un supermercado."""

    def ingresar_producto(self, producto):
        """Método para ingresar un producto al supermercado."""
        for p in self.productos:
            if p == producto:
                p.stock += producto.stock  # Sumar el stock si el producto ya existe
                break
        else:
            self.productos.append(producto)

    def listar_productos(self, tipo_tienda: int):
        """Método para listar los productos de la farmacia."""
        if tipo_tienda == 2:
            resultado = "\n".join(
                [f"{producto.nombre} - Stock: {producto.stock}{' - Pocos productos disponibles' if producto.stock < 10 else ''} - ${producto.precio}" for producto in self.productos]
            )
            return resultado

    def realizar_venta(self, nombre_producto, cantidad):
        """Método para realizar una venta en el supermercado."""
        for p in self.productos:
            if p.nombre == nombre_producto:
                print("---------stock inicial")
                print(p.stock)
                if p.stock >= cantidad:
                    p.stock -= cantidad
                    print(f"Venta realizada: {cantidad} unidades de {nombre_producto}")
                    print("---------stock final")
                    print(p.stock)
                else:
                    print("No hay suficiente stock para realizar la venta")
                break
        else:
            print("El producto solicitado no está disponible")

class Farmacia(Tienda):
    """Clase que representa una farmacia."""

    def ingresar_producto(self, producto):
        """Método para ingresar un producto a la farmacia."""
        for p in self.productos:
            if p == producto:
                p.stock += producto.stock  # Sumar el stock si el producto ya existe
                break
        else:
            self.productos.append(producto)

    def listar_productos(self, tipo_tienda: int):
        """Método para listar los productos de la farmacia."""
        if tipo_tienda == 1:
            resultado = "\n".join(
                [f"{producto.nombre} - ${producto.precio}{' - Envío gratis al solicitar este producto' if producto.precio > 15000 else ''}" for producto in self.productos]
            )
            return resultado

    def realizar_venta(self, nombre_producto, cantidad):
        """Método para realizar una venta en el restaurante."""
        for p in self.productos:
            if p.nombre == nombre_producto:
                if cantidad > 3:
                    print("No se puede solicitar más de 3 unidades por venta en una farmacia")
                    return
                if p.stock >= cantidad:
                    p.stock -= cantidad
                    print(f"Venta realizada: {cantidad} unidades de {nombre_producto}")
                else:
                    print(f"Stock insuficiente. Solo se venderán {p.stock} unidades de {nombre_producto}.")
                    p.stock = 0
                return
        print("El producto solicitado no está disponible")