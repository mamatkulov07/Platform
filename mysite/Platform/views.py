from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsAdminUserOrReadOnly
from rest_framework.permissions import IsAuthenticated


class HomeViewSets(viewsets.ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = HomeSerializers
    permission_classes = [IsAdminUserOrReadOnly]


class AboutUsViewSets(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializers
    permission_classes = [IsAdminUserOrReadOnly]


class StudyAbroadViewSets(viewsets.ModelViewSet):
    queryset = StudyAbroad.objects.all()
    serializer_class = StudyAbroadSerializers
    permission_classes = [IsAdminUserOrReadOnly]


class UniversityViewSets(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
    permission_classes = [IsAdminUserOrReadOnly]


class FacultyViewSets(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description']
    permission_classes = [IsAdminUserOrReadOnly]


class CountryViewSets(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializers
    filter_backends = [SearchFilter]
    search_fields = ['name']
    permission_classes = [IsAdminUserOrReadOnly]


class ContactsViewSets(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializers
    permission_classes = [IsAdminUserOrReadOnly]
