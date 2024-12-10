
from django.urls import path # type: ignore
from . import views



urlpatterns = [
    path('', views.drive),
    path('about/', views.about),
    path('item/<int:val_id>/', views.item),
    path('items/', views.all_items),
    path('products/', views.products, name='next_page'),
    path('products/<int:value>', views.second_product, name='page'),
    
]


