from django.urls import path
from .views import *

urlpatterns = [
    path('home/', HomeViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='home_list'),

    path('home/<int:pk>/', HomeViewSets.as_view({'get': 'retrieve', 'put': 'update',  'delete':  'destroy'}),
         name='home_detail'),

    path('aboutus/', AboutUsViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='aboutus_list'),

    path('aboutus/<int:pk>/', AboutUsViewSets.as_view({'get': 'retrieve', 'put': 'update',  'delete':  'destroy'}),
         name='aboutus_detail'),


    path('studyabroad/', StudyAbroadViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='studyabroad_list'),

    path('studyabroad/<int:pk>/', StudyAbroadViewSets.as_view({'get': 'retrieve', 'put': 'update',  'delete':  'destroy'}),
         name='studyabroad_detail'),


    path('country/', CountryViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='country_list'),

    path('country/<int:pk>/', CountryViewSets.as_view({'get': 'retrieve', 'put': 'update',  'delete':  'destroy'}),
         name='country_detail'),


    path('university/', UniversityViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='university_list'),

    path('university/<int:pk>/', UniversityViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='university_detail'),


    path('faculty/', FacultyViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='faculty_list'),

    path('faculty/<int:pk>/', FacultyViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='faculty_detail'),


    path('contacts/', ContactsViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='contacts_list'),

    path('contacts/<int:pk>/', ContactsViewSets.as_view({'get': 'retrieve', 'put': 'update',  'delete':  'destroy'}),
         name='contacts_detail'),

]