from fastapi import FastAPI
import pandas as pd
app = FastAPI()





#Endpoint Recommendation system
@app.get("/Recommendation_system/{Game}")
def recomendacion_juego(Game : str):   
    df_RS = pd.read_csv("datos/Recommendation_system.csv")
    RS_data = df_RS[df_RS["Game"] == Game]
    RS_data_dict = RS_data.to_dict(orient="records")

    return RS_data_dict

