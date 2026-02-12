from django.urls import path

from inventore import views

app_name = "inventore"

api = [
    path('api/unit', views.UnitViewApi.as_view(), name="api-unit"),
    path('api/metric_unit', views.MetricUnitViewApi.as_view(), name="api-metric-unit"),
]

metric_unit_path = [
    path('metric_unit', views.MetricUnitView.as_view(), name="metric-unit"),
    path('metric_unit/<int:pk>/edit', views.MetricUnitDetailView.as_view(), name="metric-unit-update"),
    path('metric_unit/<int:pk>/delete', views.MetricUnitDeleteView.as_view(), name="metric-unit-delete"),
    path('metric_unit/create', views.MetricUnitCreateView.as_view(), name="metric-unit-create"),
]

unit_path = [
    path('unit', views.UnitView.as_view(), name='unit'),
    path('unit/<int:pk>/edit', views.UnitDetailView.as_view(), name='unit-update'),
    path('unit/<int:pk>/delete', views.UnitDeleteView.as_view(), name='unit-delete'),
    path('unit/create', views.UnitCreateView.as_view(), name='unit-create'),
]

tax_path = [
    path('tax', views.TaxView.as_view(), name='tax'),
    path('tax/<int:pk>/edit', views.TaxDetailView.as_view(), name='tax-update'),
    path('tax/<int:pk>/delete', views.TaxDeleteView.as_view(), name='tax-delete'),
    path('tax/create', views.TaxCreateView.as_view(), name='tax-create'),
]

item_path = [
    path('item', views.ItemView.as_view(), name='item'),
    path('item/<int:pk>/edit', views.ItemDetailView.as_view(), name='item-update'),
    path('item/<int:pk>/delete', views.ItemDeleteView.as_view(), name='item-delete'),
    path('item/create', views.ItemCreateView.as_view(), name='item-create'),
]

urlpatterns = api+metric_unit_path+unit_path+tax_path+item_path
