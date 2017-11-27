# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
import webcam.admin # needed to show the right widget in the admin
from webcam.fields import CameraField

class Person(models.Model):
    picture = CameraField()
