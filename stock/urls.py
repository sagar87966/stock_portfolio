from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="index"),
    path('about/', views.about, name="about"),
    path('add_stock/', views.add_stock, name="add_stock"),
    path('delete/<ticker_id>', views.delete, name="delete"),
]