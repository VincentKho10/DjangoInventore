from django.urls import path

from inventore import views

app_name = "inventore"

urlpatterns = [
    path('metric-unit', views.MetricUnitView.as_view(), name="metric_unit"),
    path('unit', views.UnitView.as_view(), name="unit")
]
