from django.db import models


# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=255, unique=True)
    capacity = models.IntegerField()
    projector = models.BooleanField(default=False)


class Reservation(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateField()
    comment = models.TextField(null=True)

    class Meta:
        unique_together = ('room_id', 'date',)


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
        room_data = Room.objects.get(id=room_id)
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


def reserve_room(room_id, reservation_date, comment):
    message = ""
    try:
        if comment:
            Reservation.objects.create(date=reservation_date, comment=comment,
                                       room_id_id=room_id)
        else:
            Reservation.objects.create(date=reservation_date,
                                       room_id_id=room_id)
    except Exception as e:
        message = "Database error"
    return message
