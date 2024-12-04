# from django.contrib import admin
from django.urls import path, include # type: ignore
# from MainAPP import views

urlpatterns = [
    path('', include('MainAPP.urls'))

]
