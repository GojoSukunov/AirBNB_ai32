from django_filters.rest_framework import FilterSet



from .models import Property


class PropertyFilter(FilterSet):
    class Meta:
        model=Property
        fields={
            'city':['exact'],
            'price':['exact','gte','lte']
        }