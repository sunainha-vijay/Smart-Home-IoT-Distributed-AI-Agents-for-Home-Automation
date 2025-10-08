# door_agent.py
import asyncio, websockets, json, random

async def door_agent():
    async with websockets.connect("ws://localhost:8765") as ws:
        print("Door Agent connected")
        while True:
            # randomly simulate door opening
            event = random.choice(["door opened", "door closed"])
            data = {"sender": "DoorAgent", "type": "sensor", "content": event}
            await ws.send(json.dumps(data))
            await asyncio.sleep(10)

asyncio.run(door_agent())
