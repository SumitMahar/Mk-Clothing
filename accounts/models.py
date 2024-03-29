from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # The first element in each tuple is the actual value to be stored, 
    # and the second element is the human-readable name.
    CHOICES = [
        ('1', 'Yes'),
        ('0', 'No'),
    ]
    home_address = models.CharField(max_length=255, null=True, blank=True)
    are_you_above_18 = models.CharField(
                            max_length=250, 
                            null=True, 
                            blank=True, 
                            choices=CHOICES, 
                            default='1',
                             )
    