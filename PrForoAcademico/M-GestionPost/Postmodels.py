import reflex as rx
from datetime import datetime
from typing import List

class Category(rx.Model, table = True):
    nombre: str

class Post(rx.Model, table=True):

    autor: str
    titulo: str
    content: str
    categoriaId: int
    contadorVotos: int = 0
    status: str = "activo"
    creadoEl: datetime = datetime.now()
    actualizadoEl: datetime = datetime.now()

class Comment(rx.Model, table=True):
    postId: int
    autor: str
    contenido: str
    contadorVotos: int=0
    creadoEl: datetime = datetime.now()

class Interaccion(rx.Model, table=True):
    usuarioId: int
    postId: int
    valor: int