from django.urls import path

from inventore import views

app_name = "inventore"

urlpatterns = [
    path('api/metric_unit', views.MetricUnitViewApi.as_view(), name="api_metric_unit"),
    path('api/unit', views.UnitViewApi.as_view(), name="api_unit"),
    path('metric_unit', views.MetricUnitView.as_view(), name="metric_unit")
]
