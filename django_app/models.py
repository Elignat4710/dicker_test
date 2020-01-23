from django.db import models


class MySimpleModel(models.Model):
    text = models.CharField(max_length=200)
