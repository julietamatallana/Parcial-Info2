import pandas as pd

# 1. Cargas el archivo (asegúrate de que esté en la misma carpeta que este script)
df = pd.read_csv('CalAIR_VA_2023.csv')

# 2. Ver solo los nombres de las columnas
print("Nombres de las columnas:")
print(df.columns.tolist())

# 3. Ver las primeras 5 filas para entender los datos
print("\nPrimeras filas:")
print(df.head())

# 4. Ver qué tipo de datos hay (si son números o texto)
print("\nInformación de tipos:")
print(df.dtypes)