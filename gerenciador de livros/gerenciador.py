from biblioteca import Livro





class Gerenciador(object):
        def __init__(self)->None:
            self.lista_de_livro = []

        def adicionar_livro(self,fisico:str,nome:str,assunto:str,resumo:str,isbn:int)->None:
            novo_book  =  Livro ( fisico,nome,assunto,resumo,isbn)
            if not self.procurar_livro(novo_book):
                self.lista_de_livro.append(novo_book)
                return True
            return False


        def procurar_livro(self,  biblioteca: Livro)->bool:
            for book in self.lista_de_livro:
                if book == biblioteca:
                    return True
            return False

        def remover_livro(self,fisico:bool,nome:str,assunto:str,resumo:str,isbn:int) -> bool:
            for book in self.lista_de_livro:
                if book.nome == nome and book.assunto == assunto:
                    self.lista_de_livro.remove(book)
                    return True 
            return False
        
        def emprestimo(self,fisico:bool,nome:str,assunto:str,resumo:str,isbn:int):
            for book in self.lista_de_livro:
                if book.nome == nome and book.isbn == isbn:
                    self.lista_de_livro.remove(book)
                    return True
                return False
        
        def devolucao(self,fisico:str,nome:str,assunto:str,resumo:str,isbn:int):
            devolvendo = Livro(fisico,nome,assunto,resumo,isbn)
            if not self.procurar_livro(devolvendo):
                self.lista_de_livro.append(devolvendo)
                return True
            return False


        def imprimir_lista(self):
            for book in self.lista_de_livro:
                print("Livro Fisico",book.fisico, "Nome do livro",book.nome,"Assunto",book.assunto,"Resumo",book.resumo,"ISBN",book.isbn)
        print("------------fim da lista-----------------")



if __name__ == "__main__":
    gen = Gerenciador()
    print(gen.adicionar_livro("fisico","game","assunto","resumo","isbn"))
    print(gen.adicionar_livro("fisico","game","assunto","resumo","isbn"))
    print(gen.adicionar_livro("fisico","game","assunto","resumo","isbn"))
    print(gen.adicionar_livro("fisico","game","assunto","resumo","isbn"))
    gen.imprimir_lista()
    print(gen.remover_livro("fisico","game","assunto","resumo","isbn"))
    print(gen.remover_livro("fisico","game","assunto","resumo","isbn"))
    print(gen.remover_livro("fisico","game","assunto","resumo","isbn"))
    print(gen.remover_livro("fisico","game","assunto","resumo","isbn"))
    gen.imprimir_lista()
    print(gen.emprestimo("fisico","game","assunto","resumo","isbn"))
    print(gen.devolucao("fisico","game","assunto","resumo","isbn"))
    gen.imprimir_lista()

    print("---------------------fim da lista-----------------------------------")
