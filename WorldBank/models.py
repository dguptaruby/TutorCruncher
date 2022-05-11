from django.db import models


class Country(models.Model):
    country_code = models.CharField(max_length=50, blank=True, null=True)
    country_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.country_code + " - " + self.country_name


class Metric(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    metric_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.id) + " - " + str(self.metric_name)


class Value(models.Model):
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE)
    country_code = models.CharField(max_length=50, blank=True, null=True)
    record_2006 = models.FloatField(null=True, blank=True)
    record_2007 = models.FloatField(null=True, blank=True)
    record_2004 = models.FloatField(null=True, blank=True)
    record_2005 = models.FloatField(null=True, blank=True)
    record_2008 = models.FloatField(null=True, blank=True)
    record_2009 = models.FloatField(null=True, blank=True)
    record_2011 = models.FloatField(null=True, blank=True)
    record_2010 = models.FloatField(null=True, blank=True)
    record_2013 = models.FloatField(null=True, blank=True)
    record_2012 = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.metric) + " - " + str(self.country_code)
