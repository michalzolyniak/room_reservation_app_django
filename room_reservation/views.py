from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from room_reservation.check_functions import check_room, check_capacity, check_if_room_exist
from room_reservation.models import add_new_room


# Create your views here.

def main_page(request):
    room = "test"

    return render(request, 'main_menu.html', {
        'room': room
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
