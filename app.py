
from fastapi import FastAPI
from pydantic import BaseModel
import time, threading, random

app = FastAPI(title="AgriSahayak 360 API")

STATE = {
    "irrigation": False,
    "latest_sensor": {}
}

def sensor_sim():
    while True:
        STATE["latest_sensor"] = {
            "soil_moisture": round(random.uniform(10,60),2),
            "temperature": round(random.uniform(15,40),2),
            "humidity": round(random.uniform(20,95),2),
            "timestamp": int(time.time())
        }
        time.sleep(5)

threading.Thread(target=sensor_sim, daemon=True).start()

class Irrigation(BaseModel):
    action: str

class Soil(BaseModel):
    ph: float
    nitrogen: float
    phosphorus: float
    potassium: float
    field_area_acres: float

@app.get("/ping")
def ping():
    return {"status":"ok","irrigation":STATE["irrigation"],"sensor":STATE["latest_sensor"]}

@app.post("/irrigation")
def irr(cmd: Irrigation):
    if cmd.action.lower()=="on":
        STATE["irrigation"]=True
        return {"result":"irrigation_on"}
    STATE["irrigation"]=False
    return {"result":"irrigation_off"}

@app.post("/soiltest")
def soiltest(s: Soil):
    crops = [
        {"name":"Wheat","yield":2.5,"price":20000},
        {"name":"Rice","yield":3.0,"price":22000},
        {"name":"Maize","yield":4.0,"price":15000},
        {"name":"Cotton","yield":1.2,"price":35000},
    ]
    out=[]
    for c in crops:
        expected = c["yield"]*s.field_area_acres
        revenue = expected*c["price"]
        out.append({"crop":c["name"],"expected_yield_tons":expected,"estimated_revenue_inr":int(revenue)})
    return {"recommendations":out}
