from api.entidades import formacao
from ..models import formacao_model
from api import db

def create_formacao(formacao_entidade):
    nova_formacao = formacao_model.Formacao(
        nome=formacao_entidade.nome,
        descricao=formacao_entidade.descricao
    )
    db.session.add(nova_formacao)
    db.session.commit()
    print(f"Formacao criada: {nova_formacao.nome}, {nova_formacao.descricao}")
    return nova_formacao

def listar_formacoes():
    cursos = formacao_model.Formacao.query.all()

    return [formacao_model.Formacao(
        id = formacao.id,
        nome = formacao.nome,
        descricao = formacao.descricao
    ) for formacao in cursos]

def listar_formacao_id(id):
    return formacao_model.Formacao.query.filter_by(id=id).first()


def atualiza_formacao(formacao_anterior, formacao_novo):
    formacao_anterior.nome = formacao_novo.nome
    formacao_anterior.descricao = formacao_novo.descricao
    db.session.commit()
    print(f"Formacao atualizado: {formacao_anterior.nome}, {formacao_anterior.descricao}")
    return formacao_anterior

def deleta_formacao(formacao):
    db.session.delete(formacao)
    db.session.commit()