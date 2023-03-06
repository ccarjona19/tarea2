from sqlalchemy import Column, String, Integer
from conexion import base, engine, session_create

class Slangs(base):
    __tablename__ = 'Slangs'

    diccionario = {
        1:{"palabra": "tongo", "significado": "policia"},
        2:{"palabra": "gringo", "significado": "persona de origen anglo no habla espaniol"},
        3:{"palabra": "mopri", "significado": "primo"},
        4:{"palabra": "llesca", "significado": "calle"},
        5:{"palabra": "compa", "significado": "compadre"}
    }
    
    id = Column(Integer, primary_key=True)
    palabra = Column(String(50))
    significado = Column(String(255))

    def __init__(self, palabra, significado):
        self.palabra = palabra
        self.significado = significado

    @classmethod
    def insertar(base, session):
        for llave, valor in base.diccionario.items():
            diccionario = session.query(base).filter(base.palabra == valor['palabra']).first()

            if diccionario:
                diccionario.significado = valor['significado']
            else:
                diccionario = base(palabra=valor['palabra'], significado=valor['significado'])
                session.add(diccionario)
                
        session.commit()



