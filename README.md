# 🚀 Sistema de Gestão de Clientes com Flask

Este projeto é uma aplicação web simples, construída com Python e Flask, que implementa um CRUD (Create, Read, Update, Delete) completo para o gerenciamento de clientes.

Foi desenvolvido como um exercício prático para solidificar conceitos fundamentais do Flask, incluindo roteamento, Blueprints, templates com Jinja2, manipulação de formulários (`GET`/`POST`) e arquitetura de aplicação.

## ✨ Funcionalidades

* [x] **Listar** todos os clientes cadastrados.
* [x] **Adicionar** um novo cliente através de um formulário.
* [x] **Editar** as informações de um cliente existente.
* [x] **Excluir** um cliente da lista.
* [x] **Estrutura Organizada** usando Blueprints do Flask.

## 🛠️ Tecnologias Utilizadas

* **[Python](https://www.python.org/)** - Linguagem de programação principal.
* **[Flask](https://flask.palletsprojects.com/)** - Micro-framework web para o backend.
* **[Jinja2](https://jinja.palletsprojects.com/)** - Motor de templates para renderizar o HTML.
* **[HTML5](https://developer.mozilla.org/pt-BR/docs/Web/HTML)** - Estruturação das páginas.
* **[Bootstrap](https://getbootstrap.com/)** - Framework CSS para estilização rápida (botões, formulários, etc.).

## 📁 Estrutura das Rotas (Endpoints)

O projeto utiliza um Blueprint (`cliente`) para organizar as rotas:

| Método | Rota | Função | Descrição |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | `lista_clientes` | Exibe a lista de todos os clientes. |
| `POST` | `/` | `inserir_cliente` | Recebe os dados do formulário de novo cliente e o cadastra. |
| `GET` | `/new` | `cadastrar_cliente` | Exibe o formulário para criar um novo cliente. |
| `GET` | `/<id>` | `obter_cliente` | Exibe a página de detalhes de um cliente (template `detalhe_cliente.html`). |
| `GET` | `/<id>/edit` | `atualizar_cliente` | Exibe o formulário para editar um cliente existente, com os campos pré-preenchidos. |
| `POST` | `/<id>/update` | `inserir_atualizacao_cliente` | Recebe os dados do formulário de edição e atualiza o cliente. |
| `POST` | `/<id>/delete` | `deletar_cliente` | Remove o cliente da lista. |
