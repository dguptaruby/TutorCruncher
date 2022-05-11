"""
Script for importing world bank data into django.

You need to edit this to actually import data, however it will run now to show you what's in the data.
"""
import json
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DevTest.settings')
django.setup()
from WorldBank.models import Value as recordsModel, Metric as metricsModel, Country as countryModel


def load_data():
    data = json.load(open('data.json', 'r'))
    records = data['records']
    countries = data['countries']
    metrics = data['metrics']

    for c_code, c_name in countries.items():
        # save your country data if empty.
        countryObj = countryModel.objects.all()
        if len(countryObj) != len(countries):
            countryModel.objects.create(country_code=c_code, country_name=c_name)
        else:
            print("All ready inserted.")
            break

    for m_name, m_id in metrics.items():
        # save your metrics data
        metricsObj = metricsModel.objects.all()
        if len(metricsObj) != len(metrics):
            metricsModel.objects.create(id=m_id, metric_name=m_name)
        else:
            print("All ready inserted.")
            break

    for r in records:
        # save your records data
        recordObj = recordsModel.objects.all()
        if len(recordObj) != len(records):
            recordsModel.objects.create(
                metric=metricsModel.objects.get(id=r['metric_id']),
                country_code=r['Country Code'],
                record_2006=r['2006'],
                record_2007=r['2007'],
                record_2004=r['2004'],
                record_2005=r['2005'],
                record_2008=r['2008'],
                record_2009=r['2009'],
                record_2011=r['2011'],
                record_2010=r['2010'],
                record_2013=r['2013'],
                record_2012=r['2012'],
            )
        else:
            print("All ready inserted.")
            break


load_data()
