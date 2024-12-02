from django.shortcuts import render
from django.http import HttpResponse


autor = {'Имя': 'Тимофей', 'Отчество': 'Сергеевич', 'Фамилия': 'Пармон', 
'email': 'mysite@.com'}

def drive(request):
    text = '''<h1>"Изучаем django"</h1>
<strong>Автор</strong>: <i>Пармон Т.С.</i><br>'''
   
    return HttpResponse(text)


def about(request):
    test = f'''Имя: <strong>{autor['Имя']}</strong><br>
    Отчество: <strong>{autor["Отчество"]}</strong><br>
    Фамилия: <strong>{autor["Фамилия"]}</strong><br>
    email: <strong>{autor["email"]}</strong><br>'''
    
    return HttpResponse(test)


   
 

# def product(request):
#     items = [
#    {"id": 1, "name": "Кроссовки abibas"},
#    {"id": 2, "name": "Куртка кожаная"},
#    {"id": 3, "name": "Coca-cola 1 литр"},
#    {"id": 4, "name": "Картофель фри"},
#    {"id": 5, "name": "Кепка"},
# ]

#     return HttpResponse(items[1]['name'])
