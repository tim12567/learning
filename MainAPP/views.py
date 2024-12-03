from django.shortcuts import render
from django.http import HttpResponse



autor = {'Имя': 'Тимофей', 'Отчество': 'Сергеевич', 'Фамилия': 'Пармон', 
'email': 'mysite@.com'}

items = [
   {"id": 1, "name": "Кроссовки abibas", "links": "http://127.0.0.1:8000/item/1/"},
   {"id": 2, "name": "Куртка кожаная", "links": "http://127.0.0.1:8000/item/2/"},
   {"id": 3, "name": "Coca-cola 1 литр", "links": "http://127.0.0.1:8000/item/3/"},
   {"id": 4, "name": "Картофель фри", "links": "http://127.0.0.1:8000/item/4/"},
   {"id": 5, "name": "Кепка", "links": "http://127.0.0.1:8000/item/5/"},
]

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


def item(request, val_id):
    for val in items:
        if val['id'] == val_id: return HttpResponse(f"<h3><i>{val['name']}</i></h3> <i><a href='http://127.0.0.1:8000/items/'> возврат в каталог</a></i>")
    return HttpResponse(f'<i>товара с id: {val_id} не существует</i>')

def all_items(request):
    
    # spisok = [f"<p>{i['id']}:</p> <h4><i>{i['name']}</i></h4> <p><a href={i['links']} target='_blank'> ссылка на товар</a></p>" for i in items]
    spisok = []
    
    for k in items:
        num = 0
        for i, j in k.items():
            if num < 2:
                num += 1
                spisok.append(f"<pre><big>{i}: <i><strong>{j}</strong></i></big></pre>")
            elif num >1: spisok.append(f"<pre><big><strong>{i}</strong>: <i><a href={j}> ссылка на товар</a></i></big></pre><br>")

    return HttpResponse(f'{i}' for i in spisok)
        

