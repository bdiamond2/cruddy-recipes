from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('recipe_list/', views.recipe_list, name='recipe_list')
]
