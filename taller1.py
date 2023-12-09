from graphic import Graphic
from data_taller1.channels import A,  B, C
from arrays import Arrays

arr = Arrays()
arr.fill_array(1, A,B, C)

arr.fill_EstadoCanalF()
arr.fill_EstadoEstadoF()
arr.fill_EstadoCanalP()
arr.fill_EstadoEstadoP()
Graphic.graficar(arr.EstadoCanalF, "Estado Canal F")
Graphic.graficar(arr.EstadoEstadoF, "Estado Estado F")
Graphic.graficar(arr.EstadoCanalP, "Estado Canal P")
Graphic.graficar(arr.EstadoEstadoP, "Estado Estado F")