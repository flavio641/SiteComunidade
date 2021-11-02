import flask_bcrypt
from flask import render_template, redirect, url_for, flash, request
from comunidadeimpressionadora import app, database, Bcrypt, bcrypt
from comunidadeimpressionadora.forms import FormLogin, FormCriarConta
from comunidadeimpressionadora.models import Usuario
from flask_login import login_user, logout_user,  current_user, login_required


lista_usuarios = ['lira', 'joao', 'alon', 'alessandra', 'Amanda']


@app.route('/')
def teste():
    return render_template('teste.html')


@app.route('/contato')
def contato():
    return render_template('contato.html', )


@app.route('/usuario')
@login_required
def usuarios():
    return render_template('usuario.html', lista_usuarios=lista_usuarios)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()

    if form_login.validate_on_submit() and 'botao_submit_Login' in request.form:
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario, remember=form_login.lembrar_dados.data)
            flash(f'Login Feito com Sucesso no E-mail: {form_login.email.data}', 'alert-success')
            return redirect(url_for('teste'))
        else:
            flash(f'Falha no login. E-mail ou senha incorreto ', 'alert-danger')

    if form_criarconta.validate_on_submit() and 'botao_submit_Criar_Conta' in request.form:
        flash(f'Conta Criada para o E-mail: {form_criarconta.email.data}', 'alert-success')
        senha_cript = flask_bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuario(username=form_criarconta.username.data, email=form_criarconta.email.data, senha=senha_cript)
        database.session.add(usuario)
        database.session.commit()

        return redirect(url_for('teste'))

    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)


@app.route('/sair')
@login_required
def sair():
    logout_user()
    flash(f'logout feito com sucesso ', 'alert-success')
    return redirect(url_for('teste'))


@app.route('/perfil')
@login_required
def perfil():
    return render_template('perfil.html', )


@app.route('/post/criar')
@login_required
def criar_post():
    return render_template('criarpost.html', )


