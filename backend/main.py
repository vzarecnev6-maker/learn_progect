from fastapi import FastAPI, HTTPException, status
from database import init_db
import crud
from schemas import *

app = FastAPI(title="Polyclinic Doctors API")

@app.on_event("startup")
def startup():
    init_db()

@app.get("/doctors")
def read_doctors():
    return crud.get_all_doctors()

@app.get("/doctors/{doctor_id}")
def read_doctor(doctor_id: int):
    doctor = crud.get_doctor_by_id(doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Доктор не найден")
    return doctor

@app.post("/doctors", status_code=status.HTTP_201_CREATED)
def create_doctor(doctor: CreateDoctor):
    doctor_id = crud.create_doctor(doctor.model_dump())
    return {"message": "Запись создана", "id": doctor_id}