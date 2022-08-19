from gerenciadorestoque import Gerenciador

class IntGrafica(object):

    def __init__(self) ->None:
        self.gen = Gerenciador()

    def adicionar(self) -> None:
        #O usuario vai digitar as caracteristicas do produto 
        nome = input("Digite o nome do produto : ") 
        codigo = input("Digite o codigo de barra: ") 
        valor = input("Digite o valor do produto: ") 
        quantidade = input("Digite a quantidade: ") 
        
        #Aqui ele vai adicionar os produtos
        if self.gen.adicionar(nome,codigo,valor,quantidade):
            print("Seu produto foi  cadastrado com sucesso!!")
        else:
            print("!!! Ja existe um produto com esses dados !!!")
        #nesta parte estamos removendo os produtos 
    def remover_item(self) -> None:
        nome = input("Digite o título: ")
        if self.gen.remover_item(nome):
            print("Seu produto foi removido com sucesso!")
        else:
            print("Seu Produto não esta sendo encontrado ")
        #colocar o produto na  lista
    def listar(self) -> None:
        estoque = self.gen.listar()
        for estoque in estoque:
            print("--------------------")
            print("Nome do produto: ", estoque.nome)
        print("Fim da listagem de produtos ")

    def imprimir_menu(self) -> None:
        print("-------------------Menu--------------")
        print("|        1- Cadastrar produto        |")
        print("|        2- Remover produto          |")
        print("|        3- Listar Produtos          |")
        print("|        4- Fechar programa          |")
        print("-------------------------------------")
       
        #Configurarçao do menu
    def main(self):
        sair = False
        while not sair:
            self.imprimir_menu()
            opcao = int(input("O que você deseja fazer: "))
            if opcao == 1:
                self.adicionar()
            elif opcao == 2:
                self.remover_item()
            elif opcao == 3:
                self.listar()
            elif opcao == 4:
                sair = True
            else:
                print("Opção inválida!")

if __name__ == "__main__":
    app = IntGrafica()
    app.main()
