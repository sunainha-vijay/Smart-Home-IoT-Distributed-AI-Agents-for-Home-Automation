# 🏡 NANDA Smart Home — Distributed AI Agent Network

This is a mini project demonstrating the **core principles of NANDA (Networked Autonomous Neural Distributed Agents)** applied to a **Smart Home IoT domain**.

Multiple autonomous agents (Light, Temperature, Door) communicate with each other **without a centralized brain** — showcasing **distributed intelligence**.

---

## ✨ Features

- 🌡️ Temperature agent broadcasts sensor data  
- 🚪 Door agent sends open/close events  
- 💡 Light agent reacts autonomously to events  
- 🕸️ WebSocket-based communication protocol  
- 🧠 Fully decentralized — no central controller

---

## 🧭 System Architecture


| Agent             | Role                                                       |
|--------------------|------------------------------------------------------------|
| Light Agent        | Turns lights on/off based on temperature and door events   |
| Temp Agent         | Simulates temperature readings and broadcasts updates      |
| Door Agent         | Simulates door open/close events                           |
| Coordinator        | Routes messages between agents                             |
| Client             | Sends manual commands (e.g., check temperature)            |

---

## 🧰 Tech Stack

- **Language:** Python 3.8+  
- **Libraries:** `websockets`, `asyncio`, `json`  
- **Architecture:** Decentralized event-driven system

---

## ⚡ Installation & Setup

### 1. Clone this repository
```bash
git clone https://github.com/your-username/nanda-smart-home.git
cd nanda-smart-home

python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

pip install websockets

