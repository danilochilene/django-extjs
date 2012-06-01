# Create your views here.
from django.shortcuts import render_to_response
from .models import Usuarios

def index(request):
	return render_to_response('hello_extjs/index.html')