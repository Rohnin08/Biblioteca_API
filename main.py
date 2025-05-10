from fastapi import FastAPI, HTTPException
from models import Livro, Leitor, Emprestimo
from typing import List
from uuid import UUID

app = FastAPI()

livros: List[Livro] = []
leitores: List[Leitor] = []
emprestimos: List[Emprestimo] = []

# LIVROS
@app.get("/livros/", response_model=List[Livro])
def listar_livros():
    return livros

@app.post("/livros/", response_model=Livro)
def criar_livro(livro: Livro):
    livros.append(livro)
    return livro

@app.get("/livros/{id}", response_model=Livro)
def obter_livro(id: UUID):
    for livro in livros:
        if livro.id == id:
            return livro
    raise HTTPException(status_code=404, detail="Livro não encontrado")

# LEITORES
@app.get("/leitores/", response_model=List[Leitor])
def listar_leitores():
    return leitores

@app.post("/leitores/", response_model=Leitor)
def criar_leitor(leitor: Leitor):
    leitores.append(leitor)
    return leitor

@app.get("/leitores/{id}", response_model=Leitor)
def obter_leitor(id: UUID):
    for leitor in leitores:
        if leitor.id == id:
            return leitor
    raise HTTPException(status_code=404, detail="Leitor não encontrado")

# EMPRESTIMOS
@app.get("/emprestimos/", response_model=List[Emprestimo])
def listar_emprestimos():
    return emprestimos

@app.post("/emprestimos/", response_model=Emprestimo)
def fazer_emprestimo(emprestimo: Emprestimo):
    emprestimos.append(emprestimo)
    return emprestimo

@app.get("/emprestimos/{id}", response_model=Emprestimo)
def obter_emprestimo(id: UUID):
    for emprestimo in emprestimos:
        if emprestimo.id == id:
            return emprestimo
    raise HTTPException(status_code=404, detail="Empréstimo não encontrado")
