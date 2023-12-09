
from graphic import Graphic
from channels2 import A, B, C
from arrays import Arrays
import time
import numpy as np

start = time.time()
arr = Arrays()
arr.fill_array(1, A, B, C)
arr.fill_initial_table_for_taller3()

# Graphic.graficar(arr.EstadoCanalF, "Estado Canal F")
# Graphic.graficar(arr.EstadoEstadoF, "Estado Estado F")
# Graphic.graficar(arr.EstadoCanalP, "Estado Canal P")
# Graphic.graficar(arr.EstadoEstadoP, "Estado Estado F")

# Graphic.graficar(arr.initial_table_for_taller3, "initial table")


# mar_col, _ = arr.marginalize_next_state(
#                 current_state=(1, 0, None),
#                 next_state=(True, True, None)
#             )

# mar_row  = arr.marginalize_one_current_state(
#                 current_state=(1, 0, None),
#                 next_state=(True, None, None)
#             )

# mar_row2  = arr.marginalize_one_current_state(
#                 current_state=(1, 0, None),
#                 next_state=(None, True, None)
#             )

# pro = np.outer(mar_row, mar_row2).flatten()

# print('\n\n\n', mar_row, '\n\n\n', mar_row2)
# print('\n\n\n', pro)

print('duration: ', time.time() - start, ' seconds')
print("(C | A = 1):\n",arr.get_probability_distribution(
                current_state=(None, 0, None),
                next_state=(True, None, True)))