from django.db import models


class BaseModel(models.Model):
    """Base abstract timestamped model"""
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True
