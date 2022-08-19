class Produto(object):

     def __init__(self,nome:str,codigo:int,valor:float,quantidade:int) -> None:
         self.nome = nome
         self.codigo = codigo
         self.valor = valor
         self.quantidade = quantidade