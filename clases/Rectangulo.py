#creo la clase
class Rectangulo: 
#caracteristicas del rectangulo
    def __init__(self, base:float, altura:float)->None:
        self.base = base 
        self.altura = altura

    def rectangulo_descripcion(self) -> None:
        print(f"La base del rectangulo es: {self.base}, la altura del rectangulo es: {self.altura}")

    #CALCULAR EL AREA DEL RECTANGULO 
    def areaRectangulo(self)->float: 
        area = self.base * self.altura
        print(" El valor del area es: ",area)
        return area
    
    #CALCULAR EL PERIMETRO
    def perimetroRectangulo(self)->float: 
        perimetro = 2*self.base + 2*self.altura
        print("El perimetro del rectangulo es: ", perimetro)
        return perimetro  