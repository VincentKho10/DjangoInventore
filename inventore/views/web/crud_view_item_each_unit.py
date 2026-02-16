from django.urls import reverse_lazy
from django.views import generic

from inventore.services.crud_services.service_crud_item_each_unit import serviceCreateItemEachUnit
from inventore.models import Item, ItemEachUnit
from inventore.serializers import ItemSerializer

class ItemEachUnitView(generic.ListView):
    template_name = "inventore/index.html"
    context_object_name = "item_each_units"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["create_path"] = "inventore:item-each-unit-create"
        context["update_path"] = "inventore:item-each-unit-update"
        context["delete_path"] = "inventore:item-each-unit-delete"

        context['t_content'] = "inventore/model_content/tcontent_item_each_unit.html"

        return context

    def get_queryset(self):
        return ItemEachUnit.objects.all()

class ItemEachUnitCreateView(generic.CreateView):
    model = ItemEachUnit
    fields = ['quantity', 'unit', 'unit_price', 'tax', 'item']
    template_name = "inventore/utils/detail.html"
    success_url = reverse_lazy('inventore:item-each-unit')

    def form_valid(self, form):
        post = form.data.tax
        print(post)
        # serviceCreateItemEachUnit(post)
        return super().form_valid(form)

class ItemEachUnitDetailView(generic.UpdateView):
    model = ItemEachUnit
    fields = ['quantity', 'unit', 'unit_price', 'tax', 'item']
    template_name = "inventore/utils/detail.html"
    success_url = reverse_lazy('inventore:item-each-unit')

class ItemEachUnitDeleteView(generic.DeleteView):
    model = ItemEachUnit
    template_name = "inventore/utils/delete.html"
    success_url = reverse_lazy('inventore:item-each-unit')