from flask import Flask, render_template, request

from database.mysql import get_connection
from model.produtosV2 import ProdutosModel

app = Flask(__name__)
produtosModel = ProdutosModel()

@app.route("/")
def index():
    request.get_data('')
    return render_template('index.html', numero=2)


@app.route("/home")
def home():
        return render_template('index.html', numero=1)

@app.route("/dinamica")
def dinamica():
    numero = int(request.args['numero']) 
    return render_template('index.html', numero=numero)

@app.route("/produtos")
def listar_produtos():
    produtos = produtosModel.carregar_produtos()
    print(produtos)
    return render_template('lista_produtosV2.html', produtos=produtos)

@app.route("/produtos/incluir")
def incluir_produto():
    return render_template('form_produto.html', produto=None, acao='INCLUIR')

@app.route("/produtos/editar/<id>")
def editar_produto(id):

    produto = produtosModel.carregar_produto(id)

    return render_template('form_produto.html', acao='EDITAR', produto=produto)

@app.route("/produtos/excluir/<id>")
def excluir_produto(id):
    produto = produtosModel.carregar_produto(id)
    return render_template('form_produto.html', acao='EXCLUIR', produto=produto)

@app.route("/produtos/processar", methods=['POST'])
def processar_produto():
    produto = request.form.to_dict()
    mensagem = ' '

    if (produto['ACAO'] ==  'INCLUIR'):
        produtosModel.incluir_produto(produto)
        mensagem = "Produto cadastrado com sucesso!"
    elif (produto['ACAO'] == 'EDITAR'):
        produtosModel.editar_produto(produto)
        mensagem = "Produto editado com sucesso!"
    elif (produto['ACAO'] ==  'EXCLUIR'):
        produtosModel.excluir_produto(produto)
        mensagem = "Produto excluído com sucesso!"

    produtos = produtosModel.carregar_produtos()

    return render_template('lista_produtosV2.html', produtos=produtos, mensagem=mensagem)

