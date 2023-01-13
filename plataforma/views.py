from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import constants


@login_required(login_url='/auth/')
def plataforma(request):
    return render(request, 'plataforma.html')













































# # from django.http import HttpResponse
# # from django.shortcuts import render, redirect, get_object_or_404
# # from django.contrib.auth.decorators import login_required
# # from django.contrib import messages
# # from django.contrib.messages import constants
# # from .models import Dispositivo


# # @login_required(login_url='/auth/logar/')
# # def plataforma(request):
# #     return render(request, 'plataforma.html')

# # @login_required(login_url='/auth/logar/')
# # def dados_consumo(request):
# #     # return HttpResponse('Tela de cadastro')
# #     # Se o metodo for GET, será redirecionado para pagina padrao, senão
# #     # será renderizado o cadastro.html
# #     if (request.method == 'GET'):
# #         # return HttpResponse('tela de dados de consumo')
# #         dispositivos = Dispositivo.objects.filter(user=request.user)
# #         return render(request, 'dados_consumo.html', {'dispositivos': dispositivos})
# #         # if (request.user.is_authenticated):
# #         #     return redirect('/')
# #         # return render(request, 'cadastro.html')

# # @login_required(login_url='/auth/logar/')
# # def dispositivos(request):
# #     if (request.method == 'GET'):
# #         # return HttpResponse('Tela de dispositivos')
# #         dispositivos = Dispositivo.objects.filter(user=request.user)
# #         return render(request, 'dispositivos.html', {'dispositivos': dispositivos})
# #     elif (request.method == 'POST'):
# #         # return HttpResponse('POST')
# #         id_esp8266 = request.POST.get('id_esp8266')
# #         email_adm = request.POST.get('email_adm')
# #         endereco = request.POST.get('endereco')
# #         senha_adm = request.POST.get('senha_adm')

# #         if (len(id_esp8266.strip()) == 0) or (len(email_adm.strip()) == 0) or (len(endereco.strip()) == 0) or (len(senha_adm.strip()) == 0):
# #             messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
# #             return redirect('/dispositivos/')

# #         # dispositivo = Dispositivo.objects.filter(id=id_esp8266)
# #         # if dispositivo.exists():
# #         #     messages.add_message(request, constants.ERROR, 'Já existe um dispositivo com esse ID / MAC')
# #         #     return redirect('/dispositivos/')
# #         try:
# #             d1 = Dispositivo(
# #                 id = id_esp8266,
# #                 email_adm = email_adm,
# #                 endereco = endereco,
# #                 senha_adm = senha_adm,
# #                 user = request.user
# #             )

# #             d1.save()
# #             messages.add_message(request, constants.SUCCESS, 'Dispositivo cadastrado com sucesso')
# #             return redirect('/dispositivos/')
# #         except:
# #             messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
# #             return redirect('/dispositivos/')

# # def pg_inicial(request):
# #     if (request.method == 'GET'):
# #         return HttpResponse('Pagina inicial do site')
# #         # if (request.user.is_authenticated):
# #         #     return redirect('/plataforma/')
# #         # else: 
# #         #     return render(request, 'pg_inicial.html')