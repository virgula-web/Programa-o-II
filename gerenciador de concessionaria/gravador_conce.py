from gerenciador_conce import Concessionaria,Motocicleta

class Gravador_estoque(object):

    def gravar(self, lista_) -> None:
        """[gravar]

        Args:
            lista_ ([type]): [Quando o usuario escolher a opção 5 ele abrira um arquivo que se chama gravador_conce,este arquivo servira como um metodo para guardar dados ]
        """
        arquivo = open("gravador_conce.txt", "w")
        for car in lista_:
            arquivo.write(car.converter_str()+"\n")
        arquivo.close()

        

    def recuperar(self) -> list:
        """[recuperar]

        Returns:
            list: [recuperar tera quase o mesmo procedimento de gravar mas aqui ele ira recuperar oque havi no arquivo]
        """
        arquivo = open("gravador_conce.txt", "r")
        lista = []
        for linha in arquivo.readlines():
            linha = linha.replace("\n", "")
            info = linha.split(" ")
            car = Concessionaria( info[0], info[1], info[2], info[3])
            lista.append(car)
        arquivo.close()
        return lista


