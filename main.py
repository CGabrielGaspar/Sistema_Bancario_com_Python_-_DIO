import datetime


class Banco:
    def __init__(self):
        self.extrato = []
        self.saldo = 0.0
        self.limite_saque_diario = 500.0
        self.saques_diarios = 0

    def depositar(self, valor):
        """Deposita um valor na conta."""
        if valor > 0:
            self.saldo += valor
            self.extrato.append(('Depósito', valor, datetime.datetime.now()))
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor):
        """Saca um valor da conta."""
        if self.saques_diarios >= 3:
            print("Limite de saques diários atingido.")
        elif valor > self.limite_saque_diario:
            print(f"Limite de saque excedido. Valor máximo de saque: R$ {self.limite_saque_diario:.2f}")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            self.extrato.append(('Saque', valor, datetime.datetime.now()))
            self.saques_diarios += 1

    def visualizar_extrato(self):
        """Imprime o extrato da conta."""
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            for operacao, valor, data in self.extrato:
                print(f"{operacao} de R$ {valor:.2f} em {data.strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Saldo atual: R$ {self.saldo:.2f}")


if __name__ == "__main__":
    banco = Banco()
    while True:
        print("1: Depositar")
        print("2: Sacar")
        print("3: Visualizar extrato")
        print("4: Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            valor = float(input("Digite o valor a ser depositado: "))
            banco.depositar(valor)
        elif opcao == '2':
            valor = float(input("Digite o valor a ser sacado: "))
            banco.sacar(valor)
        elif opcao == '3':
            banco.visualizar_extrato()
        elif opcao == '4':
            break
        else:
            print("Opção inválida.")
        print("")
