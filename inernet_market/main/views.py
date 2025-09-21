from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


async def index(request):
    context:dict[str,str] = {
        'title':'Home',
        'context': 'Главная страница магазина - HOME'
    }
    return render(request, 'main/index.html')

async def about(request):
    return HttpResponse('About page')