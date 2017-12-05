# coding: utf-8
def predictflightmodel(p1model, p2_arr_flights, p3_carrier_ct, p4_weather_ct, p5_nas_ct):
    import pandas as pd
    import numpy as np
    from sklearn import datasets, linear_model
    from sklearn.metrics import mean_squared_error, r2_score
    from matplotlib import cm
    import pickle


    strmodel = "modelos_vuelos/{model}.pkl"
    strmodel = strmodel.replace("{model}",p1model)

    model = pickle.load(open(strmodel, 'rb')) 
    lstvalue = {"arr_flights":[p2_arr_flights], "carrier_ct":[p3_carrier_ct], "weather_ct": [p4_weather_ct],"nas_ct": [p5_nas_ct]}
    dfvalue = pd.DataFrame(lstvalue)
    resultado = model.predict(dfvalue.values)
    return resultado[0]



