from rest_framework import viewsets,generics
from django.db.models import Avg
from .models import (UserProfile,Country,City,Amenity,Property,Favorite,Booking
,ImagesProperty,Payment,AvailabilityCalendar,Review,Message)
from .serializers import (UserProfileSerializer,CountrySerializer,CitySerializer,AmenitySerializer,PropertyListSerializer,PropertyDetailSerializer,FavoriteSerializer,BookingSerializer,
                          ImagesPropertySerializer,PaymentSerializer,ReviewSerializer,MessageSerializer,AvailabilityCalendarSerializer)
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import PropertyPagination
from .filter import PropertyFilter
from rest_framework import permissions
from .permission import IsOwnerOrAdmin, ReviewPermission, MessagePermission, AvailabilityPermission




class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAdminUser]
class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [permissions.IsAdminUser]
class AmenityViewSet(viewsets.ModelViewSet):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer
    permission_classes = [permissions.IsAdminUser]
class PropertyListViewSet(generics.ListCreateAPIView):
    queryset = Property.objects.annotate(
        avg_reviews=Avg('review__stars'))
    serializer_class = PropertyListSerializer
    filter_backends = [SearchFilter,OrderingFilter,DjangoFilterBackend]
    search_fields=['city__city_name','property_name','amenity__amenity_name','property_type']
    ordering_fields=['created_at','price','avg_reviews']
    filterset_class=PropertyFilter
    pagination_class =PropertyPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class PropertyDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyDetailSerializer
    permission_classes = [IsOwnerOrAdmin]
class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated,ReviewPermission]
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated,ReviewPermission]
class ImagesPropertyViewSet(viewsets.ModelViewSet):
    queryset = ImagesProperty.objects.all()
    serializer_class = ImagesPropertySerializer
    permission_classes = [IsOwnerOrAdmin]
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated,ReviewPermission]


class AvailabilityCalendarViewSet(viewsets.ModelViewSet):
    queryset = AvailabilityCalendar.objects.all()
    serializer_class = AvailabilityCalendarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,AvailabilityPermission]
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,ReviewPermission]
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated,MessagePermission]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
