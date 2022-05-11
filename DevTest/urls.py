from django.urls import path
from django.views.generic import TemplateView
from WorldBank.views import metricData

from django.contrib import admin

urlpatterns = [
    # path('', TemplateView.as_view(template_name='index.html')),
    path('', metricData),  # get all metric data
    path('<int:metric_id>/', metricData),  # filter by metric id
    path('<str:country_code>/', metricData),  # filter by country code
    path('<int:metric_id>/<str:country_code>/', metricData),  # filter by country code and metric id
    path('admin/', admin.site.urls),
]
