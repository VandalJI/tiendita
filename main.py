from fastapi import FastAPI
from routers.rutas_productos import router as productos_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="API de Productos",
    description="Manejo de productos en memoria",
    version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido a la Calculadora API"}

app.include_router(productos_router, prefix="/tiendita", tags=["Productos"])
