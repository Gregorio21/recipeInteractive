from django.db import models
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.

#This is the model for the basic info of a recipe and is a foreign key to the Ingredients and Steps
#as well as identifying which user own the recipe
class Recipe(models.Model):
    Title = models.CharField(max_length=255)
    Description = models.TextField(default="")
    Privacy = models.BooleanField()
    UserId = models.ForeignKey(User,on_delete=models.CASCADE)

#Model to store the ingredinets of a recipe, foreign key to Recipe model
class Ingredient(models.Model):
    IngredientName = models.CharField(max_length=50)
    RecipeId = models.ForeignKey(Recipe,on_delete=models.CASCADE)
    #add list of units for choices in Unit
    Unit = models.CharField(max_length=20)
    Quantity = models.IntegerField()
    IngredientOrder = models.IntegerField()

#Model to store the steps of a recipe, foreign key to Recipe model
class Step(models.Model):
    StepOrder = models.IntegerField()
    Step = models.TextField()
    RecipeId = models.ForeignKey(Recipe, on_delete=models.CASCADE)

#modelform for the recipe model
class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['Title','Description','Privacy']
        widgets = {
            'Description': forms.Textarea(attrs={'rows': 2, 'cols': 30}),
        }

#modelform for the Ingredinets model
class IngredientForm(ModelForm):
    #Delete = forms.BooleanField(initial=False)
    class Meta:
        model = Ingredient
        fields = ['IngredientName','Quantity','Unit','id']

#modelform for the Steps model
class StepForm(ModelForm):
    #Delete = forms.BooleanField(initial=False)
    class Meta:
        model = Step
        fields = ['Step','id']
        widgets = {
            'Step': forms.Textarea(attrs={'rows': 2, 'cols': 30}),
        }