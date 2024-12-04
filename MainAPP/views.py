from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore



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

    author = {'name': 'Тимофей', 'surname': 'Пармон'}
    pro = {'name': 'Привет'}
    context = {'aut': author, 'pro': pro}

    return render(request, 'drive.html', context)


def about(request):

    slovar = {'name': 'Тимофей', 'surname': 'Пармон', 'legacy': 'Сергеевич'}
    return render(request, 'about.html', slovar)


def item(request, val_id):
    sylka = {}
    for val in items:
        if val["id"] == val_id:
            sylka.setdefault('code', [val['id'], val['name'], val['links']])
            context = {'sylka': sylka}
            return render(request, 'item.html', context)
        elif val["id"] == val_id:
            context = {'sylka': False}
            return render(request, 'item.html', context)
    # else: return HttpResponse(f'товар с id: {val_id} не существует')


def all_items(request):
    slovar ={'product': items}
    return render(request, 'all_items.html', slovar)




