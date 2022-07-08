"""reservation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from room_reservation.views import main_page, AddNewRoom, \
    Rooms, DeleteRoom, ModifyRoom, ReserveRoom, RoomReservations

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rooms/', main_page),
    path('room/new/', AddNewRoom.as_view()),
    path('availability_rooms', Rooms.as_view(), name="room-list"),
    path('room/delete/<int:room_id>/', DeleteRoom.as_view()),
    path('room/modify/<int:room_id>/', ModifyRoom.as_view()),
    path('room/reserve/<int:room_id>/', ReserveRoom.as_view()),
    path('room/room_reservations/<int:room_id>/', RoomReservations.as_view()),
]
