from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator

CHOSE_ROLES=(
('Администратор','•	Администратор'),
('Хост','Хост'),
('Гость','Гость')
)



class UserProfile(AbstractUser):
    phone_number=PhoneNumberField(region='KG',default='+996')
    age=models.PositiveSmallIntegerField(default=0,validators=[MinValueValidator(18)])
    profile_image=models.ImageField(upload_to='profile_image/',null=True,blank=True)
    role=models.CharField(max_length=13,choices=CHOSE_ROLES,default='Хост')

    def __str__(self):
        return self.username

class Country(models.Model):
    country_name=models.CharField(max_length=32)
    def __str__(self):
        return self.country_name
class City(models.Model):
    country=models.ForeignKey(Country,on_delete=models.CASCADE)
    city_name=models.CharField(max_length=32)
    def __str__(self):
        return self.city_name

class Amenity(models.Model):
    amenity_icon=models.ImageField(upload_to='amenity/')
    amenity_name=models.CharField(max_length=32)
    def __str__(self):
        return self.amenity_name

class Property(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    city=models.ForeignKey(City,on_delete=models.CASCADE)
    amenity=models.ManyToManyField(Amenity)
    property_name=models.CharField(max_length=32)
    property_avatar=models.ImageField(upload_to='property_avatar/')
    description=models.TextField()
    price=models.PositiveSmallIntegerField(default=0)
    created_at=models.DateField(auto_now_add=True)
    PROPERTY_TYPE=(
    ('hotel','hotel'),
    ('apartment','apartment'),
    ('house','house'),
    ('studio','studio')
    )
    property_type=models.CharField(max_length=9,choices=PROPERTY_TYPE,default='house')
    TYPE_STATUS=(
    ('is active','is active'),
    ('not active','not active')
    )
    status=models.CharField(max_length=10,choices=TYPE_STATUS,default='is active')

    def __str__(self):
        return self.property_name

    def get_avg_reviews(self):
        reviews = self.review.all()
        if reviews.exists():
            return sum([i.stars for i in reviews]) / reviews.count()
        return 0

    def get_count_reviews(self):
        reviews = self.review.all()
        if reviews.exists():
            return reviews.count()
        return 0


class ImagesProperty(models.Model):
    property=models.ForeignKey(Property,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='image_property/')
    def __str__(self):
        return self.property.property_name

class Booking(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    property=models.ForeignKey(Property,on_delete=models.CASCADE)
    check_in=models.DateField()
    check_out=models.DateField()
    for_adults=models.PositiveSmallIntegerField(default=0)
    for_kids=models.PositiveSmallIntegerField(default=0)
    create_date=models.DateField(auto_now_add=True)
    BOOKING_STATUS = (
        ('pending', 'pending'),
        ('confirmed', 'confirmed'),
        ('cancelled', 'cancelled'),
    )
    status=models.CharField(max_length=32,choices=BOOKING_STATUS,default='pending')

    def __str__(self):
        return f'{self.user}:{self.property}'

class Review(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    property=models.ForeignKey(Property,on_delete=models.CASCADE,related_name='review')
    comment=models.TextField(null=True,blank=True)
    stars=models.PositiveSmallIntegerField(choices=[(i,str(i)) for i in range(1,6)])
    created_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('user', 'property')


class Favorite(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    property=models.ForeignKey(Property,on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'property')
    def __str__(self):
        return f'{self.user}:{self.property}'

class Message(models.Model):
    sender=models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='sender_mess')
    receiver=models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='receiver_mess')
    text=models.TextField()
    class Meta:
        indexes = [
            models.Index(fields=['sender', 'receiver']),
    ]
    def __str__(self):
        return f'{self.sender}:{self.receiver}'




class Payment(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    booking=models.OneToOneField(Booking,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    STATUS_PAY=(
    ('paid','paid'),
    ('pending','pending'),
    ('failed','failed'),
    ('refunded','refunded')
    )
    status=models.CharField(max_length=8,choices=STATUS_PAY,default='pending')

    def __str__(self):
        return self.booking.user.username
class AvailabilityCalendar(models.Model):
    property=models.ForeignKey(Property,on_delete=models.CASCADE)
    date=models.DateField()
    is_booked=models.BooleanField(default=True)

    def __str__(self):
        return self.property.property_name




