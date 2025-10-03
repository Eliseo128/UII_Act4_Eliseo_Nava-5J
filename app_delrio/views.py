from django.shortcuts import render

# Create your views here.
def index(request):
        empleados = [
        {'nombre': 'Alice', 'edad': 30, 'puesto': 'Desarrolladora'},
        {'nombre': 'Bob', 'edad': 24, 'puesto': 'Diseñador'},
        {'nombre': 'Charlie', 'edad': 35, 'puesto': 'Gerente de Proyecto'},
    ]
        return render(request, 'index.html', {'empleados': empleados})