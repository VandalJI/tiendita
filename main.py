from fastapi import FastAPI
from routes.rutas_productos import router as productos_router

app = FastAPI(
    title="API de Productos",
    description="Manejo de productos en memoria",
    version="1.0.0"
)

app.include_router(productos_router, prefix="/tiendita", tags=["Productos"])
