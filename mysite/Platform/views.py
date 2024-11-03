from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.filters import SearchFilter


class HomeViewSets(viewsets.ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = HomeSerializers


class AboutUsViewSets(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializers


class StudyAbroadViewSets(viewsets.ModelViewSet):
    queryset = StudyAbroad.objects.all()
    serializer_class = StudyAbroadSerializers


class CountryViewSets(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializers
    filter_backends = [SearchFilter]
    search_fields = ['higher', 'specializations', 'countrys']


class ContactsViewSets(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializers
