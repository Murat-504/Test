from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
    # Верстка портфолио
    # path('', views.index, name='home'),
    # path('about', views.about, name='about'),
    # path('contact', views.contact, name='contact'),

    # Попытка создать интернет магазин
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name="product_list_by_category"),
    path('<int:id>/<slug:slug>', views.product_detail, name='product_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
