
# Register your models here.
from django.contrib import admin
from.models import Room, Booking

class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'capacity', 'price', 'is_available')
    search_fields = ('name', 'description')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer', 'room', 'start_date', 'end_date', 'created_at', 'updated_at')
    search_fields = ('customer__user__username', 'room__name')

admin.site.register(Room, RoomAdmin)
admin.site.register(Booking, BookingAdmin)