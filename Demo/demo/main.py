from fastapi import FastAPI, Form
from joblib import load
from pydantic import BaseModel
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.metrics import roc_auc_score, accuracy_score
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error,mean_absolute_error, mean_absolute_percentage_error
from sklearn import svm
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeRegressor

class Parameters(BaseModel):
    GOLD_open: float
    GOLD_high: float
    GOLD_low: float
    GOLD_close: float  
    copper: float  
    crude_oil: float
    DXY: float  
    EURUSD: float    
    MSCI: float    
    NASDAQ: float    
    NLR: float  
    platinum: float      
    RUT: float  
    silver: float
    SP500: float    
    VIX: float
    
    
def get_inputs(features,exclude_gold_close=False):
    if not exclude_gold_close:
        data = pd.DataFrame({
            'GOLD_open': [features.GOLD_open],
            'GOLD_high': [features.GOLD_high],
            'GOLD_low': [features.GOLD_low],
            'GOLD_close' : [features.GOLD_close],
            'copper':  [features.copper],
            'crude_oil':[features.crude_oil],
            'DXY':  [features.DXY],
            'EURUSD':   [features.EURUSD] ,
            'MSCI':    [features.MSCI] ,
            'NASDAQ': [features.NASDAQ] ,  
            'NLR': [features.NLR],
            'platinum':[features.platinum],     
            'RUT':  [features.RUT],
            'silver': [features.silver],
            'SP500':  [features.SP500] , 
            'VIX': [features.VIX]
        })
    else:
        data = pd.DataFrame({
            'GOLD_open': [features.GOLD_open],
            'GOLD_high': [features.GOLD_high],
            'GOLD_low': [features.GOLD_low],
            'copper':  [features.copper],
            'crude_oil':[features.crude_oil],
            'DXY':  [features.DXY],
            'EURUSD':   [features.EURUSD] ,
            'MSCI':    [features.MSCI] ,
            'NASDAQ': [features.NASDAQ] ,  
            'NLR': [features.NLR],
            'platinum':[features.platinum],     
            'RUT':  [features.RUT],
            'silver': [features.silver],
            'SP500':  [features.SP500] , 
            'VIX': [features.VIX]
            })
    
    return data
def get_inputs_knn(features):
    data = pd.DataFrame({
        'GOLD_open': [features.GOLD_open],
        'GOLD_high': [features.GOLD_high],
        'GOLD_low': [features.GOLD_low]
    })
    return data
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Gold price Prediction"}

@app.post("/predict_price")
def predict_price(
    GOLD_open:  float= Form(...),
    GOLD_high:  float= Form(...),
    GOLD_low:   float= Form(...),
    GOLD_close: float= Form(...),  
    copper:     float= Form(...),
    crude_oil:  float= Form(...),
    DXY:        float= Form(...),
    EURUSD:     float= Form(...),
    MSCI:       float= Form(...),
    NASDAQ:     float= Form(...), 
    NLR:        float= Form(...), 
    platinum:   float= Form(...),      
    RUT:        float= Form(...),
    silver:     float= Form(...),
    SP500:      float= Form(...),  
    VIX:        float= Form(...)
):
    input_data = Parameters(
        GOLD_open=GOLD_open,
        GOLD_high=GOLD_high,
        GOLD_low=GOLD_low,
        GOLD_close=GOLD_close,
        copper=copper,
        crude_oil=crude_oil,
        DXY=DXY,
        EURUSD=EURUSD,
        MSCI=MSCI,
        NASDAQ=NASDAQ,
        NLR=NLR,
        platinum=platinum,
        RUT=RUT,
        silver=silver,
        SP500=SP500,
        VIX=VIX
    )
    inputs = get_inputs(input_data)
    inputs_except_gold_close = get_inputs(input_data, exclude_gold_close=True)
    inputs_knn=get_inputs_knn(input_data)
    results = {}
    adaboost = load(r"C:\Users\Laptop K1\Downloads\model (1)")
    knn=load(r"C:\Users\Laptop K1\Downloads\KNN.pkl")
    random_forest=load(r"C:\Users\Laptop K1\Downloads\best_grid_1")
    ridge=load(r"C:\Users\Laptop K1\Downloads\ridge_model.pkl")
    results["Gold Price pridicted by Adaboost"] = str(adaboost.predict(inputs))
    results["Gold Price pridicted by KNN"] = str(knn.predict(inputs_knn))
    results["Gold Price pridicted by Random_forest"] = str(random_forest.predict(inputs_except_gold_close ))
    results["Gold Price pridicted by Ridge Regression"] = str(ridge.predict(inputs_except_gold_close ))
z
    return results