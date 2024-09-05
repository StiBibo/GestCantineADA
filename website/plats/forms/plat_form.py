from django import forms
from ..models.plats_model import PlatModel


class PlatForm(forms.ModelForm):
    class Meta :
        model = PlatModel
        exclude = ('status',)
        # fields = "__all__" 
 