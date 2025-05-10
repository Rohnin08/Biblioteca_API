from pydantic import BaseModel
from uuid import UUID
from datetime import date
from typing import List

class Livro(BaseModel):
    id:UUID
    titulo:str
    autor:str
    publicacao:int
    disponibilidade:bool = True

class Leitor(BaseModel):
    id:UUID
    nome:str
    livrosQuePossui: List[Livro] = []

class Emprestimo(BaseModel):
    id:UUID
    dataEmprestimo:date
    dataDevolucao:date 
