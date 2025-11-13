# AgriSahayak 360 — Smart Farmer Assistant (India)
AgriSahayak 360 is a multilingual farmer assistant that provides soil testing, crop recommendations, irrigation power control, and live sensor simulation.  
Built using FastAPI backend + HTML/JS frontend, simple enough for a 10th standard student.

## Features
- Soil test & crop recommendation (rule-based)
- Irrigation ON/OFF system (mock relay)
- Live sensor simulator (moisture, temp, humidity)
- Weather/atmosphere simulator
- Multilingual UI (English, Hindi, Kannada)
- Works offline (frontend)

## How to Run
1. Install backend deps:
   pip install -r backend/requirements.txt
2. Start backend:
   uvicorn backend.app:app --reload --port 8000
3. Open frontend/index.html
