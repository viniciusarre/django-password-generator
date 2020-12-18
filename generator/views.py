from django.shortcuts import render
import random
# Create your views here.


def home(request):
    return render(request, 'home.html', {'options': range(6, 15)})


def password(request):
    get = request.GET.get
    characters = list('abcdefghijklmnopqrstuvwxyz')
    special = list(
        '¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ')
    numbers = list('0123456789')
    length = int(get('length'))
    if get('uppercase'):
        characters.extend([c.capitalize() for c in characters])
    if get('special'):
        characters.extend(special)
    if get('numbers'):
        characters.extend(numbers)
    password = ''
    for _ in range(length):
        password += random.choice(characters)

    return render(request, 'password.html', {'password': password})
