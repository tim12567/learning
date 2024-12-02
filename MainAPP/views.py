from django.shortcuts import render
from django.http import HttpResponse

# def drive(request):
#     text = '''<h1>"Изучаем django"</h1>
# <strong>Автор</strong>: <i>Пармон Т.С.</i><br>
# <i>Имя: <strong>Тимофей</strong></i><br>
# <i>Отчество: <strong>Сергеевич</strong></i><br>
# <i>Фамилия: <strong>Пармон</strong></i><br>
# <i>email: <strong>mysite@.com</strong></i>'''
   
#     return HttpResponse(text)

def about(request):
    text = '''
<i>Имя: <strong>Тимофей</strong></i><br>
<i>Отчество: <strong>Сергеевич</strong></i><br>
<i>Фамилия: <strong>Пармон</strong></i><br>
<i>email: <strong>mysite@.com</strong></i>'''
   
    return HttpResponse(text)

# def product(request):
#     items = [
#    {"id": 1, "name": "Кроссовки abibas"},
#    {"id": 2, "name": "Куртка кожаная"},
#    {"id": 3, "name": "Coca-cola 1 литр"},
#    {"id": 4, "name": "Картофель фри"},
#    {"id": 5, "name": "Кепка"},
# ]

#     return HttpResponse(items[1]['name'])
