""" Entry point: creates the FastAPI app and plugs in the routers. """

from fastapi import FastAPI
from app.routes import health

app = FastAPI(title = "Federal Deployment Platform API", version = "1.0.0")

# Each routes/ file owns one group of endpoints; 
# main.py only wires them together.
app.include_router(health.router)
