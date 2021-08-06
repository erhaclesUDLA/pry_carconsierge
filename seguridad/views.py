from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models.functions import Upper
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from psycopg2._psycopg import IntegrityError




from pry_carconsierge.funciones import addUserData



from django.db.models import FloatField

from django.db.models import Sum, Count, Max,Min,Avg


@login_required(login_url='/seguridad/login/')
def index(request):
    data = {
        'titulo': 'Empresa',
        'saludo': 'Bienvenido',
    }
   
    def current_date_format(month):
        months = (
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre",
        "Diciembre")
        month = months[month - 1]
        return month



    return render(request, 'main/index.html', data)





def login_session(request):
    data = {'titulo': 'Inicio de sesión - Dental Bonilla'}
    success_url = reverse_lazy('index')
    if request.user.is_authenticated:
         return HttpResponseRedirect(success_url)
    if request.method == 'POST':
        print(request.POST)
        user = authenticate(username=request.POST['usuario'],password=request.POST['password'])
        data['resp'] = False
        if user is not None:
            if user.is_active:
                login(request, user)
                data['resp'] = True
                data['user'] = user.username

            else:
                data['error'] = 'Usuario no esta Activo'
        else:
            data['error'] = 'El Usuario es Incorrecto'
        return JsonResponse(data)
    else:
        data['sistema'] = 'LM TECH'
        data['logo'] = "fas fa-spinner fa-spin"
        data['institucion'] = 'Francisco Chango'
        return render(request, 'seguridad/login.html', data)


def logout_user(request):
    logout(request)
    return redirect('/seguridad/login/')