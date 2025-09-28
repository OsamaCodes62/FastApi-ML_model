from fastapi import FastAPI
from pydantic import BaseModel, computed_field, Field
from typing import Annotated, Literal
import pandas as pd
import pickle
from fastapi.responses import JSONResponse


with open("insurance_model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

# Tier 1 – Most Polluted Cities
tier1 = [
    "Delhi",
    "Lucknow",
    "Gaya",
    "Kolkata"
]


# Tier 2 – Moderately Polluted Cities
tier2 = [
    "Jaipur",
    "Chennai",
    "Indore",
    "Mumbai",
    "Kota",
    "Hyderabad",
    "Chandigarh",
    "Pune",
    "Jalandhar",
    "Bangalore"
]


class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt=0, lt=150, description="Interger Age of person")]
    weight: Annotated[float, Field(..., gt=0, description="Float weight of person")]
    height: Annotated[float, Field(..., gt=0, lt=3, description="float height of person")]
    income_lpa: Annotated[float, Field(..., gt=0, description="float income of person")]
    smoker: Annotated[bool, Field(..., description="Bool smoking habit of person")]
    city: Annotated[str, Field(..., description="String city of person")]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'], Field(..., description="Occupation of person")]

    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"
    
    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight / self.height **2
    
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"
        
    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier1:
            return 1
        elif self.city in tier2:
            return 2
        else:
            return 3
        



@app.post('/predict')
def predict_premium(data : UserInput):
    data.city = data.city.title()
    input_df = pd.DataFrame([
        {
            "age_group"	: data.age_group, 
            "bmi"	: data.bmi ,
            "occupation" : data.occupation	,
            "income_lpa" :	data.income_lpa,
            "lifestyle_risk": data.lifestyle_risk	,
            "city_tier" : data.city_tier
        }
        ])
    
    predict = model.predict(input_df)[0]
    return JSONResponse(status_code=200, content={"predict_category": predict})
