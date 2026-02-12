from django.urls import reverse_lazy
from django.views import generic

from inventore.serializers import TaxSerializer
from inventore.services.crud_services.service_crud_tax import serviceCreateTax, serviceGetOneTax
from inventore.models import Tax

class TaxView(generic.ListView):
    template_name = "inventore/index.html"
    context_object_name = "taxes"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["create_path"] = "inventore:tax-create"
        context["update_path"] = "inventore:tax-update"
        context["delete_path"] = "inventore:tax-delete"

        context['t_content'] = "inventore/model_content/tcontent_tax.html"

        return context

    def get_queryset(self):
        return Tax.objects.all()

class TaxCreateView(generic.CreateView):
    model = Tax
    fields = ['tax_value']
    template_name = "inventore/utils/detail.html"
    success_url = reverse_lazy('inventore:tax')
    
    def form_valid(self, form):
        print(form)
        post = form.save(commit=False)

        post.tax_value = post.tax_value/100
        post.save()
        return super().form_valid(form)
        

class TaxDetailView(generic.UpdateView):
    model = Tax
    fields = ['id','tax_value']
    template_name = "inventore/utils/detail.html"
    success_url = reverse_lazy('inventore:tax')

    def get_form(self):
        form = super().get_form(None)
        form.initial['tax_value']*=100
        return form
    
    def form_valid(self, form):
        print(form)
        post = form.save(commit=False)

        post.tax_value = post.tax_value/100
        post.save()
        return super().form_valid(form)

class TaxDeleteView(generic.DeleteView):
    model = Tax
    template_name = "inventore/utils/delete.html"
    success_url = reverse_lazy('inventore:tax')