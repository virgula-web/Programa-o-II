from sqlalchemy import true
from config import *

class Casa (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    formato = db.Column(db.String(254))
    
    # lista reversa!
    quartos = db.relationship("Quarto", backref="casa")

    def __str__(self):
        return f'Casa: {self.formato}'        
        
class Quarto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    dimensoes = db.Column(db.String(254))
    casa_id = db.Column(db.Integer, db.ForeignKey(Casa.id), nullable=False)
    mobilias = db.relationship("Mobilia", backref="quarto")

    def __str__(self):
        s = f'Quarto: {self.nome}, {self.dimensoes}, em: {str(self.casa)}'
        s += f'na casa: {str(self.casa)}'          
        return s

class Mobilia(db.Model):
    id = db.Column(db.Integer,primary_key=true)
    nome = db.Column(db.String(254))
    utilidade = db.Column(db.String(254))
    material = db.Column(db.String(254))
    quarto_id = db.Column(db.Integer, db.ForeignKey(Quarto.id),nullable=True) 

    def __str__(self):
        s = f'Mobilia: {self.nome}, {self.utilidade},{self.material}, Quarto: {self.quarto}'
        return s


if __name__ == "__main__": # teste das classes
    
    if os.path.exists(arquivobd): # se houver o arquivo...
        os.remove(arquivobd) # ...apagar!

    db.create_all() # criar tabelas

    c1 = Casa(formato="Germânica") # cria uma casa
    db.session.add(c1)
    db.session.commit()

    print(c1) # exibir atributos da casa

    q1 = Quarto(nome="Sala", dimensoes="6x5 metros", casa=c1)
    q2 = Quarto(nome="Banheiro", dimensoes="3x4 metros", casa=c1)
    
    db.session.add(q1)
    db.session.add(q2)
    db.session.commit()

    print(q1, q2)

    m1 = Mobilia(nome="Cadeira",utilidade = "descanso", material = "madeira" ,quarto_id=q1.id)
    db.session.add(m1)
    db.session.commit()


    print(m1)