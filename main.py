
from graphic import Graphic
from channels2 import A,  B, C
from arrays import Arrays
import time

start = time.time()
arr = Arrays()
arr.fill_array(1, A,B, C)

# Graphic.graficar(arr.EstadoCanalF, "Estado Canal F")
# Graphic.graficar(arr.EstadoEstadoF, "Estado Estado F")
# Graphic.graficar(arr.EstadoCanalP, "Estado Canal P")
# Graphic.graficar(arr.EstadoEstadoP, "Estado Estado F")

# Graphic.graficar(arr.initial_table_for_taller3, "initial table")


mar_col, mar_row  = arr.marginalize_next_systems(
                initial_state=(0, 0, None),
                next_state=(0, None, None)
            )
print(mar_col, '\n\n\n',mar_row)


print('duration: ', time.time() - start, ' seconds')

    