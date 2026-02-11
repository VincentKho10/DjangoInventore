from django.urls import reverse_lazy
from django.views import generic

from inventore.models import Unit
from inventore.serializers import UnitSerializer

class UnitView(generic.ListView):
    template_name = "inventore/index.html"
    context_object_name = "units"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["create_path"] = "inventore:unit-create"
        context["update_path"] = "inventore:unit-update"
        context["delete_path"] = "inventore:unit-delete"

        context['t_content'] = "inventore/unit/tcontent.html"

        return context

    def get_queryset(self):
        return [UnitSerializer(u) for u in Unit.objects.all()]

class UnitCreateView(generic.CreateView):
    model = Unit
    fields = ['unit_name', 'metric_unit', 'ratio']
    template_name = "inventore/utils/detail.html"
    success_url = reverse_lazy('inventore:unit')

class UnitDetailView(generic.UpdateView):
    model = Unit
    fields = ['unit_name', 'metric_unit', 'ratio']
    template_name = "inventore/utils/detail.html"
    success_url = reverse_lazy('inventore:unit')

class UnitDeleteView(generic.DeleteView):
    model = Unit
    template_name = "inventore/utils/delete.html"
    success_url = reverse_lazy('inventore:unit')