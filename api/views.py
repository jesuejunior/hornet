# Residence APIs
from rest_framework import generics
from api.models import Residence, Appliance, Plug, Usage
from api.serializers import ResidenceSerializer, ApplianceSerializer, PlugSerializer, UsageSerializer


class ResidenceBaseView(generics.GenericAPIView):
    model = Residence
    serializer_class = ResidenceSerializer
    queryset = Residence.objects.select_related().all()
    permission_classes = ()
    authentication_classes = ()


class ResidenceNew(ResidenceBaseView, generics.CreateAPIView):
    """
        Create a new residence
    """


class ResidenceList(ResidenceBaseView, generics.ListAPIView):

    """
        Residences list
    """


class ResidenceDetail(ResidenceBaseView, generics.RetrieveAPIView):

    """
        Detail residence selected
    """


class ResidenceEdit(ResidenceBaseView, generics.RetrieveUpdateAPIView):
    u"""
        Edit residence registered
    """


class ResidenceDelete(ResidenceBaseView, generics.DestroyAPIView):
    u"""
        Delete residence selected.
    """

# Appliance


class ApplianceBaseView(generics.GenericAPIView):
    model = Appliance
    serializer_class = ApplianceSerializer
    queryset = Appliance.objects.select_related().all()
    permission_classes = ()
    authentication_classes = ()


class ApplianceNew(ApplianceBaseView, generics.CreateAPIView):
    """
        Create a new appliance
    """


class ApplianceList(ApplianceBaseView, generics.ListAPIView):
    """
        Appliances list
    """


class ApplianceDetail(ApplianceBaseView, generics.RetrieveAPIView):

    """
        Detail appliance selected
    """


class ApplianceEdit(ApplianceBaseView, generics.RetrieveUpdateAPIView):
    u"""
        Edit appliance registered
    """


class ApplianceDelete(ApplianceBaseView, generics.DestroyAPIView):
    u"""
        Delete appliance selected.
    """

# Plug


class PlugBaseView(generics.GenericAPIView):
    model = Plug
    serializer_class = PlugSerializer
    queryset = Plug.objects.select_related().all()
    permission_classes = ()
    authentication_classes = ()


class PlugNew(PlugBaseView, generics.CreateAPIView):
    """
        Create a new plug
    """


class PlugList(PlugBaseView, generics.ListAPIView):
    """
        Plugs list
    """


class PlugDetail(PlugBaseView, generics.RetrieveAPIView):

    """
        Detail plug selected
    """


class PlugEdit(PlugBaseView, generics.RetrieveUpdateAPIView):
    u"""
        Edit plug registered
    """
    def connect_plug(self):
        pass

    def disconnect_plug(self):
        pass

    def manager_plug(self, request):
        if request.data.get('connected'):
            self.connect_plug()
        else:
            self.disconnect_plug()

    def put(self, request, *args, **kwargs):
        self.manager_plug(request)
        return super(PlugEdit, self).put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        self.manager_plug(request)
        return super(PlugEdit, self).patch(request, *args, **kwargs)


class PlugDelete(PlugBaseView, generics.DestroyAPIView):
    u"""
        Delete plug selected.
    """

# Usage


class UsageBaseView(generics.GenericAPIView):
    model = Usage
    serializer_class = UsageSerializer
    queryset = Usage.objects.select_related().all()
    permission_classes = ()
    authentication_classes = ()


class UsageNew(UsageBaseView, generics.CreateAPIView):
    """
        Create a new usage
    """


class UsageList(UsageBaseView, generics.ListAPIView):
    """
        Usages list
    """


class UsageDetail(UsageBaseView, generics.RetrieveAPIView):

    """
        Detail usage selected
    """


class UsageEdit(UsageBaseView, generics.RetrieveUpdateAPIView):
    u"""
        Edit usage registered
    """


class UsageDelete(UsageBaseView, generics.DestroyAPIView):
    u"""
        Delete usage selected.
    """

