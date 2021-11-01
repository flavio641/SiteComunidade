from flask import render_template, redirect, url_for, flash, request
from comunidadeimpressionadora import app, database
from comunidadeimpressionadora.forms import FormLogin, FormCriarConta
from comunidadeimpressionadora.models import Usuario


lista_usuarios = ['lira', 'joao', 'alon', 'alessandra', 'Amanda']


@app.route('/')
def teste():
    return render_template('teste.html')


@app.route('/contato')
def contato():
    return render_template('contato.html', )


@app.route('/usuario')
def usuarios():
    return render_template('usuario.html', lista_usuarios=lista_usuarios)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()

    if form_login.validate_on_submit() and 'botao_submit_Login' in request.form:
        flash(f'Login Feito com Sucesso no E-mail: {form_login.email.data}', 'alert-success')
        return redirect(url_for('teste'))

    if form_criarconta.validate_on_submit() and 'botao_submit_Criar_Conta' in request.form:
        usuario = Usuario(username=form_criarconta.username.data, email=form_criarconta.email.data, senha=form_criarconta.senha.data)
        database.session.add(usuario)
        database.session.commit()
        flash(f'Conta Criada para 0 E-mail: {form_criarconta.email.data}', 'alert-success')
        return redirect(url_for('teste'))

    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)