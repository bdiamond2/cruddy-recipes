from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('recipe_list/', views.recipe_list, name='recipe_list'),
    path('recipe_detail/<int:recipe_id>/',
         views.recipe_detail, name='recipe_detail')
]
