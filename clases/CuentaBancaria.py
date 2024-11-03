#CREO LA CLASE

class CuentaBancaria:
    def __init__(self, titular:str, saldo_encapsulado:int)->None:
        self.titular = titular 
        self.saldo_encapsulado = saldo_encapsulado 

    def cuenta_descripcion(self) -> None:
        print(f"El titular de la cuenta es: {self.titular}, su saldo es de: {self.saldo_encapsulado}")

#INCOMPLETO NO LLEGO A ENTENDER EL ENCAPSULAMIENTO 
