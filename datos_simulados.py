import numpy as np
import pandas as pd
import datetime
import os

# Variables Globales
PATH = os.getcwd()
INPUT_FOLDER = 'input'
FILENAME = 'dataset.xlsx'

# Si no esta la carpeta input, la creo
if not os.path.exists(os.path.join(PATH, INPUT_FOLDER)):
    os.mkdir(INPUT_FOLDER)

# Parámetros
n_samples = 500
n_features = 3

# Coeficientes reales para la regresión multilineal (puedes cambiarlos a tu gusto)
coefficients = np.array([3000, 15000, -2000])

# Generar variables independientes (área, número de habitaciones, antigüedad)
areas = np.random.randint(50, 200, n_samples)  # Áreas entre 50 y 200 m²
rooms = np.random.randint(1, 6, n_samples)  # Número de habitaciones entre 1 y 5
ages = np.random.randint(0, 100, n_samples)  # Antigüedad entre 0 y 100 años

# Combinar las variables independientes en una matriz X
X = np.column_stack((areas, rooms, ages))

# Generar ruido aleatorio
noise = np.random.normal(0, 5000, n_samples)

# Calcular la variable dependiente (precio) usando los coeficientes y el ruido
Y = np.dot(X, coefficients) + noise

# Generar fechas aleatorias
start_date = datetime.date(2000, 1, 1)
end_date = datetime.date(2022, 1, 1)
date_range = (end_date - start_date).days
dates = [start_date + datetime.timedelta(days=np.random.randint(0, date_range)) for _ in range(n_samples)]

# Crear un DataFrame con las variables predictoras, la variable a predecir y el campo de fechas
data = {'Fecha': dates, 'Area': areas, 'Habitaciones': rooms, 'Antiguedad': ages, 'Precio': Y}
df = pd.DataFrame(data)

# Exportar el DataFrame a un archivo de Excel
df.to_excel(os.path.join(PATH, INPUT_FOLDER, FILENAME), index=False)