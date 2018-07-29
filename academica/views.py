from django.shortcuts import render


def alumno(request):
    return render(request, 'academica/alumno.html', {})
