from django.shortcuts import render

from .models import Value


def metricData(request):
    # query param
    metric_id = request.GET.get("metric_id")
    country_code = request.GET.get("country_code")
    order_type = request.GET.get("order_type")

    if not metric_id and not country_code:
        # get all metric data
        metric_data = Value.objects.all()
        if order_type == 'desc':
            metric_data = metric_data.order_by("-country_code")
    elif metric_id and not country_code:
        # only metric id filter data
        metric_data = Value.objects.filter(metric_id=metric_id)
        if order_type == 'desc':
            metric_data = metric_data.order_by("-country_code")
    elif country_code and not metric_id:
        # only country code filter data
        metric_data = Value.objects.filter(country_code=country_code)
        if order_type == 'desc':
            metric_data = metric_data.order_by("-country_code")
    else:
        # filter country and filter data
        metric_data = Value.objects.filter(country_code=country_code, metric_id=metric_id)
        if order_type == 'desc':
            metric_data = metric_data.order_by("-country_code")

    context = {'metric_obj': metric_data}
    return render(request, 'metric_list.html', context)