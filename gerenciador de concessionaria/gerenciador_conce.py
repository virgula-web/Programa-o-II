

class Concessionaria(object):
    """[Concessionaria]

    Args:
        object ([type]): [Concessionaria sera responsavel por carros]
    """

    def __init__(self,marca:str,modelo:str,cor:str,placa:str) -> None:
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.placa = placa

    def __repr__(self) -> str:
        return ("marca"+ " " + self.marca + "," + "Modelo"+ " " + self.modelo + "," +  "cor" + " " + self.cor + "," + "placa" + self.placa)
    
    def converter_str(self):
        """[converter_str]

        Returns:
            [type]: [converter_str vai transformar em string]
        """
        return self.marca +" -- "+ self.modelo +" -- "+ self.cor +" -- "+ self.placa


class Motocicleta(Concessionaria):
    """[Motocicleta]
       [Motocicleta estara dentro da concessionaria sendo responsavel por motos e tendo alguns valores extras]
    """ 
    def __init__(self,marca,modelo,cor,placa, cilindrada)->None:
        super().__init__(marca, modelo, cor, placa) 
        self.cilindrada = cilindrada

    def __repr__(self) -> str:
        return ("marca"+ " " + self.marca + "," + "Modelo"+ " " + self.modelo + "," +  "cor" + " " + self.cor + "," + "placa" + self.placa + "," + str(self.cilindrada))

class Gerenciador(object):
    """[Gerenciador]

    Args:
        object ([type]): [Gerenciador cuidara da parte do gerenciamento da concessionaria]
    """
    def __init__(self)->None:
        self.lista_veiculos = []


    def carregar_lista_veiculos(self, lista: list)-> None:
        """[carregar_lista_veiculos]

        Args:
            lista (list): [sera uma lista para os veiculos tanto carro como moto]
        """
        self.lista_veiculos = lista

      
    def set_carro(self,marca:str,modelo:str,cor:str,placa:str)->None:
        novo_carro  =  Concessionaria ( marca,modelo,cor,placa)
        """[set_carro]

        Returns:
            [adicionar]: [O set_carro vai pegar e vai conferir se tenha algum carro com os dados iguais e se nao tiver ele ira adiciona-lo]
        """
        if not self.localizar_veiculo(novo_carro):
            self.lista_veiculos.append(novo_carro)
            return True
        return False


    def set_moto(self,marca:str,modelo:str,cor:str,placa:str,cilindrada:int)->None:
        """[set_moto]

        Returns:
            [adicionar]: [O set_moto vai pegar e vai conferir se tenha algum carro com os dados iguais e se nao tiver ele ira adiciona-lo]
        """  
        nova_moto  =  Motocicleta ( marca,modelo,cor,placa,cilindrada)
        if not self.localizar_moto(nova_moto):
            self.lista_veiculos.append(nova_moto)
            return True
        return False 
            
    def localizar_veiculo(self,  gerenciador: Concessionaria)->bool:
        """[localizar_veiculo]

        Args:
            gerenciador (Concessionaria): [vai utilizar os valores do construtor]

        Returns:
            bool: [localizar_veiculo vai ver o carro que esta na lista_veiculos e se o carro que tiver la ele retornara True ]
        """
        for car in self.lista_veiculos:
            if car == gerenciador:
                return True
        return False 

    def localizar_moto(self,  gerenciador: Motocicleta)->bool:
        """[localizar_moto]

        Args:
            gerenciador (Concessionaria): [vai utilizar os valores do construtor]

        Returns:
            bool: [localizar_moto vai ver o carro que esta na lista_veiculos e se o carro que tiver la ele retornara True ]               
        """
        for bike in self.lista_veiculos:
            if bike == gerenciador:
                return True
        return False 
    


    def get_carro(self,marca:str,modelo:str,cor:str,placa:str) -> bool: 
        """  [get_carro]
            [get_carro para o carro que esta na lista ele vai ver se a marca e a placa sao iguais se for igual ele removera retornando TRUE]

         """         
        for car in self.lista_veiculos:
            if car.marca == marca and car.placa == placa :
                self.lista_veiculos.remove(car)
                return True 
        return False

    def get_moto(self,marca:str,modelo:str,cor:str,placa:str,cilindrada:int = None) -> bool:   
        """  [get_carro]
             [get_moto para o carro que esta na lista ele vai ver se a marca e a placa sao iguais se for igual ele removera retornando TRUE]

         """         
        for bike in self.lista_veiculos:
            if bike.marca == marca and bike.placa == placa :
                self.lista_veiculos.remove(bike)
                return True 
        return False

# vai imprimir oque esta no estoque
    def imprimir_estoque(self):
        for car in self.lista_veiculos:
            print(car)

    def imprimir_estoque_moto(self):
        for bike in self.lista_veiculos:
            print(bike)



if __name__ == "__main__":



    ger = Gerenciador()
    # fiz o teste basico adicionando 4 carros e para saber se esta correto ele vai printar 4 true e 4 carros 
    print(ger.set_carro("bmw","m5","preto","1551454515"))
    print(ger.set_carro("bmw","m5","preto","1551454515"))
    print(ger.set_carro("bmw","m5","preto","1551454515"))
    print(ger.set_carro("bmw","m5","preto","1551454515"))
    ger.imprimir_estoque()
    print("---------------------------------------------")
    # neste teste removi 3 veiculos dos 4 que adicionei e mostrei o estoque , para saber se esta correto ele vai mostra o nome do carro que sobrou
    print(ger.get_carro("bmw","m5","preto","1551454515"))
    print(ger.get_carro("bmw","m5","preto","1551454515"))
    print(ger.get_carro("bmw","m5","preto","1551454515"))
    ger.imprimir_estoque()
    print("---------------------------------------------")

    print(ger.set_moto("yamanha","mt09","preto","fafafag515",847))
    print(ger.set_moto("yamanha","mt09","preto","fafafag515",847))
    print(ger.set_moto("yamanha","mt09","preto","fafafag515",847))
    print(ger.set_moto("yamanha","mt09","preto","fafafag515",847))
    ger.imprimir_estoque_moto()
    print("---------------------------------------------")
    # neste teste removi 3 veiculos dos 4 que adicionei e mostrei o estoque , para saber se esta correto ele vai mostra o nome do carro que sobrou
    print(ger.get_moto("yamanha","mt09","preto","fafafag515",847))
    print(ger.get_moto("yamanha","mt09","preto","fafafag515",847))
    print(ger.get_moto("yamanha","mt09","preto","fafafag515",847))
    ger.imprimir_estoque_moto()
    print("---------------------------------------------")
