from django.urls import path
from . import views

urlpatterns = [
    path('createRecipe/', views.createRecipe,name="CreateRecipe"),
    path('editRecipe/<int:id>', views.editRecipe,name="EditRecipe"),
    path('createAccount/',views.createAccount,name="CreateAccount"),
    path('',views.loginView,name="login"),
    path('login',views.loginView,name="login2"),
    path('logout', views.logout_view,name="logout"),
    path('search/<str:search>', views.search,name="Search"),
    path('search/', views.search,name="Search"),
    path('viewRecipe/<int:id>',views.viewRecipe,name="ViewRecipe"),

]