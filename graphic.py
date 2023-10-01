import matplotlib.pyplot as plt
from matplotlib.table import Table
import numpy as np
import pandas as pd
class Graphic:

    def graficar(table, title):
        # Datos para la tabla
        cell_height = 0.15

        # Datos de ejemplo en la lista response
        EstadosCanalF = table
       # Crear un DataFrame con los datos
      
        df = pd.DataFrame(EstadosCanalF[1:], columns=EstadosCanalF[0])
    
        # Crear la tabla
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.axis('off')
        tabla = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

        
        # Ajustar la altura de las filas
        tabla.auto_set_font_size(False)
        tabla.set_fontsize(14)
        for irow, cell in enumerate(tabla.get_celld().values()):
            cell.set_height(0.1)
        plt.title(title)
        plt.show()







                                                
        
               
