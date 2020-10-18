from django import forms
from .models import Food as FoodModel, Ingredient as IngredientModel


class Food(forms.ModelForm):

    class Meta:
        model = FoodModel
        fields = ['name', 'ingredients']


class Ingredient(forms.ModelForm):
    
    class Meta:
        model = IngredientModel
        fields = ['name', 'value_by_kilo']
