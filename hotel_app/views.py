from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Room, Booking, UserProfile, Feedback
from .forms import BookingForm, UserProfileForm, FeedbackForm, UserRegisterForm
from django.contrib import messages



def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
           
            messages.success(request, f'Your account has been created! You are able to login'),
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'hotel_app/register.html', {'form': form})


def room_list(request):
    rooms = Room.objects.filter(available=True)
    return render(request, 'room_list.html', {'rooms': rooms})

@login_required
def book_room(request, room_id):
    room = Room.objects.get(id=room_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.room = room
            booking.save()
            room.available = False
            room.save()
            return redirect('booking_confirmation')
    else:
        form = BookingForm()
    return render(request, 'book_room.html', {'room': room, 'form': form})

@login_required
def booking_confirmation(request):
    user_bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking_confirmation.html', {'user_bookings': user_bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    room = booking.room
    booking.delete()
    room.available = True
    room.save()
    return redirect('booking_confirmation')

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'profile.html', {'form': form})

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            return redirect('feedback_thankyou')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})

def feedback_thankyou(request):
    return render(request, 'feedback_thankyou.html')
