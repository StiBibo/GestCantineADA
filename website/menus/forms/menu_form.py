from django import forms
from ..models.menu_models import MenuModel


class MenuForm(forms.ModelForm):
    class Meta :
        model = MenuModel
        exclude = ('status',)
        # fields = "__all__"
