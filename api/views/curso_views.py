from wsgiref import validate
from flask_restful import Resource
from api import api
from api.models import curso_model
from api.schemas import curso_schema
from flask import jsonify, request, make_response
from ..entidades import curso
from ..services import curso_service
from ..models import curso_model


class CursoList(Resource):
    def get(self):
        cursos = curso_service.listar_cursos()
        cs = curso_schema.CursoSchema(many=True)

        return make_response(cs.jsonify(cursos), 200)

    def post(self):
        cs = curso_schema.CursoSchema()
        validate = cs.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            descricao = request.json['descricao']
            data_publicacao = request.json['data_publicacao']

            novo_curso = curso.Curso(
                id = None,
                nome = nome,
                descricao = descricao,
                data_publicacao = data_publicacao
            )

            resultado = curso_service.create_curso(novo_curso)
            x = cs.jsonify(resultado)

            return make_response(x, 201)

api.add_resource(CursoList, '/cursos')