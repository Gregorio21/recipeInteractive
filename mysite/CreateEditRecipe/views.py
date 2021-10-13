from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import RecipeForm,IngredientForm,StepForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms import formset_factory

def loginView(request):
    context = {}
    if request.POST:
        user = authenticate(username=request.POST['username'],password=request.POST['password'])
        login(request,user)
        return redirect('createRecipe')
    return render(request,'login.html',context)

def createAccount(request):
    context={}
    if request.POST:
        #create account
        User.objects.create_user(request.POST['username'],request.POST['email'],request.POST['password'])
    return render(request,'createAccount.html',context)

def createRecipe(request):
    context={}
    form = RecipeForm(request.POST or None)
    num = 1
    """if request.POST:
        num = request.POST['count'] + 1"""
    IngredientFormSet = formset_factory(IngredientForm,extra=num)
    StepFormSet = formset_factory(StepForm)
    context['form']= form
    context['Ingredients'] = IngredientFormSet
    context['Steps'] = StepFormSet
    #need instance of user
    """if form.is_valid():
        form = form.save(commit=False)
        form.UserId = 1
        form = form.save()
        id = form.pk
        context['id'] = id"""
    return render(request,'createRecipe.html',context)
