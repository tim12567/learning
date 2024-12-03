from django.shortcuts import render
from django.http import HttpResponse



autor = {'Имя': 'Тимофей', 'Отчество': 'Сергеевич', 'Фамилия': 'Пармон', 
'email': 'mysite@.com'}

items = [
   {"id": 1, "name": "Кроссовки abibas", "links": "https://www.wildberries.ru/catalog/194197845/detail.aspx"},
   {"id": 2, "name": "Куртка кожаная", "links": "https://www.wildberries.ru/catalog/0/search.aspx?search=кожаные%20куртки%20мужские"},
   {"id": 3, "name": "Coca-cola 1 литр", "links": "https://www.ozon.ru/category/coca-cola-1-litr/"},
   {"id": 4, "name": "Картофель фри", "links": "https://www.ozon.ru/category/kartofel-fri/"},
   {"id": 5, "name": "Кепка", "links": "https://www.wildberries.ru/catalog/aksessuary/golovnye-ubory/tags/kepki-muzhskie"},
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
        if val['id'] == val_id: return HttpResponse(f"<h3><i>{val['name']}</i></h3> <i><a href={val['links']} target='_blank'> ссылка на товар</a></i>")
    return HttpResponse(f'<i>товара с id: {val_id} не существует</i>')

def all_items(request):
    
    # spisok = [f"<p>{i['id']}:</p> <h4><i>{i['name']}</i></h4> <p><a href={i['links']} target='_blank'> ссылка на товар</a></p>" for i in items]
    spisok = []
    
    for k in items:
        num = 0
        for i, j in k.items():
            if num < 2:
                num += 1
                spisok.append(f"<p>{i}:</p> <h4><i>{j}</i></h4>")
            elif num >1: spisok.append(f"<p>{i}:</p> <i><a href={j} target='_blank'> ссылка на товар</a></i>")

    return HttpResponse(f'{i}' for i in spisok)
        

