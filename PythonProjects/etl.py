
import requests
import pandas as pd

# URL de la API
url = "https://jsonplaceholder.typicode.com/posts"  # Ejemplo de API pública

# Hacer una solicitud GET a la API
response = requests.get(url)

# Verificar el estado de la respuesta
if response.status_code == 200:
    # Convertir la respuesta JSON a un objeto de Python (lista o diccionario)
    data = response.json()
    
    
    # Crear un DataFrame de Pandas con los datos
    df = pd.DataFrame(data)
    
    # Mostrar como viene el json
    print(data)

    # Mostrar las primeras filas del DataFrame
    print(df.head())

    # Limpiar los saltos de línea en la columna
    df['body'] = df['body'].str.replace('\n', ' ', regex=True)

    # Guardar como CSV
    df.to_csv("datos.csv", index=False)
else:
    print(f"Error al acceder a la API: {response.status_code}")
