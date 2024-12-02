# from django.contrib import admin
from django.urls import path
from MainAPP.views import drive, about


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', drive),
    path('next', about),
    
]
