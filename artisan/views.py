import json
import traceback
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from artisan.models import *


def index(request):
    if request.method == 'GET':
        template = 'index.html'
        context = locals()
        return render(request,template,context)