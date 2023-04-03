# Flask API para cadastro e busca de usuários
Esta API é uma aplicação simples desenvolvida com Flask para realizar o cadastro e busca de usuários em uma base de dados.

## Requisitos
  - Python 3.x
  - Flask

## Desenvolvimento
  - A API foi desenvolvida com Flask e utiliza uma lista simples como base de dados para armazenar os usuários cadastrados. O cadastro é realizado através da rota /usuarios e a busca através da rota /usuarios/<cpf>.

## Como utilizar
  - Para utilizar a API, basta executar o arquivo app.py e acessar as rotas:

  - /usuarios (método POST): realiza o cadastro de um novo usuário com os dados informados. É necessário enviar um objeto JSON no corpo da requisição com os campos "cpf", "nome" e "data_nascimento".
  - /usuarios/<cpf> (método GET): busca um usuário na base de dados pelo CPF informado e retorna seus dados em formato JSON.

