from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User,
        related_name='profile',
        on_delete=models.CASCADE)

    uinfin = models.CharField(max_length=9, blank=True)
    sex  = models.CharField(max_length=6, blank=True)
    race = models.CharField(max_length=15, blank=True)
    nationality  = models.CharField(max_length=15, blank=True)
    dob  = models.DateField(blank=True, null=True)
    mobile  = models.CharField(max_length=15, blank=True)
    housetype = models.CharField(max_length=15, blank=True)
    address_block = models.CharField(max_length=10, blank=True)
    address_street = models.CharField(max_length=100, blank=True)
    address_building = models.CharField(max_length=100, blank=True)
    address_floor = models.CharField(max_length=5, blank=True)
    address_unit = models.CharField(max_length=5, blank=True)
    postal = models.CharField(max_length=10, blank=True)


@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()