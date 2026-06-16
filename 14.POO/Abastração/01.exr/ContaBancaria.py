class ContaBancaria:
    """
    Cria uma conta bancaria que permite fazer saques e depositos
    """

    def __init__(self, Id, nome, saldo =0):
        self.id = Id #publico
        self._titular = nome #protegido
        self.__saldo = saldo #privado
        print(f"Conta {self.id} criada com sucesso. Saldo actual de {self.__saldo:,.2f}£")

    def __str__(self):
        return f"A conta {self.id} de {self._titular} tem {self.__saldo:,.2f}£"
         

    def despositar(self, valor):
        self.__saldo += valor
        print(f"Desposito de {valor:,.2f}£ autorizado na conta {self.id}")

    def sacar(self, valor):
        if valor > self.__saldo:
            print(f'Saque de {valor:,.2f}£ NEGADO na conta {self.id}. SALDO INSUFICIENTE')
        
        else:
            self.__saldo -= valor
            print(f'O saque de {valor:,.2f}£ foi autorizado na conta {self.id}')




