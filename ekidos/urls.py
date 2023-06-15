
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from food.views import *
from users.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('', index, name= 'index'),
    path('', include('users.urls')),
    path('about/', about, name='about'),
    path('menu/', menu, name='menu'),
    path('book/', book, name='book'),
    path('food-order/<int:id>',food_order,name='food_order'),
    path('search/',search,name='search'),
    path('cardpay/',cardpay,name='cardpay'),
    path('bron/',bron,name='bron'),

    
]

from django.urls import path
from .views import recipe_list, recipe_detail

urlpatterns = [
    path('recipes/', recipe_list, name='recipe_list'),
    path('recipes/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
]

urlpatterns += static(settings.MEDIA_URL,
document_root = settings.MEDIA_ROOT)