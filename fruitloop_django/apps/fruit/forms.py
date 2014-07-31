from django import forms
from django.core.exceptions import ValidationError

from .models import FruitLocation


class FruitForm(forms.ModelForm):

    class Meta:
        model = FruitLocation
        fields = (
            'address', 
            'fruit_type', 
            'comment'
        )