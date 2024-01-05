from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return "<html><body>This is a web page.</body></html>"
