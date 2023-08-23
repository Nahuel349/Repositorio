class CuentaBancaria:
    cuentas = []
    # ¡No olvides agregar algunos valores predeterminados para estos parámetros!

    def __init__(self, tasa_interes, balance): 
        self.tasa_interes = tasa_interes #(recuerda, los atributos de instancia van aquí)
        self.balance = balance
        CuentaBancaria.cuentas.append(self)
        # no te preocupes por la información del usuario aquí; pronto involucraremos la clase de usuario
    def deposito(self, amount):
        self.balance += amount
        return self
        # tu código aquí
    def retiro(self, amount):
        self.balance -= amount
        
        return self
        # tu código aquí
    def mostrar_info_cuenta(self):
        print(f'CuentaBancaria : {self.tasa_interes}, balance : ${self.balance}')
        return self
        # tu código aquí
    def generar_interes(self):
            if self.balance > 0:
                self.balance += (self.balance * self.tasa_interes)
                return self
            # tu código aquí
    @classmethod
    def imprimir_cuentas(cls):
        for cuenta in cls.cuentas:
            cuenta.mostrar_info_cuenta()  
class User:
    def __init__(self,nombre,email):
        self.nombre = nombre
        self.email = email
        self.cuenta = {
            "saldo" : CuentaBancaria(tasa_interes = 0.22 , balance = 0),
            "ahorro": CuentaBancaria(tasa_interes = 0.66, balance = 0)
        }
    def hacer_deposito(self, amount):
        self.cuenta['ahorro'].deposito(amount)
        return self
    def hacer_retiro(self,amount):
        self.cuenta['ahorro'].retiro(amount)
        return self
    def mostrar_balance_usuario(self):
        print(f"User: {self.nombre}, Saldo Balance: {self.cuenta['saldo'].mostrar_info_cuenta()}")
        print(f"User: {self.nombre}, Ahorro Balance: {self.cuenta['ahorro'].mostrar_info_cuenta()}")
        return self

