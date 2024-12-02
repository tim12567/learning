# from django.contrib import admin
from django.urls import path
from MainAPP.views import about


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', drive),
    path('', about),
    # path('', product),
   
    
]
