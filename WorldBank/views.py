from django.shortcuts import render
from django.db.models import Avg, Count, Min, Sum, Max
from .models import Value


def getAggregationData(filter_key):
    # get aggregate value from years column
    filter_key1 = filter_key + '__isnull'
    my_filter = {filter_key1: True}

    valueObj = Value.objects.exclude(**my_filter)
    valueObj = valueObj.aggregate(record_count=Count(filter_key), record_max=Max(filter_key),
                                  record_min=Min(filter_key), record_avg=Avg(filter_key),
                                  record_sum=Sum(filter_key))
    return valueObj


def metricData(request):
    # query param
    metric_id = request.GET.get("metric_id")
    country_code = request.GET.get("country_code")
    order_type = request.GET.get("order_type")
    record_years = request.GET.get("record_year")

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

    aggregate_values = None
    rec_val = record_years if record_years else "2004"
    aggregate_values = getAggregationData("record_" + rec_val)

    context = {'metric_obj': metric_data, "aggregate_obj": aggregate_values}
    return render(request, 'metric_list.html', context)
