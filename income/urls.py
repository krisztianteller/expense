from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index, name="income"),
    path('add_income', views.add_income, name="add-income"),
    path('edit_income/<int:id>', views.income_edit, name="edit_income"),
    path('income-delete/<int:id>', views.delete_income, name="delete_income"),
    path('search-income', csrf_exempt(views.search_income), name="search_income")
]