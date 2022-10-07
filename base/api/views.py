from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer
from base.api import serializers


@api_view(["GET"])
def getRoutes(request):
    routes = [
        "GET /api",
        "GET /api/rooms",
        "GET /api/rooms/:id",
    ]
    return Response(routes)


@api_view(["GET"])
def getRooms(request):
    rooms = Room.objects.all()
    # we get python list query set here,
    # need to serialize, turn python objects into JSON objects
    serializer = RoomSerializer(rooms, many=True)
    # many means we what to serialize many objects
    return Response(serializer.data)
