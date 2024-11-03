from rest_framework import serializers
from .models import *


class HomeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'


class AboutUsSerializers(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'


class StudyAbroadSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudyAbroad
        fields = '__all__'


class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class ContactsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'