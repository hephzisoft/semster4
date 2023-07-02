from django.db import models
from django.conf import settings

from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractUser




class User(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=14)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.first_name

class Room(models.Model):
    ROOM_CATEGORIES = (
    ('DEL', 'DELUXE'),
    ('KIN', 'KING'),
    ('QUE', 'QUEEN')
)
    number = models.IntegerField()
    description  = models.TextField()
    category = models.CharField(max_length=3, choices=ROOM_CATEGORIES)
    price  = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(0)])
    beds  = models.IntegerField()
    capacity = models.IntegerField()


    def __str__(self):
        return f'{self.number}. {self.category} with {self.beds} beds for {self.capacity} people'
   
class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()


    def __str__(self):
        return f'{self.user} has booked {self.room} from {self.check_in} to {self.check_out}'
    

class Feedback(models.Model):
    user  =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField()
    date_added = models.DateTimeField(auto_created=True)
