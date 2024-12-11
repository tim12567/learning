from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore
from .models import Item



autor = {'Имя': 'Тимофей', 'Отчество': 'Сергеевич', 'Фамилия': 'Пармон', 
'email': 'mysite@.com'}

items = [
   {"id": 1, "name": "Кроссовки abibas", "links": "http://127.0.0.1:8000/item/1/"},
   {"id": 2, "name": "Куртка кожаная", "links": "http://127.0.0.1:8000/item/2/"},
   {"id": 3, "name": "Coca-cola 1 литр", "links": "http://127.0.0.1:8000/item/3/"},
   {"id": 4, "name": "Картофель фри", "links": "http://127.0.0.1:8000/item/4/"},
   {"id": 5, "name": "Кепка", "links": "http://127.0.0.1:8000/item/5/"},
]


def second_product(request, value):
    tovar = Item.objects.all()
    
    for val in tovar:
        # val это экземпляр объекта поэтому к нему обращаться надо через точку
        if val.id == value:
            tov = {'tov': val}
            return render(request, 'second_product.html', tov)
    return HttpResponse(f'<ul><h4>товара под номером {value} не существует</h4></ul>')
   

def products(request):
    all_product = Item.objects.all()
    pro = {'ali': all_product}
    return render(request, 'products.html', pro)


def drive(request):
    author = {'name': 'Тимофей', 'surname': 'Пармон'}
    context = {'aut': author}

    return render(request, 'drive.html', context)


def about(request):
    return render(request, 'about.html', autor)


def item(request, val_id):
    sylka = {}
    for val in items:
        if val["id"] == val_id:
            sylka.setdefault('code', [val['id'], val['name'], val['links']])
            context = {'sylka': sylka}
            return render(request, 'item.html', context)
      
    else: return HttpResponse(f'товар с id: {val_id} не существует')


def all_items(request):
    slovar ={'product': items}
    return render(request, 'all_items.html', slovar)




