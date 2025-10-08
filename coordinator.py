# coordinator.py
import asyncio, websockets, json

connected = set()

async def handler(websocket):
    connected.add(websocket)
    try:
        async for message in websocket:
            data = json.loads(message)
            print(f"[COORDINATOR] {data}")
            for conn in connected:
                if conn != websocket:
                    await conn.send(json.dumps(data))
    finally:
        connected.remove(websocket)

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("Coordinator running at ws://localhost:8765")
        await asyncio.Future()

asyncio.run(main())
