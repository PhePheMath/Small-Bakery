from django.shortcuts import render
from django.views.generic.edit import FormView, CreateView
from .forms import Order

# Create your views here.

class NewOrder(FormView, CreateView):
    template_name = 'form.html'
    form_class = Order
    success_url = '/'

    def get_context_data(self, **kwargs):
        """Use this to add extra context."""
        context = super(NewOrder, self).get_context_data(**kwargs)
        model = self.form_class.Meta.model
        all_orders = [{'customer': order.customer,
                       'address': order.address,
                       'value': order.value,
                       'product': order.product} for order in model.objects.all()]
        context['item_list'] = all_orders
        context['item_head'] = 'Cliente', 'Endereço', 'Valor', 'Produto'
        context['delivery'] = True
        return context

novo_pedido = NewOrder.as_view()
