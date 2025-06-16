from fastapi import FastAPI
import uvicorn
from routes import health, surveys

app = FastAPI()

app.include_router(health.router)
app.include_router(surveys.router)

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", reload=True)
