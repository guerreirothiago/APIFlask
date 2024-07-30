from flask_restful import Resource
from api import api
from api.schemas import formacao_schema
from flask import jsonify, request, make_response
from ..entidades import formacao
from ..services import formacao_service
from ..models import formacao_model



class FormacaoList(Resource):
    def get(self):
        formacoes = formacao_service.listar_formacoes()
        fs = formacao_schema.FormacaoSchema(many=True)

        return make_response(fs.jsonify(formacoes), 200)
    

    def post(self):
        fs = formacao_schema.FormacaoSchema()
        validate = fs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        
        nome = request.json['nome']
        descricao = request.json['descricao']

        nova_formacao = formacao.Formacao(
            id = None,
            nome = nome,
            descricao = descricao
        )

        resultado = formacao_service.create_formacao(nova_formacao)
        fs = formacao_schema.FormacaoSchema()
        return make_response(fs.jsonify(resultado), 201)
        
class FormacaoDetail(Resource):
    def get(self, id):
        formacao_bd = formacao_service.listar_formacao_id(id)
        if not formacao_bd:
            return make_response(jsonify({'message': 'Formação não encontrado'}), 404)

        fs = formacao_schema.FormacaoSchema()
        return make_response(fs.jsonify(formacao_bd), 200)


    def put(self, id):
        formacao_bd = formacao_service.listar_formacao_id(id)
        if not formacao_bd:
            return make_response(jsonify({'message': 'Formação não encontrado'}), 404)

        fs = formacao_schema.FormacaoSchema()

        validate = fs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)

        nome = request.json['nome']
        descricao = request.json['descricao']

        nova_formacao = formacao.Formacao(
            id = formacao_bd.id,
            nome = nome,
            descricao = descricao
        )

        resultado = formacao_service.atualiza_formacao(formacao_bd, nova_formacao)

        return make_response(fs.jsonify(resultado), 200)


        
    def delete(self, id):
        formacao_bd = formacao_service.listar_formacao_id(id)
        if not formacao_bd:
            return make_response(jsonify({'message': 'Formação não encontrado'}), 404)
        
        formacao_service.deleta_formacao(formacao_bd)
        return make_response('Formação excluido com sucesso', 204)

api.add_resource(FormacaoList, '/formacoes')
api.add_resource(FormacaoDetail, '/formacoes/<int:id>')