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

class Medicine(models.Model):
    Name = models.CharField()
    Manufacturer = models.CharField()
    Cures = models.CharField()
    SideEffects = models.CharField()

class Collection(models.Model):
    Medicine = models.CharField()
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    # Date =
    # Collected =
    CollectedApproved = models.BooleanField(default=False)
    CollectedApprovedBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='approved_by', null=True, blank=True)
