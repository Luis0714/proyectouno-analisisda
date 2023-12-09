from graphic import Graphic
from data_taller2.channels import A,  B, C
from data_taller2.channels2 import A as A2,  B as B2, C as C2
from arrays import Arrays


arr = Arrays()
arr.fill_array(1, A,B, C)
arr.fill_EstadoCanalF()
Graphic.graficar(arr.EstadoCanalF, "Estado Canal F (muestra 15)")

arr.fill_array(1, A2,B2, C2)
arr.fill_EstadoCanalF()
Graphic.graficar(arr.EstadoCanalF, "Estado Canal F (muestra 16)")
