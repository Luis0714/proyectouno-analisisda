
from graphic import Graphic
from channels import A,  B, C
from arrays import Arrays

arr = Arrays()
arr.fill_array(1,A,B, C)



Graphic.graficar(arr.EstadoCanalF, "Estado Canal F")
Graphic.graficar(arr.EstadoEstadoF, "Estado Estado F")
Graphic.graficar(arr.EstadoCanalP, "Estado Canal P")
Graphic.graficar(arr.EstadoEstadoP, "Estado Estado F")


