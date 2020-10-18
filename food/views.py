from django.shortcuts import render
from django.views.generic.edit import FormView, CreateView
from .forms import Food, Ingredient

# Create your views here.

class RegisterFood(FormView, CreateView):
    template_name = 'form.html'
    form_class = Food
    success_url = '/'

    def get_context_data(self, **kwargs):
        """Use this to add extra context."""
        context = super(RegisterFood, self).get_context_data(**kwargs)
        model = self.form_class.Meta.model
        all_orders = [{
                'name': instance.name,
                'ingredientes': list(instance.ingredients.all().values_list('name', flat=True))
            } for instance in model.objects.all()]
        context['item_list'] = all_orders
        context['item_head'] = 'Comida', 'Ingredientes'
        context['food'] = True
        return context
    
registrar_comida = RegisterFood.as_view()


class RegisterIngredient(FormView, CreateView):
    template_name = 'form.html'
    form_class = Ingredient
    success_url = '/'
    
    def get_context_data(self, **kwargs):
        """Use this to add extra context."""
        context = super(RegisterIngredient, self).get_context_data(**kwargs)
        model = self.form_class.Meta.model
        context['ingredient'] = True
        return context

registrar_ingrediente = RegisterIngredient.as_view()
