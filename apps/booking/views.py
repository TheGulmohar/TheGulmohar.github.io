from django.shortcuts import render

from apps.booking.forms import AvailabilityForm
from apps.utils.constants import RoomTypeEnum
from .models import Room
from apps.gulmohar.models import Customer
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.
def room_list(request):
    rooms = Room.objects.filter(is_available=True)
    return render(request, 'booking/room_list.html', {'rooms': rooms})


from django.shortcuts import render
from .models import Booking

def booking_details(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'booking/booking_details.html', {'booking': booking})

from django.shortcuts import render
from django.contrib.auth.models import User

def user_management(request):
    users = User.objects.all()
    return render(request, 'booking/user_management.html', {'users': users})





def book_sample(request):
    if request.method == 'GET':
        print("GRT TRIGGRED")
        return render(request, "booking/booking_2.html", {})


def check_availability(request):
    
    if request.method == 'POST':
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            room_type = form.cleaned_data['room_type']

            if room_type:
                rooms = Room.objects.filter(room_type=room_type)
            else:
                room = Room.objects.all()

            available_rooms = rooms.exclude(
                Q(booking__start_date__lt=end_date) & Q(booking__end_date__gt=start_date)
            )

            data_room = {}
            if not room_type:
                for room in RoomTypeEnum:
                    data_room[room.name] = available_rooms.filter(room_type=room.value).count()
            else:
                data_room[room_type] = available_rooms.count()

            context = {
                'available_rooms': available_rooms,
                'form': form,
            }
            return render(request, 'booking/booking_2.html', context)
    else:
        form = AvailabilityForm()
    return render(request, 'booking/booking_2_orig.html', {'form': form})



def book_room(request):
    if request.method == 'GET':
        print("GRT TRIGGRED")

        return render(request, "booking/booking_2.html")

    if request.method == 'POST':
        room_number = request.POST['room_number']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        customer_id = request.POST['customer']
        print(request.POST)
        customer = Customer.objects.get(id=customer_id)
        room = Room.objects.filter(is_available=True).first()

        if room:

            booking = Booking(room=room, start_date=start_date, end_date=end_date, customer=customer)
            room.is_available=False
            room.save()
            booking.save()

            # return redirect('booking_success', room_number="12")
            # return redirect('landing7')
            return redirect('booking_success', room_number='23', start_date=start_date, end_date=end_date)


        html = "<html><body>Rooms are full</body></html>"    
        return HttpResponse(html)
    
    customers = Customer.objects.all()
    return render(request, 'booking/booking.html', {'customers': customers})

def booking_success(request, room_number, start_date, end_date):
    return render(request, 'booking/booking_success.html', {'room_number': room_number, 'start_date': start_date, 'end_date': end_date})
# def booking_success(request, room_number):
#     return render(request, 'booking/booking_success_test.html', {'room_number': room_number, 'start_date': start_date, 'end_date': end_date})
