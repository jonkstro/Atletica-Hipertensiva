from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import constants

from plataforma.models import Carteira

from datetime import datetime

from django.http import HttpResponse
from django.views.generic import View
from .utils import render_to_pdf

hoje = datetime.now().date()

# Página inicial do sistema, onde irá listas as opções que podem ser escolhidas pelo usuário
@login_required(login_url='/auth/')
def plataforma(request):
    return render(request, 'plataforma.html')

# Listar os associados cadastrados no sistema
@login_required(login_url='/auth/')
def dados_associados_listar(request):
    if request.method == "GET":
        carteiras = Carteira.objects.all()
        return render(request, 'dados_associados_listar.html', {'carteiras': carteiras, 'hoje':hoje})
    elif request.method == "POST":
        filtro = request.POST.get('filtro')
        carteiras = Carteira.objects.filter(nome__contains = filtro)
        return render(request, 'dados_associados_listar.html', {'carteiras': carteiras, 'hoje':hoje})

# Realizar o cadastro dos associados no sistema
@login_required(login_url='/auth/')
def add_associado(request):
    if request.method == "GET":
        return render(request, 'add_associado.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        matricula = request.POST.get('matricula')
        associacao = request.POST.get('associacao')
        foto = request.FILES.get('foto')
        data_nasc = request.POST.get('data-nasc')
        data_exped = request.POST.get('data-exped')
        data_valid = request.POST.get('data-valid')

        if (len(nome.strip()) == 0) or (len(email.strip()) == 0) or (len(cpf.strip()) == 0) or (len(matricula.strip()) == 0) or (len(associacao.strip()) == 0) or (len(data_nasc.strip()) == 0) or (len(data_exped.strip()) == 0) or (len(data_valid.strip()) == 0):
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/add-associado/')
        associado = Carteira.objects.filter(matricula=matricula)
        if associado.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um associado com essa Matrícula cadastrado')
            return redirect('/add-associado/')

        try:
            c1 = Carteira(
            nome = nome,
            email = email,
            cpf = cpf,
            matricula = matricula,
            associacao = associacao,
            foto = foto,
            data_nasc = data_nasc,
            data_exped = data_exped,
            data_valid = data_valid
            )
            c1.save()
            messages.add_message(request, constants.SUCCESS, 'Associado cadastrado com sucesso')
            return redirect('/add-associado/')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/add-associado/')





# Listar carteirinha
@login_required(login_url='/auth/')
def carteirinha (request, matricula):
    carteirinha = get_object_or_404(Carteira, matricula = matricula)
    if request.method == "GET":
        return render(request, 'carteirinha.html', {'carteirinha':carteirinha})

# Buscar carteirinhas por Matrícula
def buscar_carteirinha (request):
    if request.method == "GET":
        return render(request, 'buscar_carteirinha.html')
    elif request.method == "POST":
        # try:
            matricula = request.POST.get('matricula')
            carteirinha = get_object_or_404(Carteira, matricula = matricula)
            # pdf = render_to_pdf('pdf_carteirinha.html', {'carteirinha':carteirinha})
            # return HttpResponse(pdf, content_type='application/pdf')
            return render(request, 'pdf_carteirinha.html', {'carteirinha':carteirinha, 'hoje':hoje})
        # except:
        #     messages.add_message(request, constants.ERROR, 'Matrícula não localizada no sistema')
        #     return redirect('/buscar-carteirinha/')

def pdf_carteirinha (request, matricula):
    if request.method == "GET":
        # try:
            carteirinha = get_object_or_404(Carteira, matricula = matricula)
            return render (request, 'pdf_carteirinha.html', {'carteirinha':carteirinha, 'hoje':hoje})
        # except:
        #     messages.add_message(request, constants.ERROR, 'Matrícula não localizada no sistema')
        #     return redirect('/buscar-carteirinha/')




def gerar_relatorios (request):
    if request.method == "GET":
        return render(request, 'relatorios.html')
