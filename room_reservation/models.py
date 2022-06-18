from django.db import models


# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=255, unique=True)
    capacity = models.IntegerField()
    projector = models.BooleanField(default=False)


def add_new_room(name, capacity, projector):
    print(name)
    print(capacity)
    print(projector)
    try:
        Room.objects.create(name=name, capacity=capacity,
                            projector=projector)
    except Exception as e:
        return False
    return True
