from flask import Flask, render_template, url_for
from forms import FormLogin, FormCriarConta

app = Flask(__name__, template_folder='templates')

lista_usuarios = ['lira', 'joao', 'alon', 'alessandra', 'Amanda']

app.config['SECRET_KEY'] = '11f3ebe859a026ed558e54cb1a3cf33f'



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
    form_criarconta= FormCriarConta()
    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)


if __name__ == '__main__':
    app.run(debug=True)
