from pydantic import BaseModel



class ProductoEntrada(BaseModel):
    nombre: str
    precio: float

class Productos(BaseModel):
    id: int
    nombre: str
    precio: float
