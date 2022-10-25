from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://localhost.tiangolo.com",
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Hello World"}


@app.get("/temperature/dataset")
async def root():
    return {"months": ['January', 'February', 'March', 'April', 'May', 'June'],
            "datasets": [{"label": "Temperature at 2PM",
                        "backgroundColor": "rgb(255, 99, 132)",
                        "borderColor": "rgb(255, 99, 132)",
                        "data": [10, 22, 17, 14, 32, 42, 57]
                        }]
            }