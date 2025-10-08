# client.py
import asyncio, websockets, json

async def client():
    async with websockets.connect("ws://localhost:8765") as ws:
        print("Client connected")
        while True:
            cmd = input("Enter command (e.g., 'check temperature'): ")
            data = {"sender": "Client", "type": "task", "content": cmd}
            await ws.send(json.dumps(data))

asyncio.run(client())
