from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True



class OrderModel(models.Model):
    order = models.IntegerField()

    class Meta:
        abstract = True


class ActiveModel(models.Model):
    active = models.BooleanField(default=True)


    class Meta:
        abstract = True