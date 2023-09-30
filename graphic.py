import matplotlib.pyplot as plt
from matplotlib.table import Table
import numpy as np
from channels import A, B, C
from arrays import Arrays
from logic import Logic
import pandas as pd
class Graphic:

    def graficar():
        # Datos para la tabla
        arr = Arrays()
        arr.fill_array(A, B, C)
        cell_height = 0.15
        channels = ['Canal '+Graphic.obtener_letra_por_numero(i+1) for i in range(len(arr.array_channels))]
        headers =  ['A','B','C' ]+channels
        # dats = Logic.probability_system_and_channels(data)
        # Datos para la primera tabla

        # Datos de ejemplo en la lista response
        response = Logic.probability_system_and_channels(arr)
    
        # response[0][0] = str(response[0][0])

        cell_height = 0.1

        # Crear subplots y mostrar las tablas
        fig, axs = plt.subplots(len(response), 1, figsize=(6, 8 * len(response)))  # Un subplot por cada tabla

        for i, table_data in enumerate(response):
            df = pd.DataFrame(table_data, columns=headers)
            # Mostrar la tabla en el subplot actual con cellLoc y cellLoc table personalizados
            axs[i].axis('off')  # Eliminar ejes
            tabla = axs[i].table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

            # Ajustar la altura de las filas
            tabla.auto_set_font_size(False)
            tabla.set_fontsize(14)
            for irow, cell in enumerate(tabla.get_celld().values()):
                cell.set_height(cell_height)

        plt.subplots_adjust(hspace=0.5)  # Ajustar el espacio entre las filas

        # Mostrar la figura
        plt.show()
                                        

                           
    def obtener_letra_por_numero(numero):
        if 1 <= numero <= 26:
            # Asumiendo que el número 1 corresponde a 'A', el número 2 a 'B' y así sucesivamente.
            letra = chr(ord('A') + numero - 1)
            return letra
        else:
            return "Número fuera de rango"
