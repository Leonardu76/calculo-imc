from django.shortcuts import render
from .forms import Info

# Create your views here.

def home(request):
    imc = None

    if request.method == 'POST':

        # cria um formulario NameForm com os campos que foram digitados
        form = Info(request.POST)
        # checa se é um formulário válido:
        
        if form.is_valid():
            # pega o número digitado
            altura = form.cleaned_data['altura']
            peso = form.cleaned_data['peso']
            alt2 = altura * altura 
            cal =  peso / alt2 
            imc =  round(cal, 2)


    else:
        form = Info(request.POST)


    return render (request, 'tabela/index.html', {'form': form, 'imc':imc })
