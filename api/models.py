# -*- coding: utf-8 -*-
from django.db import models


def format_unicode(*args):
    return u' - '.join([unicode(arg) for arg in args])


class Residence(models.Model):
    # owner = models.ForeignKey() #TODO: Implements owner in future
    cep = models.CharField(max_length=7)
    address = models.CharField(u'Endereço', max_length=11)

    class Meta:
        app_label = 'api'
        db_table = 'residence'
        verbose_name = u'Residência'
        verbose_name_plural = u'Residências'

    def __unicode__(self):
        return format_unicode(self.cep, self.address)


class Appliance(models.Model):
    name = models.CharField('Nome', max_length=55)
    type = models.CharField('Tipo', max_length=25)  #Put choices

    class Meta:
        app_label = 'api'
        db_table = 'appliance'
        verbose_name = u'Aplicação'
        verbose_name_plural = u'Aplicações'

    def __unicode__(self):
        return format_unicode(self.name)


class Plug(models.Model):
    name = models.CharField('Nome', max_length=55)
    room = models.TextField(u'Cômodo')
    appliance = models.ForeignKey(Appliance, verbose_name=u'Aplicação', null=True, blank=True)
    connected = models.BooleanField('Conectado', default=False)
    priority = models.IntegerField('Prioridade', default=0)

    class Meta:
        app_label = 'api'
        db_table = 'plug'
        verbose_name = 'Tomada'
        verbose_name_plural = 'Tomadas'

    def __unicode__(self):
        return format_unicode(self.name, self.room)


class Usage(models.Model):
    plug = models.ForeignKey(Plug, verbose_name='Tomada')
    registered = models.DateTimeField('Data registrada', auto_now_add=True)
    total_usage = models.FloatField('Total Usado')
    kilowatt_hour = models.FloatField('KW/h')
    power = models.FloatField(u'Potência')
    voltage = models.FloatField('Voltagem')

    class Meta:
        app_label = 'api'
        db_table = 'usage'
        verbose_name = 'Consumo'
        verbose_name_plural = 'Consumos'

    def __unicode__(self):
        return format_unicode(self.plug.name, self.total_usage, self.registered)