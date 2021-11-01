from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, length, email, equal_to


class FormCriarConta(FlaskForm):
    username = StringField('Nome do usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), email()])
    senha = PasswordField('Senha', validators=[DataRequired(), length(6, 20)])
    confirmacao_senha = PasswordField('Confirmação da Senha', validators=[DataRequired(), equal_to(senha)])
    botao_submit_Criar_Conta = SubmitField('Criar Conta', validators=[])


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), email()])
    senha = PasswordField('Senha', validators=[DataRequired(), length(6, 20)])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_submit_Login = SubmitField('Fazer Login')










