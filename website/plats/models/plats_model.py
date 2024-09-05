from django.db import models
from base.models.helpers.name_date_time import NamedDateTimeModel

class PlatModel(NamedDateTimeModel):
    summary = models.CharField(max_length=255)