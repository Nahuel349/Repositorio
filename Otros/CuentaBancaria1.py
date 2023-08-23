class CuentaBancaria:
    cuentas_bancarias = []
    def __init__(self, tasa_interes, balance):
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.cuentas_bancarias.append(self)

    def deposito(self, amount): #methodo deposito
        self.balance += amount
        print(f"Se ha realizado un depósito de {amount}, su nuevo balance es: {self.balance}")
        return self

    def retiro(self, amount): #methodo retiro disminuye el balance de la cuenta en el monto dado si hay fondos suficientes; si no hay suficiente dinero, imprime el mensaje: "Fondos insuficientes: cobrando una tarifa de $5", y resta $5
        if CuentaBancaria.puede_retirar(self.balance,amount):
            self.balance -= amount
            print(f"Se ha realizado un retiro de {amount}, su nuevo balance es: {self.balance}")
        else:
            print("Fondos insuficientes se cobrara una tarifa de $5")
            self.balance -= 5 #se cobran 5
        return self
    
    @staticmethod
    def puede_retirar(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

    def generar_interes(self):
        interes_generado = self.balance * self.tasa_interes
        self.balance += interes_generado
        print(f"Se ha generado un interes de: {interes_generado}")
        return self
    
    def mostrar_info_cuenta(self): #methodo retiro
        print(f"Nuevo balance: {self.balance}")
        return self

    @classmethod
    def imprimir_informacion_cuentasBancarias(cls):
        for cadacuenta in cls.cuentas_bancarias:
            print(f"Balance: {cadacuenta.balance}, su Interes generado {cadacuenta.tasa_interes}")

# Crear una instancia de CuentaBancaria
cuenta1 = CuentaBancaria(0.01, 1000)
cuenta2 = CuentaBancaria(0.01, 2000)

# Realizar depósitos, retiros en la cuenta y mostrar balance
cuenta1.deposito(500).deposito(100).deposito(600).retiro(200).generar_interes().mostrar_info_cuenta()
cuenta2.deposito(800).deposito(800).retiro(100).retiro(100).retiro(100).retiro(100).generar_interes().mostrar_info_cuenta()

#imprime la informacion de todas las cuentas
CuentaBancaria.imprimir_informacion_cuentasBancarias()