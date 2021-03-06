import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from modules import router

app = FastAPI(title="Music Store API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/music-store/api/v1")

if __name__ == '__main__':
    # Programa principal

    uvicorn.run(app, host='127.0.0.1', port=8000)
