from django.contrib.auth.models import User
from django.contrib import messages
from random import choice
from django.db import transaction
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from  django.conf import  settings
from django.core.mail import send_mail
from django.utils.html import strip_tags

def registrar(request):
    return render(request, 'seguridad/register.html')