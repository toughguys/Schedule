from django.db import models


# Create your models here.
class Client(models.Model):
    full_name = models.CharField(max_length=255)
    password = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=255)


class Service(models.Model):
    name = models.CharField(max_length=255)


class ServiceCategory(models.Model):
    name = models.CharField(max_length=255)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)


class Master(models.Model):
    full_name = models.CharField(max_length=255)
    srvctg = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)


class MastersInformation(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
