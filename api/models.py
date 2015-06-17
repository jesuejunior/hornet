from django.db import models


class Residence(models.Model):
    # owner = models.ForeignKey() #TODO: Implements owner in future
    cep = models.CharField(max_length=7)
    address = models.CharField(max_length=11)

    class Meta:
        app_label = 'api'
        db_table = 'residence'


class Appliance(models.Model):
    name = models.CharField(max_length=55)
    type = models.CharField(max_length=25)  #Put choices

    class Meta:
        app_label = 'api'
        db_table = 'appliance'


class Plug(models.Model):
    name = models.CharField(max_length=55)
    room = models.TextField()
    appliance = models.ForeignKey(Appliance, null=True, blank=True)
    connected = models.BooleanField(default=True)

    class Meta:
        app_label = 'api'
        db_table = 'plug'


class Usage(models.Model):
    plug = models.ForeignKey(Plug)
    registered = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()

    class Meta:
        app_label = 'api'
        db_table = 'usage'