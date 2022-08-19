from estoque import Produto 

class Gerenciador(object):

    def __init__(self):
        self.item = []

    def buscar_item(self, nome: str) -> Produto:
        for estoque in self.item:
            if estoque.nome == nome:
                return estoque
        return None

    def adicionar_item(self,nome:str,codigo:int,valor:float,quantidade:int) -> bool:           
        if self.buscar_item(nome) is None:
            novo_item = Produto(nome,codigo,valor,quantidade)
            self.item.append(novo_item)
            return True
        return False

    def remover_item(self, nome:str) -> bool:
        estoque = self.buscar_item(nome)
        if Produto is not None:
            self.item.remove(estoque)
            return True
        return False

    def listar(self) -> list:
        print(id(self.item))
        return self.item[:]
