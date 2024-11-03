from clases.Libro import Libro
from clases.Rectangulo import Rectangulo
from clases.Calculadora import Calculadora
from clases.Animal import Animal 
from clases.Perro import Perro 
from clases.Gato import Gato 

#EJERCICIO 1
libro_1 = Libro(" De sangre y cenizas ", " Jennifer L.Armentrout ", 2021)
print(" DESCRIPCION DEL LIBRO ES : ")
libro_1.libro_descripcion()

#EJERCICIO 2
rectangulo_1 = Rectangulo(5,3)
print(" DESCRIPCION DEL RECTANGULO ES : ")
rectangulo_1.rectangulo_descripcion()
rectangulo_1.areaRectangulo()
rectangulo_1.perimetroRectangulo()

#EJERCICIO 3
calculadora_1 = Calculadora()
print(" SUMA: ", calculadora_1.sumar(10,10))
print(" RESTA: ", calculadora_1.restar(20,10))
print(" MULTIPLICACION", calculadora_1.multiplicacion(20,5))
print(" DIVISION: ", calculadora_1.dividir(10,2))

#EJERCICIO 4
mi_perro = Perro("Akamaru")
mi_gato = Gato("Zafiro")
print(f"{mi_perro.nombre} dice: {mi_perro.realice_sonido()}")
print(f"{mi_gato.nombre} dice : {mi_gato.realice_sonido()}")