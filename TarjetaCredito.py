class TarjetaCredito:
    def __init__(self, numero_tarjeta, saldo_pendiente=0):
        self.numero_tarjeta = numero_tarjeta
        self.saldo_pendiente = saldo_pendiente

    @staticmethod
    def validar_tarjeta(numero):
        numero = [int(digito) for digito in str(numero)][::-1]
        for i in range(1, len(numero), 2):
            numero[i] *= 2
            if numero[i] > 9:
                numero[i] -= 9
        return sum(numero) % 10 == 0

    def consultar_saldo_pendiente(self):
        return self.saldo_pendiente

    def pagar(self, cantidad):
        if cantidad > 0:
            self.saldo_pendiente = max(0, self.saldo_pendiente - cantidad)
            print(f"Pago realizado. Saldo pendiente: {self.saldo_pendiente}")
        else:
            print("La cantidad a pagar debe ser positiva.")


class CuentaBancaria:
    def __init__(self, titular, saldo, tarjeta):
        self.__titular = titular
        self.__saldo = saldo
        self.tarjeta = tarjeta

    def depositar(self, cantidad):
        if TarjetaCredito.validar_tarjeta(self.tarjeta.numero_tarjeta):
            if cantidad > 0:
                self.__saldo += cantidad
                print(f"Depósito exitoso. Nuevo saldo: {self.__saldo}")
            else:
                print("La cantidad a depositar debe ser positiva.")
        else:
            print("Número de tarjeta inválido. Operación cancelada.")

    def retirar(self, cantidad):
        if TarjetaCredito.validar_tarjeta(self.tarjeta.numero_tarjeta):
            if 0 < cantidad <= self.__saldo:
                self.__saldo -= cantidad
                print(f"Retiro exitoso. Nuevo saldo: {self.__saldo}")
            else:
                print("Fondos insuficientes o cantidad inválida.")
        else:
            print("Número de tarjeta inválido. Operación cancelada.")

    def consultar_saldo(self):
        return self.__saldo

    def consultar_titular(self):
        return self.__titular

    def realizar_pago_tarjeta(self, cantidad):
        if TarjetaCredito.validar_tarjeta(self.tarjeta.numero_tarjeta):
            if 0 < cantidad <= self.__saldo:
                self.__saldo -= cantidad
                self.tarjeta.pagar(cantidad)
            else:
                print("Fondos insuficientes o cantidad inválida.")
        else:
            print("Número de tarjeta inválido. Operación cancelada.")


# Ejemplo de uso
tarjeta = TarjetaCredito("4532015112830366", 500)  # Tarjeta válida según el algoritmo de Luhn
cuenta = CuentaBancaria("Juan Pérez", 1000, tarjeta)

# Operaciones
cuenta.depositar(200)
cuenta.retirar(150)
cuenta.realizar_pago_tarjeta(300)
print("Saldo final en cuenta:", cuenta.consultar_saldo())
print("Saldo pendiente en tarjeta:", tarjeta.consultar_saldo_pendiente())
