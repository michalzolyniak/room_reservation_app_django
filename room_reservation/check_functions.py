from room_reservation.models import Room


def check_if_room_exist(room_name):
    room_details = Room.objects.all()
    if room_details.filter(name=room_name).count() > 0:
        return True
    else:
        return False


def check_room(room_name):
    if not room_name:
        return "Please fill room name"
    if not isinstance(room_name, str):
        return "Room name must be string"
    if check_if_room_exist(room_name):
        return "This room name exist in our database please"


def check_capacity(capacity):
    try:
        capacity_int = int(capacity)
    except ValueError:
        return "Capacity must be integer"
    if capacity_int <= 0:
        return "Capacity must be integer greater then 0"
