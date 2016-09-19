from __future__ import unicode_literals
from django.db import models

class Secret(models.Model):
	secret = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)

class Like(models.Model):
	secret = models.ForeignKey(Secret, related_name="likessecret")
	created_at = models.DateTimeField(auto_now_add = True)	