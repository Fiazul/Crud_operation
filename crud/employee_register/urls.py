from django.urls import path,include
from . import views
from .views import search_employees

urlpatterns = [
    path('', views.form,name='employee_insert'), 
    path('<int:id>/', views.form,name='employee_update'), 
    path('delete/<int:id>/',views.delete,name='employee_delete'),
    path('list/',views.list,name='employee_list') ,
    path('search/', search_employees, name='search_employees')
]