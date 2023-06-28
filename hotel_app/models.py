from django.db import models


class Room(models.Model):
    ROOM_CATEGORIES = (
    ('DEL', 'DELUXE'),
    ('KIN', 'KING'),
    ('QUE', 'QUEEN')
)
    number = models.IntegerField()
    category = models.CharField(max_length=3, choices=ROOM_CATEGORIES)
    beds  = models.IntegerField()
    capacity = models.IntegerField()


    def __str__(self):
        return f'{self.number}. {self.category} with {self.beds} beds for {self.capacity} people'
   