from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import registrosform
from .models import registros

# Create your views here.
@login_required()
def home(request):
    data = {
        'form': registrosform()
    }
    if request.method == 'POST':
        formulario = registrosform (data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Registro Guardado"
        else:
            data["form"] = formulario
    
    return render(request, 'app/home.html',data)

@login_required()
def listar (request):
    registrosform=registros.objects.all()
    
    data = {
        'registrosform': registrosform
    }
    
    return render(request, 'app/listar.html',data)

@login_required()
def modif (request, id):
    registro = get_object_or_404(registros, id=id)
    
    data = {
        'form': registrosform(instance=registro)
    }
    
    if request.method == 'POST':
        formulario = registrosform (data=request.POST, instance=registro)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='listar')
        
        data["form"] = formulario
        
    return render(request, 'app/modif.html',data)

@login_required()
def registro (request,id):
    registro = get_object_or_404(registros, id=id)
    contexto = {
        'registrosform': registro
        
    }
    return render(request, 'app/registro.html',contexto)