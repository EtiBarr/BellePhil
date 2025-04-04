from fastapi import FastAPI

app = FastAPI()

def read_root():
    return {"message": "Hello from Python backend"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)