from django.urls import path
from . import views

urlpatterns = [
    path('createRecipe', views.createRecipe,name="createRecipe"),
    path('createAccount',views.createAccount,name="createAccount"),
    path('',views.loginView),

]