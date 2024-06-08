from django.forms import ModelForm
from .models import *

class form_class(ModelForm):
    class Meta:
        model = class_models
        fields ='__all__'
