from rest_framework import routers
from django.urls import path,include
from .views import  (UserProfileViewSet,CountryViewSet,CityViewSet,PropertyListViewSet,PropertyDetailViewSet,AmenityViewSet,
                     ImagesPropertyViewSet,FavoriteViewSet,BookingViewSet,PaymentViewSet,AvailabilityCalendarViewSet,ReviewViewSet,MessageViewSet)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router=routers.DefaultRouter()


router.register(r'user_profile',UserProfileViewSet,basename='user-profile'),
router.register(r'country',CountryViewSet,basename='country'),
router.register(r'city',CityViewSet,basename='city'),
router.register(r'amenity',AmenityViewSet,basename='amenity'),
router.register(r'image-property',ImagesPropertyViewSet,basename='image-property'),
router.register(r'favorite',FavoriteViewSet,basename='favorite'),
router.register(r'booking',BookingViewSet,basename='booking'),
router.register(r'payment',PaymentViewSet,basename='payment'),
router.register(r'availability-calendary',AvailabilityCalendarViewSet,basename='availability-calendary'),
router.register(r'review',ReviewViewSet,basename='review'),
router.register('message/',MessageViewSet,basename='message')

urlpatterns=[
    path('',include(router.urls)),
    path('properties',PropertyListViewSet.as_view(),name='property_list'),
    path('property/<int:pk>/',PropertyDetailViewSet.as_view(),name='property_detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


