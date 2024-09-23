from fastapi import FastAPI
from app.controllers import evaluation_controller

app = FastAPI()

# Registrar las rutas
app.include_router(evaluation_controller.router)

# Inicia el servidor con: uvicorn app.main:app --reload
