from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Tecnico
from .forms import TecnicoForm


# Create your views here.
def index(request):
  autos = Tecnico.objects.all()
  form = TecnicoForm()
  return render(request, 'index.html', {'autos' : autos, 'form' : form})

def show(request, auto_id):
  auto = Tecnico.objects.get(id=auto_id)
  return render(request, 'show.html', {'auto' : auto})

def post_auto(request):
  form = TecnicoForm(request.POST, request.FILES)
  if form.is_valid():
    form.save(commit = True)
  return HttpResponseRedirect('/')
