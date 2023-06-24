from django.db import models
from users.models import User
from django.core.validators import MinValueValidator





class Room(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    price = models.DecimalField(
        decimal_places=2, max_digits=10, validators=[MinValueValidator(0)])
    room_no = models.PositiveIntegerField(unique=True)
    

    def __str__(self):
        return f"Room {self.name} no-{self.room_no}"
    


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    isBooked  = models.BooleanField(default=False)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"{self.room.name} - {self.user.username}"



class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.user.username} at {self.created_at}"
