"""hornet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from api.views import ResidenceList, ResidenceDetail, ResidenceEdit, ResidenceDelete, ResidenceNew, ApplianceList, \
    ApplianceNew, ApplianceDetail, ApplianceEdit, ApplianceDelete, PlugList, PlugNew, PlugDetail, PlugEdit, PlugDelete, \
    UsageList, UsageNew, UsageDetail, UsageEdit, UsageDelete

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]

urlpatterns += patterns('api.views.residence',
                        url(r'^residence$', ResidenceList.as_view(), name='residence-list'),
                        url(r'^residence/new$', ResidenceNew.as_view(), name='residence-new'),
                        url(r'^residence/(?P<pk>[\d]+)/detail$', ResidenceDetail.as_view(), name='residence-detail'),
                        url(r'^residence/(?P<pk>[\d]+)/edit$', ResidenceEdit.as_view(), name='residence-edit'),
                        url(r'^residence/(?P<pk>[\d]+)/delete$', ResidenceDelete.as_view(), name='residence-delete'),
                        )

urlpatterns += patterns('api.views.appliance',
                        url(r'^appliance$', ApplianceList.as_view(), name='appliance-list'),
                        url(r'^appliance/new$', ApplianceNew.as_view(), name='appliance-new'),
                        url(r'^appliance/(?P<pk>[\d]+)/detail$', ApplianceDetail.as_view(), name='appliance-detail'),
                        url(r'^appliance/(?P<pk>[\d]+)/edit$', ApplianceEdit.as_view(), name='appliance-edit'),
                        url(r'^appliance/(?P<pk>[\d]+)/delete$', ApplianceDelete.as_view(), name='appliance-delete'),
                        )

urlpatterns += patterns('api.views.plug',
                        url(r'^plug$', PlugList.as_view(), name='plug-list'),
                        url(r'^plug/new$', PlugNew.as_view(), name='plug-new'),
                        url(r'^plug/(?P<pk>[\d]+)/detail$', PlugDetail.as_view(), name='plug-detail'),
                        url(r'^plug/(?P<pk>[\d]+)/edit$', PlugEdit.as_view(), name='plug-edit'),
                        url(r'^plug/(?P<pk>[\d]+)/delete$', PlugDelete.as_view(), name='plug-delete'),
                        )

urlpatterns += patterns('api.views.usage',
                        url(r'^usage$', UsageList.as_view(), name='usage-list'),
                        url(r'^usage/new$', UsageNew.as_view(), name='usage-new'),
                        url(r'^usage/(?P<pk>[\d]+)/detail$', UsageDetail.as_view(), name='usage-detail'),
                        url(r'^usage/(?P<pk>[\d]+)/edit$', UsageEdit.as_view(), name='usage-edit'),
                        url(r'^usage/(?P<pk>[\d]+)/delete$', UsageDelete.as_view(), name='usage-delete'),
                        )