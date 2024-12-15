from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore
from .models import Item, Color
# добавляем обработку исключений
from django.core.exceptions import ObjectDoesNotExist



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
    
    try: 
        tovar = Item.objects.get(id=value)
        
    except ObjectDoesNotExist: return HttpResponse(f'<ul><h4>товара под номером {value} не существует</h4></ul>')
    else:
        tov = {'tov': tovar, 'col': tovar.colors.all()}
        return render(request, 'second_product.html', tov)
    

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




