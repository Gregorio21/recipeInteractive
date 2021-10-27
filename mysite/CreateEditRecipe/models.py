from django.db import models
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
    Title = models.CharField(max_length=255)
    Description = models.TextField(default="")
    Privacy = models.BooleanField()
    UserId = models.ForeignKey(User,on_delete=models.CASCADE)

class Ingredient(models.Model):
    IngredientName = models.CharField(max_length=50)
    RecipeId = models.ForeignKey(Recipe,on_delete=models.CASCADE)
    #add list of units for choices in Unit
    Unit = models.CharField(max_length=20)
    Quantity = models.IntegerField()
    IngredientOrder = models.IntegerField()

class Step(models.Model):
    StepOrder = models.IntegerField()
    Step = models.TextField()
    RecipeId = models.ForeignKey(Recipe, on_delete=models.CASCADE)

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['Title','Description','Privacy']
        widgets = {
            'Description': forms.Textarea(attrs={'rows': 2, 'cols': 30}),
        }

class IngredientForm(ModelForm):
    #Delete = forms.BooleanField(initial=False)
    class Meta:
        model = Ingredient
        fields = ['IngredientName','Quantity','Unit','id']

class StepForm(ModelForm):
    #Delete = forms.BooleanField(initial=False)
    class Meta:
        model = Step
        fields = ['Step','id']
        widgets = {
            'Step': forms.Textarea(attrs={'rows': 2, 'cols': 30}),
        }