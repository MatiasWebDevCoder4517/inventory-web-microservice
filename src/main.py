# External
from fastapi import FastAPI


app = FastAPI(debug=True)


@app.get("/home")
def root():
    return {"message": "Hello World"}
