from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return "<html><body>This is a web page.</body></html>"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
