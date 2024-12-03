# from django.contrib import admin
from django.urls import path, include
from MainAPP import views

urlpatterns = [
    path('', include('MainAPP.urls'))

]
