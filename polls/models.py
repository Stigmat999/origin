# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class LogString(models.Model):	
	ip = models.CharField(max_length=20, default=None)
	method = models.CharField(max_length=20, default=None)
	code = models.IntegerField(default=None)
