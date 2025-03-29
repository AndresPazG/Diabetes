import pickle
from fastapi import APIRouter
import numpy as np
from interfaces import DiabetesData

router=APIRouter()
#Cargamos el modelo
with open("RFDiabetesv132.pkl","rb") as file:
    model=pickle.load(file)
    
labels=["Paciente Sano", "Paciente con diabetes"]

@router.post("/predict")
def predict(data:DiabetesData):
    data=data.model_dump()
    print(data)
    
    #Array
    Pregnancies=data["Pregnancies"]
    Glucose=data["Glucose"]
    BloodPressure=data["BloodPressure"]
    SkinThickness=data["SkinThickness"]
    Insulin=data["Insulin"]
    BMI=data["BMI"]
    DiabetesPedigreeFunction=data["DiabetesPedigreeFunction"]
    Age=data["Age"]
    
    xin = np.array([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]).reshape(1,8)
    prediction=model.predict(xin)

    print("predictions",labels[prediction[0]])
    
    return{"Prediction":labels[prediction[0]]}