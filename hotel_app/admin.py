from django.contrib import admin


from .models import Booking,Feedback,Room
from users.models import User


admin.site.register(User)
admin.site.register(Booking)
admin.site.register(Feedback)
admin.site.register(Room)