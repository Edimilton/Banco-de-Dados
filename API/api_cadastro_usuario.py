from flask import Flask, request, jsonify

# Estrutura do objeto usuario
class Usuario:
    def __init__(self, cpf, nome, data_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


# Lista de usuarios cadastrados
usuarios = []


app = Flask(__name__)


# Rota para cadastrar um novo usuario
@app.route('/usuarios', methods=['POST'])
def cadastrar_usuario():
    # Dados do usuario da requisição POST
    cpf = request.json['cpf']
    nome = request.json['nome']
    data_nascimento = request.json['data_nascimento']

    # adiciona o usuario à lista
    usuario = Usuario(cpf, nome, data_nascimento)
    usuarios.append(usuario)

    # Mensagem de sucesso
    return jsonify({'mensagem': 'Usuario cadastrado com sucesso!'})


# Rota para buscar um usuario pelo CPF
@app.route('/usuarios/<int:cpf>', methods=['GET'])
def buscar_usuario(cpf):
    # percorre a lista de usuarios em busca do usuario com o CPF informado
    for usuario in usuarios:
        if usuario.cpf == cpf:
            # retorna os dados do usuario
            return jsonify({
                'cpf': usuario.cpf,
                'nome': usuario.nome,
                'data_nascimento': usuario.data_nascimento
            })
    # retorna uma mensagem de erro caso o usuario nao seja encontrado
    return jsonify({'mensagem': 'Usuario nao encontrado!'}), 404


if __name__ == '__main__':
    app.run(debug=True)
