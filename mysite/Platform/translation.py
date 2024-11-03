from .models import *
from modeltranslation.translator import TranslationOptions, register


@register(Home)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'title', 'exams')


@register(AboutUs)
class ProductTranslationOptions(TranslationOptions):
    fields = ('nameperson', 'descriptions', 'profession')


@register(StudyAbroad)
class ProductTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(Country)
class ProductTranslationOptions(TranslationOptions):
    fields = ('specializations', 'countrys', 'higher')


@register(Contacts)
class ProductTranslationOptions(TranslationOptions):
    fields = ('firstname', 'lastname', 'company', 'help')
