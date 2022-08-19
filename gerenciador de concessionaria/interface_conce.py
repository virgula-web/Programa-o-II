from gerenciador_conce import Gerenciador
from gravador_conce import Gravador_estoque   


class InterfaceConcessionaria:

    def __init__(self) -> None:
        self.ger = Gerenciador()

    def imprimir_menu(self):
        """[imprimir_menu]
            Vair imprimir um menu para mostrar as opçoes de funcionalidades  
        """
        print(" _________________________|-Menu-|________________________")
        print("|                                                         |")
        print("|        1- vender seu carro   2- comprar carro           |")
        print("|                                                         |")
        print("|        3- vender sua Moto    4- comprar Moto            |")
        print("|                                                         |")
        print("|        5- gravar             6- recuperar               |")
        print("|                                                         |")
        print("|                              7- fechar programa         |")
        print("|                                                         |")
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

    def adicionando_carro(self):
        """[adicionando_carro]
           [vai ir la para set_carro e se os dados inseriodos forem de acordo com oque ele pede retornara uma 
           mensagem de sucesso e caso isso nao acontecer mostrar uma de falha]
        """
        marca = input("Digite a marca do carro : ")
        modelo = input("Digite o modelo do carro : ")
        cor = input("Digite qual é a cor do carro :")
        placa = input("Digite a placa do carro: ")
        if  self.ger.set_carro(marca,modelo,cor,placa):
            print(" ___________________________________________________")
            print("|Sua venda foi concluida !!! Obrigado pela confiança|)")
            print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        else:
            print("Nao foi possivel realizar sua venda :(")

    def adicionando_moto(self):
        """[adicionando_moto]
            vai ir la para set_moto e se os dados inseriodos forem de acordo com oque ele pede retornara uma mensagem de sucesso e caso isso nao acontecer mostrar uma de falha
        """
        marca = input("Digite a marca do moto : ")
        modelo = input("Digite o modelo do moto : ")
        cor = input("Digite qual é a cor do moto :")
        placa = input("Digite a placa do moto: ")
        cilindrada = int(input("Digite quantas cilindradas tem na moto :"))
        if  self.ger.set_moto(marca,modelo,cor,placa,cilindrada):
            print(" ___________________________________________________")
            print("|Sua venda foi concluida !!! Obrigado pela confiança|)")
            print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        else:
            print("Nao foi possivel realizar sua venda :(")


    def removendo_carro(self):
        """[removendo_carro]
           o usuario ira colocar os dados e se forem iguais aos da lista ira remove-lo no caso o usuario ira comprar ele
        """
        marca = input("Digite a marca do carro : ")
        modelo = input("Digite o nome do carro : ")
        cor = input("Digite qual é a cor do carro :")
        placa = (input("Digite a placa do carro: "))
        if self.ger.get_carro(marca,modelo,cor,placa):
            print(" ___________________________________________________")
            print("|Sua compra foi concluida !!! Obrigado pela confiança|)")
            print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        else:
            print("Não foi possivel realizar sua compra estamos trabalhando nisso")

    def removendo_moto(self):
        """[removendo_moto]
           o usuario ira colocar os dados e se forem iguais aos da lista ira remove-lo no caso o usuario ira comprar ele
        """
        marca = input("Digite a marca da moto : ")
        modelo = input("Digite o nome da moto : ")
        cor = input("Digite qual é a cor da moto :")
        placa = (input("Digite a placa da moto: "))
        cilindrada = int(input("Digite quantas cilindradas tem na moto :"))
        if self.ger.get_moto(marca,modelo,cor,placa,cilindrada):
            print(" ___________________________________________________")
            print("|Sua compra foi concluida !!! Obrigado pela confiança|)")
            print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        else:
            print("Não foi possivel realizar sua compra estamos trabalhando nisso")



    
    def main(self):
        """[main]
            [main sera onde ocorreram suas escolhas]
            [tratamento de erro adicionei ValueError porque se o usuario no inicio do programa digita-se uma string ele dava erro e com 
            esse tratamento ele mosta uma mensagem e retorna o codigo funcionando]
        """
        sair = False
        while not sair:
            self.imprimir_menu()
            try:
                opcao = int(input("O que você deseja fazer: "))
                if opcao == 1:
                    self.adicionando_carro()
                elif opcao == 2:
                    self.removendo_carro()
                elif opcao == 3:
                    self.adicionando_moto()
                elif opcao == 4:
                    self.removendo_moto()
                elif opcao == 5:
                    gv = Gravador_estoque()
                    gv.gravar(self.ger.lista_veiculos)
                elif opcao == 6:
                    gv = Gravador_estoque()
                    lista = gv.recuperar()
                    self.ger.carregar_lista_veiculos(lista)
                elif opcao == 7:
                    sair = True
                else:
                    print("Opção inválida!")
            except ValueError:
                print("Ocorreu um ERRO tente novamente !!!")
            except UnboundLocalError:
                print("Vamos recomeçar")
            except IndexError:
                print("Ocorreu um erro de index!!!")



if __name__ == "__main__":
    interface = InterfaceConcessionaria()
    interface.main()


