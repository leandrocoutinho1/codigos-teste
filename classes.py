class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ["basic", "premium"]
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception("Plano inválido")
    
    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            if novo_plano == self.plano:
                print(f"O plano {novo_plano} já está em utilização!")
            else:
                self.plano = novo_plano
                print("Alteração realizada com sucesso.")
        else:
            raise Exception("Plano inválido")
    

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f"Ver filme {filme}")
        elif self.plano == "premium":
            print(f"Ver filme {filme}")
        elif self.plano == "basic" and plano_filme == "premium":
            print("Faça upgrade para premium para ver esse filme")
        else:
            print("Plano inválido")






cliente = Cliente("Leandro", "leandro@gmail.com", "basic")

print(f"Nome: {cliente.nome}, email: {cliente.email},Plano: {cliente.plano}")

cliente.ver_filme("Harry Potter", "premium")

cliente.mudar_plano("premium")

cliente.ver_filme("Harry Potter", "premium")
