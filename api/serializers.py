# encoding: utf-8
from rest_framework import serializers
from api.models import Plug, Residence, Usage, Appliance

__author__ = 'jesuejunior'


class PlugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plug
        fields = ('id', 'room', 'appliance', 'connected', 'priority')


class ResidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Residence
        fields = ('id', 'cep', 'address', )


class UsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usage
        fields = ('id', 'plug', 'registered', 'total_usage',
                  'kilowatt_hour', 'power', 'voltage')


class ApplianceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appliance
        fields = ('id', 'name', 'type')