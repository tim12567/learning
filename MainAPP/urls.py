
from django.urls import path
from . import views



urlpatterns = [
    path('', views.drive),
    path('about/', views.about),
    path('item/<int:val_id>/', views.item),
    path('items/', views.all_items),

]


