from fastapi import FastAPI, HTTPException
from fastapi import APIRouter
from models.productos_model import Productos, ProductoEntrada
import services.productos_service as services

router = APIRouter()

@router.get("/productos", response_model=list[Productos])
def listar_productos():
    return services.obtener_todos()

@router.get("/productos/{id}", response_model=Productos)
def obtener_producto(id: int):
    producto = services.obtener_por_id(id)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.post("/productos", response_model=Productos)
def crear_producto(producto: ProductoEntrada):
    producto_creado = services.crear(producto)
    return producto_creado

@router.put("/productos/{id}", response_model=Productos)
def actualizar_producto(id: int, producto: Productos):
    actualizado = services.actualizar(id, producto)
    if actualizado is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return actualizado

@router.delete("/productos/{id}")
def eliminar_producto(id: int):
    eliminado = services.eliminar(id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"mensaje": "Producto eliminado correctamente"}
