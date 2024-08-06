import pessoas
import contas


class Banco:
    def __init__(
            self,
            agencias: list[int] | None = None,
            clientes: list[pessoas.Pessoa] | None = None,
            contas: list[int] | None = None,
    ):
        self.agencias = agencias
        self.clientes = clientes
        self.contas = contas

       
