import random
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from .utils import enviar_email, password_is_valid
from django.contrib.auth.models import User
from hashlib import sha256
from .models import Ativacao, MudarSenha
from django.contrib import messages, auth
from django.contrib.messages import constants
from django.conf import settings

##################### NÃO ESTÁ NO ESCOPO DO PROJETO CADASTRAR USUÁRIOS #####################

# def cadastro(request):
#     # return HttpResponse('Tela de cadastro')
#     # Se o metodo for GET, será redirecionado para pagina padrao, senão
#     # será renderizado o cadastro.html
#     if (request.method == 'GET'):
#         if (request.user.is_authenticated):
#             return redirect('/')
#         return render(request, 'cadastro.html')
#     # Se o método for POST, quer dizer que tá sendo feito o cadastro do
#     # novo usuário
#     elif (request.method == 'POST'):
#         nome = request.POST.get('nome')
#         sobrenome = request.POST.get('sobrenome')
#         username = request.POST.get('usuario')
#         email = request.POST.get('email')
#         senha = request.POST.get('senha')
#         confirmar_senha = request.POST.get('confirmar_senha')

#         # Se a senha não for válida, será redirecionado para o cadastro
#         # e será exibido mensagem de erro
#         if not password_is_valid(request, senha, confirmar_senha):
#             return redirect('/auth/cadastro')
        
#         email_usuario = User.objects.filter(email=email)
#         if email_usuario.exists():
#             messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse E-mail, caso seja seu, veja na sua lista de email o código de ativação')
#             return redirect('/auth/cadastro/')

#         username_usuario = User.objects.filter(username=username)
#         if username_usuario.exists():
#             messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse username, caso seja seu, veja na sua lista de email o codigo de ativação')
#             return redirect('/auth/cadastro/')
#         # Se a senha for válida, será dado continuidade para o cadastro do novo usuário
#         try:
#             user = User.objects.create_user(first_name=nome, last_name=sobrenome, username=username, email=email, password=senha, is_active=False)
#             user.save()
#             # Será criado um token de ativação do usuário, a mesma será enviada por email
#             token = sha256(f'{username}{email}'.encode()).hexdigest()
#             ativacao = Ativacao(token = token, user = user)
#             ativacao.save()

#             # Enviar email para confirmação e ativação do cliente
#             url_local = '127.0.0.1:8000'
#             url_heroku = settings.HEROKU_URL
#             link_ativacao=f"{url_heroku}/auth/ativar_conta/{token}"
#             mensagem = 'Cadastro realizado com sucesso no app Gestão de consumo!!\nClique no link ao lado para poder realizar a ativação da sua conta: {}'.format(link_ativacao)
#             enviar_email(email, mensagem)

#             messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso, enviamos um email para você realizar a ativação da sua conta!')
#             return redirect('/auth/logar')
            
#         except:
#             messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
#             return redirect('/auth/cadastro')


# def ativar_conta(request, token):
#     # Função de ativação da conta, irá receber a token via url GET e então irá autenticar
#     # o model ativacao do usuario
#     token = get_object_or_404(Ativacao, token=token)
#     if token.ativo:
#         messages.add_message(request, constants.WARNING, 'Essa token já foi usado')
#         return redirect('/auth/logar')
#     user = User.objects.get(username=token.user.username)
#     user.is_active = True
#     user.save()
#     token.ativo = True
#     token.save()
#     messages.add_message(request, constants.SUCCESS, 'Conta ativa com sucesso')
#     return redirect('/auth/logar')

##################### NÃO ESTÁ NO ESCOPO DO PROJETO CADASTRAR USUÁRIOS #####################

def logar(request):
    # return HttpResponse('Tela de logar')
    if (request.method == 'GET'):
        if (request.user.is_authenticated):
            return redirect('/')
        return render(request, 'logar.html')
    elif (request.method == 'POST'):
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')
        usuario = auth.authenticate(username = username, password = senha)
        # Caso o usuario não esteja autenticado (cadastrado e ativado)
        if not usuario:
            messages.add_message(request, constants.ERROR, 'Username ou senha inválidos')
            return redirect('/auth/')
        else:
            auth.login(request, usuario)
            return redirect('/plataforma/')

def sair(request):
    auth.logout(request)
    return redirect('/auth/')

def forgot(request):
    # return HttpResponse('TELA DE ESQUECEU SENHA')
    if (request.method == 'GET'):
        return render(request, 'forgot.html')
    # Se o método for POST, quer dizer que tá sendo feito o cadastro do
    # novo usuário
    elif (request.method == 'POST'):
        email = request.POST.get('email')
        token_senha = sha256(f'{email}{random.randrange(1000)}'.encode()).hexdigest()
        
        email_usuario = User.objects.filter(email=email)
        if not email_usuario.exists():
            messages.add_message(request, constants.ERROR, 'Não temos esse e-mail cadastrado!!')
            return redirect('/auth/forgot/')
        
        usuario = User.objects.get(email=email)
        alteracao = MudarSenha(token = token_senha, user = usuario)
        alteracao.save()

        url_local = '127.0.0.1:8000'
        # url_heroku = settings.HEROKU_URL

        link_ativacao=f"{url_local}/auth/alterar_senha/{token_senha}"
        mensagem = 'Você solicitou alteração de senha?\nClique no link ao lado para poder realizar a ativação da sua conta: {}\n Se você não solicitou, desconsidere esse e-mail.'.format(link_ativacao)
        enviar_email(email, mensagem)

        messages.add_message(request, constants.SUCCESS, 'Enviamos um email com o link de mudança de senha para você!')
        return redirect('/auth/forgot')

        # except:
        #     messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
        #     return redirect('/auth/forgot')


def alterar_senha(request, token):
    # return HttpResponse('função de alterar senha -> token: {}'.format(token))
    if (request.method == 'GET'):
        return render(request, 'alterar_senha.html', {'token' : token})
    # Se o método for POST, quer dizer que tá sendo feito o cadastro do
    # novo usuário
    elif (request.method == 'POST'):
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        # Se a senha não for válida, será redirecionado para o cadastro
        # e será exibido mensagem de erro
        if not password_is_valid(request, senha, confirmar_senha):
            return redirect(f'/auth/alterar_senha/{token}')
        token = get_object_or_404(MudarSenha, token=token)
        if token.ativo:
            messages.add_message(request, constants.WARNING, 'Esse link já foi usado, clique em "Esqueci a senha" para receber um novo link no email.')
            return redirect('/auth/')

        user = User.objects.get(username=token.user.username)
        user.set_password(senha)
        user.save()
        token.ativo = True
        token.save()
        messages.add_message(request, constants.SUCCESS, 'Senha alterada com sucesso')
        return redirect('/auth/')


