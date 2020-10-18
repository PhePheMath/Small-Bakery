from django.shortcuts import render, HttpResponse
from django.utils.safestring import mark_safe
from django.views.generic.edit import FormView, CreateView
from django.template.defaultfilters import register
from .forms import Crew
# Create your views here.

class SignEmployee(FormView, CreateView):
    template_name = 'form.html'
    form_class = Crew
    success_url = '/'

    def get_context_data(self, **kwargs):
        """Use this to add extra context."""
        context = super(SignEmployee, self).get_context_data(**kwargs)
        context['crew'] = True
        return context

contratar = SignEmployee.as_view()

def home_view(request):
    return render(request, 'index.html')


@register.filter
def get_item(value, item):
    if type(value[item]) == list:
        value[item]= f"<ul>{' '.join([f'<li>{val}</li>' for val in value[item]])}</ul>"
    return mark_safe(value[item])