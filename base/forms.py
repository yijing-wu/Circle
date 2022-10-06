from dataclasses import field
from django.forms import ModelForm
from .models import Room


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"
        exclude = ["host", "participants"]
        # use `exclude` to prevent showing these elements in frontend form
