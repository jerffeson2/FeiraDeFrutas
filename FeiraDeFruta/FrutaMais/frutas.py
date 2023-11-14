

class FeiraDeFrutas:
    def __init__(self):
        self.estoque = {}

    def adicionar_fruta(self, fruta, quantidade):
        if fruta in self.estoque:
            self.estoque[fruta] += quantidade
        else:
            self.estoque[fruta] = quantidade

    def comprar_fruta(self, fruta, quantidade):
        if fruta in self.estoque:
            if self.estoque[fruta] >= quantidade:
                self.estoque[fruta] -= quantidade
            else:
                print(f"Não há quantidade suficiente de {fruta} no estoque.")
        else:
            print(f"{fruta} não está disponível na feira.")

    def verificar_estoque(self):
        return self.estoque


# Exemplo de uso:
feira = FeiraDeFrutas()
feira.adicionar_fruta('Maçã', 10)
feira.adicionar_fruta('Banana', 15)
feira.adicionar_fruta('Pera', 8)

feira.comprar_fruta('Maçã', 5)
feira.comprar_fruta('Banana', 20)

estoque_atual = feira.verificar_estoque()
print(estoque_atual)
