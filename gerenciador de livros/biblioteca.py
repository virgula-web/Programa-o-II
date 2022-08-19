         
class Livro(object):
        def __init__(self,fisico:bool ,nome:str,assunto:str,resumo:str,isbn:int)->None:
      
            self.fisico = fisico
            self.nome = nome
            self.assunto = assunto
            self.resumo = resumo
            self.isbn = None


     
            def definindo_fisico(self):             
                self.fisico = True                  
                                                    
            def definindo_digital(self):            
                self.fisico = False               
                                                       
                                                            
                                                     
l1 = Livro(True,"game","assunto","resumo","isbn")                                    
l2 = Livro(False,"game","assunto","resumo","isbn")                                   
                                                    

                                                         
print("O seu livro 1 é físico?",l1.fisico)          
print("O seu livro 2 é físico?",l2.fisico)          
                                                    
  







