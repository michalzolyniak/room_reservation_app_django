from django.db import models


# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=255, unique=True)
    capacity = models.IntegerField()
    projector = models.BooleanField(default=False)


def get_rooms():
    return Room.objects.all()


def get_room_detail(room_id):
    room_details = Room.objects.all()
    return room_details.filter(id=room_id)


def add_new_room(name, capacity, projector):
    try:
        Room.objects.create(name=name, capacity=capacity,
                            projector=projector)
    except Exception as e:
        return False
    return True


def update_room(room_id, name, capacity, projector):
    try:
        room_data = get_room_detail(room_id)
        room_data.name = name
        room_data.capacity = capacity
        room_data.projector = projector
        room_data.save()
    except Exception as e:
        return False
    return True


def delete_room(room_id):
    try:
        Room.objects.filter(id=room_id).delete()
    except Exception as e:
        return False
    return True
