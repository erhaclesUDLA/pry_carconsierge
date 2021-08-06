from django.urls import path
from seguridad.view_empresa import empresa
from seguridad.view_usuariote import usuariote
from seguridad.views import  login_session,logout_user
from seguridad.viewrecuperar import recuperar
from seguridad.viewregistrar import registrar

from seguridad.perfil import perfil
urlpatterns = [
path('login/' ,login_session ,name='login'),
path('logout/', logout_user ,name='logout'),
path('recuperar/', recuperar ,name='recuperar'),
path('registrar/', registrar ,name='registrar'),
path('perfil/', perfil ,name='perfil'),

path('empresa/', empresa ,name='empresa'),
path('usuariote/', usuariote ,name='usuariote'),
]