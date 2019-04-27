from __future__ import unicode_literals
from django.db import models

class Img(models.Model):
    img_url = models.ImageField(upload_to='img')