from datetime import datetime
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from room_reservation.check_functions import check_room, check_capacity, room_available, \
    bad_reservation_date, check_post_data
from room_reservation.models import add_new_room, get_rooms, delete_room, \
    get_room_detail, update_room, reserve_room, get_room_reservations, check_room_reservations


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
            'rooms': rooms,
            # 'current_reservations': current_reservations
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

    def post(self, request, room_id):
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
            room_details = get_room_detail(room_id)
            return render(request, 'modify_room.html', {
                'room_details': room_details,
                'user_info': user_info
            })
        else:
            if update_room(room_id, room_name, capacity, projector):
                return redirect("room-list")
            else:
                user_info.append("Database error")
                room_details = get_room_detail(room_id)
                return render(request, 'modify_room.html', {
                    'room_details': room_details,
                    'user_info': user_info
                })


@method_decorator(csrf_exempt, name='dispatch')
class ReserveRoom(View):
    def get(self, request, room_id):
        return render(request, 'reserve_room.html')

    def post(self, request, room_id):
        error = ""
        errors = ()
        comment = request.POST.get('comment')
        errors = check_post_data(room_id, request.POST.get('reservation_date'))
        if not errors:
            reservation_date = datetime.strptime(request.POST.get('reservation_date'), "%Y-%m-%d")
            error = reserve_room(room_id, reservation_date, comment)
            if error:
                errors.append(error)
        if errors:
            return render(request, 'reserve_room.html', {
                'user_info': errors,
                'comment': comment
            })
        else:
            return redirect("room-list")


@method_decorator(csrf_exempt, name='dispatch')
class RoomReservations(View):
    def get(self, request, room_id):
        room_details = get_room_detail(room_id)
        room_reservations = get_room_reservations(room_id)
        return render(request, 'room_reservations.html', {
            'room_details': room_details,
            'room_reservations': room_reservations
        })
