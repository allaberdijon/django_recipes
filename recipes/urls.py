from django.urls import path
from recipes.views import RecipeListView, RecipeCrteateView, RecipeDetailView
from django.contrib.auth.decorators import login_required
urlpatterns = [
    #Главная страница и список рецептов
    path('', RecipeListView.as_view(), name='home'),
    path('recipe/<int:pk>/',RecipeDetailView.as_view(),name='recipe_detail'),
    path('recipe/add/',login_required(RecipeCrteateView.as_view()),name='recipe_add'),
    # добавление нового рецепта
]