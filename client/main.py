from fastapi import FastAPI, WebSocket
from network import connect_to_relay
from storage import save_message

app = FastAPI()

clients = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)

    while True:
        data = await websocket.receive_text()
        save_message(data)

        for client in clients:
            await client.send_text(f"Message: {data}")

@app.get("/")
def home():
    return {"status": "online"}

if __name__ == "__main__":
    connect_to_relay()
