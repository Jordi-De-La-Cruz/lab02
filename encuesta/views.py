from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'titulo': "Formulario",
    }
    return render(request, 'encuesta/formulario.html', context)

def enviar(request):
    context = {
        'titulo': "Respuesta",
        'nombre': request.POST['nombre'],
        'clave': request.POST['password'],
        'educacion': request.POST['educacion'],
        'nacionalidad': request.POST['nacionalidad'],
        'idiomas': request.POST.getlist('idiomas'),
        'correo': request.POST['email'],
        'website': request.POST['sitioweb'],
    }
    return render(request, 'encuesta/respuesta.html', context)

def calcular(request):
    return render(request, 'calculadora/formulario2.html')

def resultado(request):
    if request.method == 'POST':
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        operacion = request.POST['operacion']
        if operacion == 'suma':
            resultado = int(num1) + int(num2)
        elif operacion == 'resta':
            resultado = int(num1) - int(num2)
        else:
            resultado = int(num1) * int(num2)
        return render(request, 'calculadora/resultado.html', {'resultado': resultado})
    else:
        return render(request, 'calculadora/formulario2.html')
    
def cilindro(request):
    if request.method == 'POST':
        altura = float(request.POST['altura'])
        diametro = float(request.POST['diametro'])
        volumen = 3.1416 * (diametro/2)**2 * altura
        return render(request, 'cilindro/resultado.html', {'volumen': volumen})
    return render(request, 'cilindro/formulario3.html')
