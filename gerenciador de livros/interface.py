from gerenciador import Gerenciador
    



class InterfaceGerenciador:

    def __init__(self) -> None:
        self.gen = Gerenciador()

    def imprimir_menu(self):
        print(" ______________|-Menu-|________________")
        print("|/       1- Cadastrar novo livro      \|")
        print("|--------------------------------------|")
        print("|\       2- Remover  livro            /|")
        print("|--------------------------------------|")
        print("|/       3- Listar novo livro         \|")
        print("|--------------------------------------|")
        print("|/       4- Emprestar livro           \|")
        print("|--------------------------------------|")
        print("|/       5- Devolver livro            \|")
        print("|--------------------------------------|")
        print("|\       6- Sair                      /|")
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

    def cadastrar_livro(self):
        fisico = input("Digite o tipo: ")
        if fisico == "fisico":
            fisico = True
        else:
            fisico = False 
        nome = input("Nome do livro : ")
        assunto = input("Assunto do livro :")
        resumo = input("Resumo do livro :")
        isbn= int(input("Isbn : "))
        if self.gen.adicionar_livro(fisico,nome,assunto, resumo, isbn):
            print(" ______________________________")
            print("|Livro cadastrado com sucesso :|)")
            print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        else:
            print("Erro ao cadastrar a livro :(")

    def remover_livro(self):
        nome = input("Nome do livro ")
        assunto = input("Assunto do livro :")
        resumo = input("Resumo do livro :")
        isbn = int(input("Codigo isbn do livro: "))
        if self.gen.remover_livro(nome,assunto, resumo, isbn):
            print("Livro removido com sucesso :)")
        else:
            print("Erro ao remover livro :(")

    def emprestimo(self):
        fisico = "Livro fisico"
        nome =  input("Digite o nome do livro que voce vair pegar emprestado :")
        assunto = input("Assunto do livro :")
        resumo = input("Resumo do livro :")
        isbn = input("ISBN livro que voce esta pegando emprestado :")
        if self.gen.emprestimo(fisico,nome,assunto,resumo, isbn):
                print("O usuario tem 7 dias para devolver o livro")
        else:
                print("Erro ao emprestar")


    def devolucao(self):

        fisico = "Livro fisico"
        nome =  input("Digite o nome que voce vair devolver :")
        assunto = input("Assunto do livro :")
        resumo = input("Resumo do livro :")
        isbn = input("ISBN livro que voce esta devolvendo :")
        if self.gen.adicionar_livro(fisico,nome,assunto,resumo, isbn):
                print("Devolvido com sucesso")
        else:
                print("Erro ao devolver livro")


    def listar_livro(self):
        for book in self.gen.lista_de_livro:
            print("Nome do livro ", book.nome, " Codigo isbn ", book.isbn)
        print("------------fim da lista-----------------")

    def main(self):
        sair = False
        while not sair:
            self.imprimir_menu()
            opcao = int(input("O que você deseja fazer: "))
            if opcao == 1:
                self.cadastrar_livro()
            elif opcao == 2:
                self.remover_livro()
            elif opcao == 3:
                self.listar_livro()
            elif opcao == 4:
                self.emprestimo()
            elif opcao == 5:
                self.devolucao()
            elif opcao == 6:
                sair = True
            else:
                print("Opção inválida!")


if __name__ == "__main__":
    inter = InterfaceGerenciador()
    inter.main()
