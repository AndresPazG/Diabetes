from pydantic import BaseModel

class dataTest(BaseModel):
    nombre: str
    estudiantes: float

class DiabetesData(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int 
    