from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404

# Create your views here.
import logging
from django.conf import settings
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import RecipeForm,IngredientForm,StepForm,Recipe,Ingredient,Step
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.forms import formset_factory, inlineformset_factory, modelformset_factory
from django.contrib.auth.decorators import login_required
fmt = getattr(settings, 'LOG_FORMAT', None)
lvl = getattr(settings, 'LOG_LEVEL', logging.DEBUG)

logging.basicConfig(format=fmt, level=lvl)


def loginView(request):
    context = {}
    if request.POST:
        user = authenticate(username=request.POST['username'],password=request.POST['password'])
        login(request,user)
        return redirect('CreateRecipe')
    return render(request,'login.html',context)

def createAccount(request):
    context={}
    if request.POST:
        #create account
        User.objects.create_user(request.POST['username'],request.POST['email'],request.POST['password'])
    return render(request,'createAccount.html',context)

def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def createRecipe(request):
    context={}
    form = RecipeForm(request.POST or None)
    IngredientFormSet = formset_factory(IngredientForm,can_delete=True,extra=0)
    IngredientFormSet = IngredientFormSet(request.POST or None,prefix='Ingredient')
    StepFormSet = formset_factory(StepForm,can_delete=True,extra=0)
    StepFormSet = StepFormSet(request.POST or None,prefix='Step')
    context['form']= form
    context['Ingredients'] = IngredientFormSet
    context['Steps'] = StepFormSet
    if request.method == "POST":
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.UserId = request.user
            form2.save()
        count = 1
        for item in IngredientFormSet:
            if item.is_valid():
                #logging.debug(item.cleaned_data['Delete'])
                if item.cleaned_data['DELETE'] == True:
                    item = item.save(commit=False)
                    if item.id: item.delete()
                else:
                    item = item.save(commit=False)
                    item.RecipeId = form2
                    item.IngredientOrder = count
                    count += 1
                    item.save()
        count = 1
        for item in StepFormSet:
            if item.is_valid():
                if item.cleaned_data['DELETE'] == True:
                    item = item.save(commit=False)
                    if item.id: item.delete()
                else:
                    item = item.save(commit=False)
                    item.RecipeId = form2
                    item.StepOrder = count
                    count += 1
                    item.save()
        return HttpResponseRedirect("/editRecipe/%d"%form2.pk)

    return render(request,'createRecipe.html',context)

@login_required
def editRecipe(request,id=None):
    context={}
    obj = get_object_or_404(Recipe,id=id,UserId=request.user)
    form = RecipeForm(request.POST or None,instance=obj)
    IngredientFormSetFactory = modelformset_factory(Ingredient,form=IngredientForm,extra=0,can_delete=True)
    StepFormSetFactory = modelformset_factory(Step,form=StepForm,extra=0,can_delete=True)
    if request.method == "POST":
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.UserId = request.user
            form2.save()
        count = 1
        IngredientFormSet2 = IngredientFormSetFactory(request.POST or None, request.FILES or None, prefix="Ingredient")
        StepFormSet2 = StepFormSetFactory(request.POST or None, request.FILES or None,prefix="Step")
        for item in IngredientFormSet2:
            if item.is_valid():
                if item.cleaned_data['DELETE'] == True:
                    item = item.save(commit=False)
                    if item.id: item.delete()
                else:
                    item = item.save(commit=False)
                    item.RecipeId = form2
                    item.IngredientOrder = count
                    count += 1
                    item.save()
        count = 1
        for item in StepFormSet2:
            if item.is_valid():
                if item.cleaned_data['DELETE'] == True:
                    item = item.save(commit=False)
                    if item.id: item.delete()
                else:
                    item = item.save(commit=False)
                    item.RecipeId = form2
                    item.StepOrder = count
                    count += 1
                    item.save()
        #return HttpResponseRedirect("/editRecipe/%d"%form.pk)
    Ingredients = Ingredient.objects.filter(RecipeId=obj)
    Steps = Step.objects.filter(RecipeId=obj)
    IngredientFormSet = IngredientFormSetFactory(prefix="Ingredient", queryset=Ingredients)
    StepFormSet = StepFormSetFactory(prefix="Step", queryset=Steps)
    context['form'] = form
    context['Ingredients'] = IngredientFormSet
    context['Steps'] = StepFormSet
    return render(request,'createRecipe.html',context)

@login_required
def search(request):
    context = {}
    result = Recipe.objects.filter(Title__icontains=request.GET["search"])
    #result = Recipe.objects.all()
    context["results"] = result
    return render(request,'search.html',context)

@login_required
def viewRecipe(request,id=None):
    context = {}
    currRecipe = Recipe.objects.filter(id=id)
    Ingredients = Ingredient.objects.filter(RecipeId=currRecipe[0])
    Steps = Step.objects.filter(RecipeId=currRecipe[0])
    context["recipe"] = currRecipe
    context["ingredients"] = Ingredients
    context["steps"] = Steps
    return render(request,'viewRecipe.html',context)


