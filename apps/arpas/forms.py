from django import forms

from .models import Object3D


class Object3DForm(forms.ModelForm):
    class Meta:
        model = Object3D
        fields = ("name", "file")
