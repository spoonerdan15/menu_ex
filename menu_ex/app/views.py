from django.shortcuts import render

# Create your views here.


def base(request, name):
    return render(request, 'app/list.html', {'name': name})
