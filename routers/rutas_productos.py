from fastapi import FastAPI, HTTPException
from models.productos_model import Productos
import services.productos_service as obtener_todos, obtener_por_id, crear, actualizar, eliminar

router = APIRouter()

@router.get("/productos", response_model=list[Productos])
def listar_productos():
    return service.obtener_todos()

@router.get("/productos/{id}", response_model=Productos)
def obtener_producto(id: int):
    producto = service.obtener_por_id(id)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.post("/productos", response_model=Productos)
def crear_producto(producto: Productos):
    return service.crear(producto)

@router.put("/productos/{id}", response_model=Productos)
def actualizar_producto(id: int, producto: Productos):
    actualizado = service.actualizar(id, producto)
    if actualizado is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return actualizado

@router.delete("/productos/{id}")
def eliminar_producto(id: int):
    eliminado = service.eliminar(id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"mensaje": "Producto eliminado correctamente"}