from django.db import models


class Residence(models.Model):
    # owner = models.ForeignKey() #TODO: Implements owner in future
    cep = models.CharField(max_length=7)
    address = models.CharField(max_length=11)


class Appliance(models.Model):
    name = models.CharField(max_length=55)
    type = models.CharField(max_length=25)  #Put choices


class Plug(models.Model):
    name = models.CharField(max_length=55)
    room = models.TextField()
    appliance = models.ForeignKey(Appliance, null=True, blank=True)


class Usage(models.Model):
    plug = models.ForeignKey(Plug)
    registered = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()
