from django.contrib import admin
from .models import (UserProfile,Country,City,Amenity,Property,Favorite,Booking
,ImagesProperty,Payment,AvailabilityCalendar,Review,Message)

class ImageProperty(admin.TabularInline):
    model=ImagesProperty
    extra=1
class PropertyAdmin(admin.ModelAdmin):
    inlines = [ImageProperty]

admin.site.register(UserProfile)
admin.site.register(Favorite)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(AvailabilityCalendar)
admin.site.register(Review)
admin.site.register(Message)


from modeltranslation.admin import TranslationAdmin
@admin.register(Property)
class AllAdmin(TranslationAdmin):
    inlines =[ImageProperty]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
                'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
from modeltranslation.admin import TranslationAdmin
@admin.register(City,Country,Amenity)
class AllAdmin(TranslationAdmin):

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
                'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }