from calendar import c
import re
from wsgiref import validate
from flask_restful import Resource
from api import api
from api.models import curso_model
from api.schemas import curso_schema
from flask import jsonify, request, make_response
from ..entidades import curso
from ..services import curso_service
from ..models import curso_model
from datetime import datetime



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
        
class CursoDetail(Resource):
    def get(self, id):
        curso_bd = curso_service.listar_curso_id(id)
        if not curso_bd:
            return make_response(jsonify({'message': 'Curso não encontrado'}), 404)

        cs = curso_schema.CursoSchema()
        return make_response(cs.jsonify(curso_bd), 200)


    def put(self, id):
        curso_bd = curso_service.listar_curso_id(id)
        if not curso_bd:
            return make_response(jsonify({'message': 'Curso não encontrado'}), 404)

        cs = curso_schema.CursoSchema()

        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)

        nome = request.json['nome']
        descricao = request.json['descricao']
        data_publicacao_str = request.json['data_publicacao']

        # Converta a string de data para um objeto datetime
        try:
            data_publicacao = datetime.strptime(data_publicacao_str, '%Y-%m-%d').date()
        except ValueError:
            return make_response(jsonify({'message': 'Formato de data inválido, use YYYY-MM-DD'}), 400)

        novo_curso = curso.Curso(
            id = curso_bd.id,
            nome = nome,
            descricao = descricao,
            data_publicacao = data_publicacao
        )

        resultado = curso_service.atualiza_curso(curso_bd, novo_curso)

        return make_response(cs.jsonify(resultado), 200)


        
    def delete(self, id):
        return make_response(curso_service.delete_curso_id(id), 200)

api.add_resource(CursoList, '/cursos')
api.add_resource(CursoDetail, '/cursos/<int:id>')