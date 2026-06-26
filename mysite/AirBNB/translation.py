from modeltranslation.translator import register, TranslationOptions
from .models import Country, City, Amenity, Property


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country_name',)


@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = ('city_name',)


@register(Amenity)
class AmenityTranslationOptions(TranslationOptions):
    fields = ('amenity_name',)


@register(Property)
class PropertyTranslationOptions(TranslationOptions):
    fields = ('property_name', 'description')