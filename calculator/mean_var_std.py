import numpy as np

def calculate(x):
    if len(x) != 9:
        print('error')
        return
    else:
        matriz = np.array(x).reshape(3, 3)
        dict = {
                'mean': [np.mean(matriz,0), np.mean(matriz,1), np.mean(matriz)],
                'variance': [np.var(matriz,0), np.var(matriz,1), np.var(matriz)],
                'standard deviation': [np.std(matriz,0), np.std(matriz,0), np.std(matriz)],
                'max': [np.max(matriz,0), np.max(matriz,0), np.max(matriz)],
                'min': [np.min(matriz,0), np.min(matriz,0), np.min(matriz)],
                'sum': [np.sum(matriz,0), np.sum(matriz,0), np.sum(matriz)]
                }
    print(dict)
