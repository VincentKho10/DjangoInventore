from django.urls import reverse_lazy
from django.views import generic

from inventore.models import MetricUnit
from inventore.serializers import MetricUnitSerializer

class MetricUnitView(generic.ListView):
    template_name = "inventore/index.html"
    context_object_name = "metric_units"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["create_path"] = "inventore:metric-unit-create"
        context["update_path"] = "inventore:metric-unit-update"
        context["delete_path"] = "inventore:metric-unit-delete"

        context['t_content'] = "inventore/metric_unit/tcontent.html"
        
        return context

    def get_queryset(self):
        return [MetricUnitSerializer(mu) for mu in MetricUnit.objects.all()]
    
class MetricUnitCreateView(generic.CreateView):
    model = MetricUnit
    fields = ['metric_unit_name']
    template_name = "inventore/utils/detail.html"    
    success_url = reverse_lazy('inventore:metric-unit')
    
class MetricUnitDetailView(generic.UpdateView):
    model = MetricUnit
    fields = ['metric_unit_name']
    template_name = "inventore/utils/detail.html"
    success_url = reverse_lazy('inventore:metric-unit')

class MetricUnitDeleteView(generic.DeleteView):
    model = MetricUnit
    template_name = "inventore/utils/delete.html"
    success_url = reverse_lazy('inventore:metric-unit')