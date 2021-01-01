from flask import Flask, request
from flask_restful import Resource, Api
import json

lista_habilidades = ['Python', 'Java', 'Flask', 'PHP', 'UX', 'BackEnd', 'FrontEnd']
class Habilidades(Resource):
    def get(self):
        return lista_habilidades

    def put(self):
        return lista_habilidades

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


