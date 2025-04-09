from fastapi import FastAPI
from app.routers import usuarios, alumnos
from app.database import Base, engine

app = FastAPI(
    title="Tutorial de FastAPI Grupo 9",       
    version="1.0.0",           
    description="Primera conexion con alembic, y sqlite", 
)

app.include_router(usuarios.router, prefix="/usuarios", tags=["usuarios"])
app.include_router(alumnos.router, prefix="/alumnos", tags=["alumnos"])

@app.get("/")
async def hola_mundo():
    return {"mensaje": "Hola mundo"}