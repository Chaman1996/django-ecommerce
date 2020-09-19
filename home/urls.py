from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('category/<int:id>/<slug:slug>', views.category_products, name='category_products'),

]