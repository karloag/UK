# -*- coding: utf-8 -*-
"""evaluacion semana 3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kbN-x2HKRKvzUDiq9kgN_UzOtnxqL68g

Declara variables en Python para almacenar los siguientes datos:
● Nombres de las tiendas: ['Tienda A', 'Tienda B', 'Tienda C']
● Ventas de cada tienda: [1000, 1500, 2000]
Calcula el total de ventas usando operadores aritméticos y almacénalo
en una nueva variable.
Imprime los resultados
"""

#declaracion de las variables
nombres_tiendas= ['Tienda A', 'Tienda B','Tienda C']
ventas_tiendas= [1000,1500, 2000]
#calculo del total de ventas
tota_ventas= sum(ventas_tiendas)
#impresion de los resultados
print("Nombres de las tiendas", nombres_tiendas)
print("Ventas de cada tienda", ventas_tiendas)
print("Total de ventas", tota_ventas)

"""---

Utiliza los datos de ventas proporcionados. Realiza la limpieza de datos
para asegurar que no haya datos faltantes y luego visualiza los datos
utilizando Matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt

#conversion a array numpy
ventas_array = np.array(ventas_tiendas, dtype=np.float64)
#calcula la media ignorando valores NaN
media_ventas = np.mean(ventas_array)
#reemplazo de valores faltantes con la media
ventas_array = np.where(np.isnan(ventas_array),media_ventas, ventas_array)

#visualizacion con Matplot
plt.figure(figsize=(8, 5))
plt.bar(nombres_tiendas, ventas_array, color=['skyblue','green','red'])
plt.xlabel('Tiendas')
plt.ylabel('Ventas')
plt.title('Ventas de Tiendas')
plt.show()

"""---

Realiza un análisis de los datos de ventas y utiliza Google Colab para
cargar, limpiar, y visualizar los datos. Implementa una simulación sencilla
que prediga las ventas futuras basándose en un aumento porcentual
constante.
1. Simula un aumento del 10% en las ventas para el próximo mes.
2. Visualiza los resultados de las ventas actuales y las predicciones
futuras en un gráfico de líneas.
"""

import pandas as pd
#conversion a DataFrame
df_ventas = pd.DataFrame({'Tienda': nombres_tiendas, 'Ventas_Actuales': ventas_tiendas})

#verificar valores nulos
df_ventas['Ventas_Actuales'] = df_ventas['Ventas_Actuales'].fillna(df_ventas['Ventas_Actuales'].mean() )

#aumento del 10% ventas
df_ventas['Ventas_Futuras'] = df_ventas['Ventas_Actuales'] * 1.10

#grafico de lineas
plt.figure(figsize=(8, 5))
plt.plot(df_ventas['Tienda'], df_ventas['Ventas_Actuales'], marker='o', linestyle='-', color='blue', label='Ventas Actuales')
plt.plot(df_ventas['Tienda'], df_ventas['Ventas_Futuras'], marker='o', linestyle='--', color='red', label='Ventas Futuras')

#nombres de ejes del grafico
plt.xlabel('Tiendas')
plt.ylabel('Ventas')
plt.title('Ventas Actuales y proyeccion a futuro')
plt.legend()
plt.show()