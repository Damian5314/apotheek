from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    BioText = models.TextField()
    City = models.CharField(max_length=100)
    DateOfBirth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.User.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# class Medicine(models.Model):
    # Name =
    # Manufacturer =
    # Cures =
    # SideEffects =

# class Collection(models.Model):
    # Medicine =
    # User =
    # Date =
    # Collected =
    # CollectedApproved =
    # CollectedApprovedBy =
