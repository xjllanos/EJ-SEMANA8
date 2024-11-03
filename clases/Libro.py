#creo la clase
class Libro:
#CARACTERISTICAS
    def __init__(self, titulo:str, autor:str, anio: int)-> None:
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
    
    def libro_descripcion(self) -> None:
        print(f"El titulo del libro es: {self.titulo}, la autora es: {self.autor}, el año que se publico fue en: {self.anio}")