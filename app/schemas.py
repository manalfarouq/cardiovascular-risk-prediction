
#* Ce fichier contient les modèles Pydantic (validation d'entrée/sortie)

# ===Pydantic ===
from pydantic import BaseModel, Field                 # valide et structure les données que l'utilisateur envoie à ton API

#! Etape 7 ---- Modele Pydantic ----
#* Entrée (ce que l'utilisateur envoie) :
from pydantic import BaseModel
class PatientCreate(BaseModel):
    age: int = Field(..., ge=1, le=120)              
    gender: int = Field(..., ge=0, le=1)              # 0 = femme, 1 = homme
    pressure_high: float = Field(..., ge=50, le=250) 
    pressure_low: float = Field(..., ge=30, le=150)  
    glucose: float = Field(..., ge=50, le=500)      
    kcm: float = Field(..., ge=0, le=200)           
    troponin: float = Field(..., ge=0, le=50)        
    impluse: float = Field(..., ge=30, le=200)   
    

#* Sortie (ce que l'API renvoie) :
class PatientRespond(PatientCreate):
    id: int

    class Config:
        orm_mode = True  # permet la compatibilité ORM <=> Pydantic (cad: permet à Pydantic de comprendre les objets SQLAlchemy.)
        
# FastAPI → reçoit JSON ⮕ valide avec PatientCreate ⮕ envoie résultat avec PatientRespond
