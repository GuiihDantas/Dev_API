from flask import Flask, request
from dataset import insertuser

app = Flask("Youtube")

#Testando a API
@app.route("/Testando a API", methods=["GET"])
def minha_api():
    return{"Teste":"Testando"}

#Cadastro de usuários e parâmetros de erro
@app.route("/cadastro", methods=["POST"])
def cadastrouser():
    body = request.get_json()
    if("nome" not in body):
        return geraResponse(400, "O parametro nome é Obrigatório")

    if ("email" not in body):
        return geraResponse(400, "O parametro email é Obrigatório")

    if ("senha" not in body):
        return geraResponse(400, "O parametro senha é Obrigatório")

    usuario = insertuser(body["nome"], body["email"], body["senha"])
    return geraResponse(200, "Usuario criado", "user" ,usuario)

#Mensagens de Status
def geraResponse(status, mensagem, nome_do_conteudo=False, conteudo=False):
    response = {}
    response["status"] = status
    response["mensagem"] = mensagem

    if(nome_do_conteudo and conteudo):
        response[nome_do_conteudo] = conteudo

    return response

#if __name__ == '__main__':
app.run(debug=True)

