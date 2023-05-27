
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from food.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name= 'index'),
    path('about/', about, name='about'),
    path('menu/', menu, name='menu'),
    path('book/', book, name='book'),
    path('register/', users, name='register')

    
]

urlpatterns += static(settings.MEDIA_URL,
document_root = settings.MEDIA_ROOT)