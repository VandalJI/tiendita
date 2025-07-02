from pydantic import BaseModel

class Productos(BaseModel):
    """
    Modelo de datos para representar un producto.

    Atributos:
        id (int): Identificador único del producto.
        nombre (str): Nombre del producto.
        precio (float): Precio del producto.
    """
    id: int
    nombre: str
    precio: float

