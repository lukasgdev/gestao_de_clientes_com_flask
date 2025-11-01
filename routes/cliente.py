from flask import Blueprint, render_template, request, redirect, url_for
from database.clientes import CLIENTES

cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/')
# listar todos os clientes
def lista_clientes():
    return render_template('lista_clientes.html', clientes=CLIENTES)

@cliente_route.route('/', methods=['POST'])
# inserir cliente no servidor
def inserir_cliente():
    dados_do_form = request.form
    
    nome_recebido = dados_do_form.get('nome')
    email_recebido = dados_do_form.get('email')
    
    id_atual = len(CLIENTES)
    CLIENTES.append({'id': id_atual + 1,'nome': nome_recebido, 'email': email_recebido})
    
    return redirect(url_for('cliente.lista_clientes'))

@cliente_route.route('/new')
# formulario para cadastrar um cliente
def cadastrar_cliente():
    return render_template('form_cliente.html')

@cliente_route.route('/<int:cliente_id>')
# obtem informações de um cliente especifico
def obter_cliente(cliente_id):
    return render_template('detalhe_cliente.html')

@cliente_route.route('/<int:cliente_id>/edit')
# formulario para editar um cliente
def atualizar_cliente(cliente_id):
    for cliente in CLIENTES:
        if cliente['id'] == cliente_id:
            cliente_para_atualizar = cliente
    return render_template('form_edit_cliente.html', cliente=cliente_para_atualizar)

@cliente_route.route('/<int:cliente_id>/update', methods=['POST'])
# atualizar informações do cliente
def inserir_atualizacao_cliente(cliente_id):
    
    for cliente in CLIENTES:
        if cliente['id'] == cliente_id:
            cliente_para_atualizar = cliente

    dados_do_form = request.form
    cliente_para_atualizar['nome'] = dados_do_form.get('nome')
    cliente_para_atualizar['email'] = dados_do_form.get('email')

    return redirect(url_for('cliente.lista_clientes'))

@cliente_route.route('/<int:cliente_id>/delete', methods=['POST'])
# deletar um cliente
def deletar_cliente(cliente_id):
    global CLIENTES
    CLIENTES = [cliente for cliente in CLIENTES if cliente['id'] != cliente_id]
    return redirect(url_for('cliente.lista_clientes'))

