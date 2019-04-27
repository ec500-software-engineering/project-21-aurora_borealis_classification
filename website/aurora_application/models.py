from __future__ import unicode_literals
from django.db import models

class IMG(models.Model):
    img = models.ImageField(upload_to='img')