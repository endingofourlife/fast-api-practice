from fastapi import FastAPI
from routes import software_routes

app = FastAPI()

app.include_router(software_routes.router, prefix="/api")
