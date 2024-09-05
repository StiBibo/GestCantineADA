from django.db import models
from base.models.helpers.date_time_models import DateTimeModel
from plats.models.plats_model import PlatModel


class MenuModel(DateTimeModel):

    # Relation One to One with PlatModel
    plat = models.OneToOneField(PlatModel, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.creation_date