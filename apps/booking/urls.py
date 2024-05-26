from django.urls import path
from . import views

urlpatterns = [
    path('rooms/', views.room_list, name='room_list'),
    path('booking/<int:booking_id>/', views.booking_details, name='booking_details'),
    path('user-management/', views.user_management, name='user_management'),
    path('book/', views.book_room, name='book_room'),
    path('booking-success/<str:room_number>/<str:start_date>/<str:end_date>/', views.booking_success, name='booking_success'),
    # path('booking-success/<str:room_number>', views.booking_success, name='booking_success'),
  
]