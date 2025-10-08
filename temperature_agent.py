# temp_agent.py
import asyncio, websockets, json, random

async def temp_agent():
    async with websockets.connect("ws://localhost:8765") as ws:
        print("Temperature Agent connected")
        while True:
            temp = random.randint(20, 40)
            data = {"sender": "TempAgent", "type": "sensor", "content": f"temp {temp}"}
            await ws.send(json.dumps(data))
            await asyncio.sleep(5)  # simulate periodic temperature update

asyncio.run(temp_agent())
