# from django.contrib import admin
from django.urls import path
from MainAPP.views import drive, about, item, all_items


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', drive),
    path('about', about),
    path('item/<int:val_id>', item),
    path('items', all_items),
    
]
