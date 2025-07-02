from models.productos_model import ProductoEntrada, Productos
from typing import List, Optional

productos_db: List[Productos] = []
contador_id = [0]

def obtener_todos() -> List[Productos]:
    """
    Regresa todos los productos en la memoria.
    """
    return productos_db

def obtener_por_id(producto_id: int) -> Optional[Productos]:
    """
    Busca y retorna un producto por su ID.
    """
    for producto in productos_db:
        if producto.id == producto_id:
            return producto
    return None

def crear(producto: ProductoEntrada) -> Productos:
    nuevo_producto = Productos(
        id=contador_id[0],
        nombre=producto.nombre,
        precio=producto.precio
    )
    productos_db.append(nuevo_producto)
    contador_id[0] += 1
    return nuevo_producto

def actualizar(producto_id: int, datos: Productos) -> Optional[Productos]:
    """
    Actualiza los datos de un producto que existe en la memoria.
    """
    for producto in productos_db:
        if producto.id == producto_id:
            productos_db.remove(producto)
            producto_actualizado = Productos(
                id=producto_id,
                nombre=datos.nombre,
                precio=datos.precio
            )
            productos_db.append(producto_actualizado)
            return producto_actualizado
    return None

def eliminar(producto_id: int) -> bool:
    """
    Elimina un producto por su ID. Regresa True si se eliminó.
    """
    for aux, producto in enumerate(productos_db):
        if producto.id == producto_id:
            productos_db.pop(aux)
            return True
    return False
