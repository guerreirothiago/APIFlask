from api.entidades import formacao
from ..models import formacao_model
from api import db

def create_curso(formacao):
    formacao_bd = formacao_model.Curso(
        nome = formacao.nome,
        descricao = formacao.descricao
    )

    db.session.add(formacao_bd)
    db.session.commit()

    return formacao_model.Curso(
        id = formacao_bd.id,
        nome = formacao_bd.nome,
        descricao = formacao_bd.data_publicacao
    )

def listar_cursos():
    cursos = formacao_model.Curso.query.all()

    return formacao_model.Curso(
        id = formacao.id,
        nome = formacao.nome,
        descricao = formacao.descricao
    )

def listar_curso_id(id):
    return formacao_model.Curso.query.filter_by(id=id).first()


def atualiza_formacao(formacao_anterior, formacao_novo):
    formacao_anterior.nome = formacao_novo.nome
    formacao_anterior.descricao = formacao_novo.descricao
    db.session.commit()
    print(f"Formacao atualizado: {formacao_anterior.nome}, {formacao_anterior.descricao}")
    return formacao_anterior

def deleta_formacao(formacao):
    db.session.delete(formacao)
    db.session.commit()