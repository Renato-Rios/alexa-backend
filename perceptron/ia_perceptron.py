import numpy as np

def reconocer_porcentaje(features, archivo_modelo="modelo.dat"):
    with open(archivo_modelo, "r") as f:
        lineas = f.readlines()
        w = np.array(list(map(float, lineas[0].split())))
        theta = float(lineas[1])
    
    # Suma ponderada original del notebook
    h = np.dot(features, w) - theta  
    
    # Función Sigmoide para obtener porcentaje continuo
    porcentaje_acierto = 1 / (1 + np.exp(-h))
    
    return porcentaje_acierto * 100  # Arroja un valor de 0.0 a 100.0