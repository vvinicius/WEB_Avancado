
from django.shortcuts import render
from app_cad_aluno.models import Aluno


# Create your views here.

def index(request):
    alunos = Aluno.objects.all()
    testChave = {
        'curso': 'Desenvolvimento Web Avançado',
        'alunos': alunos
    }
    return render(request,'index.html', testChave)

def aluno(request, id):
    aluno = Aluno.objects.get(id=id)
    context = {

        'aluno': aluno

    }
    return render(request, 'aluno.html', context)

