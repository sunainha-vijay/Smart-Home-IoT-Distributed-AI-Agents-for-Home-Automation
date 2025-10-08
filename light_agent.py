# light_agent.py
import asyncio, websockets, json

async def light_agent():
    async with websockets.connect("ws://localhost:8765") as ws:
        print("Light Agent connected")
        light_status = "OFF"

        while True:
            msg = await ws.recv()
            data = json.loads(msg)

            # React to temperature
            if data["sender"] == "TempAgent" and "temp" in data["content"]:
                temp_val = int(data["content"].split()[1])
                if temp_val > 30 and light_status == "ON":
                    light_status = "OFF"
                    print(f"[Light Agent] Turning lights OFF (Hot: {temp_val}°C)")
                elif temp_val <= 30 and light_status == "OFF":
                    light_status = "ON"
                    print(f"[Light Agent] Turning lights ON (Cool: {temp_val}°C)")

            # React to door open
            if data["sender"] == "DoorAgent" and data["content"] == "door opened":
                light_status = "ON"
                print("[Light Agent] Door opened at night → Lights ON")

asyncio.run(light_agent())
