from pyexpat import model
from django.forms import ModelForm
from .models import Room, User


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"
        exclude = ["host", "participants"]
        # use `exclude` to prevent showing these elements in frontend form


class UserForm(ModelForm):
    class Meta:
        model = User
        # fields = "__all__"
        fields = ["username", "email"]
