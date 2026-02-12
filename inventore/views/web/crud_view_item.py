from django.urls import reverse_lazy
from django.views import generic

from inventore.models import Item
from inventore.serializers import ItemSerializer

class ItemView(generic.ListView):
    template_name = "inventore/index.html"
    context_object_name = "items"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["create_path"] = "inventore:item-create"
        context["update_path"] = "inventore:item-update"
        context["delete_path"] = "inventore:item-delete"

        context['t_content'] = "inventore/model_content/tcontent_item.html"

        return context

    def get_queryset(self):
        return Item.objects.all()

class ItemCreateView(generic.CreateView):
    model = Item
    fields = ['item_code', 'item_name', 'metric_unit', 'quantity', 'grand_total']
    template_name = "inventore/utils/detail.html"
    success_url = reverse_lazy('inventore:item')

class ItemDetailView(generic.UpdateView):
    model = Item
    fields = ['item_code', 'item_name', 'metric_unit', 'quantity', 'grand_total']
    template_name = "inventore/utils/detail.html"
    success_url = reverse_lazy('inventore:item')

class ItemDeleteView(generic.DeleteView):
    model = Item
    template_name = "inventore/utils/delete.html"
    success_url = reverse_lazy('inventore:item')