from rest_framework import serializers
from .models import (UserProfile,Country,City,Amenity,Property,Favorite,Booking
,ImagesProperty,Payment,AvailabilityCalendar,Review,Message)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields=['id','username']

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model=Country
        fields='__all__'


class CitySerializer(serializers.ModelSerializer):
    country=CountrySerializer()
    class Meta:
        model=City
        fields=['id','city_name','country']

class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model=Amenity
        fields='__all__'

class PropertyListSerializer(serializers.ModelSerializer):
    city=CitySerializer()
    get_avg_reviews=serializers.SerializerMethodField()
    class Meta:
        model=Property
        fields=['id','property_name','property_avatar',
                'price','property_type','city','get_avg_reviews']

    def get_avg_reviews(self, obj):
        return obj.get_avg_reviews()

class ReviewSerializer(serializers.ModelSerializer):
    user=UserProfileSerializer()
    class Meta:
        model=Review
        fields=['id','comment','stars','created_date','user']

class PropertyDetailSerializer(serializers.ModelSerializer):
    user=UserProfileSerializer()
    city=CitySerializer()
    review=ReviewSerializer(read_only=True,many=True)
    amenity=AmenitySerializer(many=True,read_only=True)
    get_avg_reviews=serializers.SerializerMethodField()
    get_count_reviews=serializers.SerializerMethodField()
    class Meta:
        model=Property
        fields=['id','property_name','property_avatar','description',
                'price','property_type','status','user','city','amenity','review','get_avg_reviews','get_count_reviews']

    def get_avg_reviews(self, obj):
        return obj.get_avg_reviews()

    def get_count_reviews(self, obj):
        return obj.get_count_reviews()


class FavoriteSerializer(serializers.ModelSerializer):
    user=UserProfileSerializer()
    property=PropertyListSerializer()
    class Meta:
        model=Favorite
        fields=['id','user','property']

class BookingSerializer(serializers.ModelSerializer):
    property=PropertyListSerializer()
    user=UserProfileSerializer()
    class Meta:
        model=Booking
        fields=['id','check_in','check_out',
                'for_adults','for_kids','create_date','status','user','property']

class ImagesPropertySerializer(serializers.ModelSerializer):
    property=PropertyListSerializer()
    class Meta:
        model=ImagesProperty
        fields=['id','image','property']
class BookingSimpleSerializer(serializers.ModelSerializer):
    property=PropertyListSerializer()
    class Meta:
        model=Booking
        fields=['check_in','check_out','property']

class PaymentSerializer(serializers.ModelSerializer):
    booking=BookingSimpleSerializer()
    class Meta:
        model=Payment
        fields=['id','amount','status','booking']


class AvailabilityCalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model=AvailabilityCalendar
        fields='__all__'


class MessageSerializer(serializers.ModelSerializer):
    receiver_mess=UserProfileSerializer(source='sender')
    sender_mess=UserProfileSerializer(source='receiver')
    class Meta:
        model=Message
        fields=['id','text','sender_mess','receiver_mess']
