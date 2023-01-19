from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse


app = FastAPI()

@app.get("/")
async def index():
    page = open("./index.html", "r").read()
    return HTMLResponse(page)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    counter = 1
    while True:
        data = await websocket.receive_json()
        data["listObject"] = f'{counter}. ' + data["listObject"]
        await websocket.send_json(data)
        counter += 1