
#* Ce fichier contient les classes qui représentent tes tables.

from sqlalchemy import Column, Integer
from .database import Base

#! Etape 4 ---- Definir un 'modele' ----=> c'est une classe qui décrit comment sera ta table dans la base
from sqlalchemy import Column, Integer, Float

class Patient(Base):                          #? Cette classe = table dans la base
    __tablename__ = "patients" 
    
    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer)
    gender = Column(Integer)                  #? 0=femme, 1=homme
    pressure_high = Column(Float)
    pressure_low = Column(Float)
    glucose = Column(Float)
    kcm = Column(Float)
    troponin = Column(Float)
    impluse = Column(Float)
