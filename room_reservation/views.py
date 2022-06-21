from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from room_reservation.check_functions import check_room, check_capacity, check_if_room_exist
from room_reservation.models import add_new_room, get_rooms, delete_room, \
    get_room_detail, update_room


# Create your views here.

def main_page(request):
    return render(request, 'main_page.html', {
    })


@method_decorator(csrf_exempt, name='dispatch')
class AddNewRoom(View):
    def get(self, request):
        return render(request, 'add_new_room.html', {
        })

    def post(self, request):
        errors = list()
        user_info = list()
        room_name = request.POST.get('room_name')
        capacity = request.POST.get('capacity')
        projector = request.POST.get('projector')

        if projector == "on":
            projector = True
        else:
            projector = False

        error = check_room(room_name)
        if error:
            errors.append(error)

        error = check_capacity(capacity)
        if error:
            errors.append(error)

        if errors:
            user_info = errors
        else:
            if add_new_room(room_name, capacity, projector):
                user_info.append("New room has been added to our database")
            else:
                user_info.append("Database error")
        return render(request, 'add_new_room.html', {
            'user_info': user_info
        })


@method_decorator(csrf_exempt, name='dispatch')
class Rooms(View):
    def get(self, request):
        rooms = get_rooms()
        return render(request, 'rooms.html', {
            'rooms': rooms
        })


@method_decorator(csrf_exempt, name='dispatch')
class DeleteRoom(View):
    def get(self, request, room_id):
        room_deleted = delete_room(room_id)
        return redirect("room-list")


@method_decorator(csrf_exempt, name='dispatch')
class ModifyRoom(View):
    def get(self, request, room_id):
        room_details = get_room_detail(room_id)
        return render(request, 'modify_room.html', {
            'room_details': room_details
        })

    def post(self, request):
        errors = list()
        user_info = list()
        room_name = request.POST.get('room_name')
        capacity = request.POST.get('capacity')
        projector = request.POST.get('projector')

        if projector == "on":
            projector = True
        else:
            projector = False

        error = check_room(room_name)
        if error:
            errors.append(error)

        error = check_capacity(capacity)
        if error:
            errors.append(error)

        if errors:
            user_info = errors
        else:
            if update_room(room_name, capacity, projector):
                user_info.append("New room has been added to our database")
            else:
                user_info.append("Database error")
        return render(request, 'add_new_room.html', {
            'user_info': user_info
        })
