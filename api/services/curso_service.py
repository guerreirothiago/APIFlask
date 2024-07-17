from api.entidades import curso
from ..models import curso_model
from api import db

def create_curso(curso):
    curso_bd = curso_model.Curso(
        nome = curso.nome,
        descricao = curso.descricao,
        data_publicacao = curso.data_publicacao
    )

    db.session.add(curso_bd)
    db.session.commit()

    return curso_model.Curso(
        id = curso_bd.id,
        nome = curso_bd.nome,
        descricao = curso_bd.descricao,
        data_publicacao = curso_bd.data_publicacao
    )

def listar_cursos():
    cursos = curso_model.Curso.query.all()

    return [curso_model.Curso(
        id = curso.id,
        nome = curso.nome,
        descricao = curso.descricao,
        data_publicacao = curso.data_publicacao
    ) for curso in cursos]

def listar_curso_id(id):
    return curso_model.Curso.query.filter_by(id=id).first()


def atualiza_curso(curso_anterior, curso_novo):
    curso_anterior.nome = curso_novo.nome
    curso_anterior.descricao = curso_novo.descricao
    curso_anterior.data_publicacao = curso_novo.data_publicacao
    db.session.commit()
    print(f"Curso atualizado: {curso_anterior.nome}, {curso_anterior.descricao}, {curso_anterior.data_publicacao}")
    return curso_anterior