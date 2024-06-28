from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    BioText = models.TextField(blank=True)
    City = models.CharField(max_length=100)
    DateOfBirth = models.DateField()

    def __str__(self):
        return self.User.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

class Medicine(models.Model):
    Name = models.CharField(max_length=100, blank=True)
    Manufacturer = models.CharField(max_length=100, blank=True)
    Cures = models.CharField(max_length=30, blank=True)
    SideEffects = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.Name

class Collection(models.Model):
    Medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Date = models.DateField()
    Collected = models.BooleanField(default=False)
    CollectedApproved = models.BooleanField(default=False)
    CollectedApprovedBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='approved_collections')

    def __str__(self):
        return f"{self.User.username} - {self.Medicine.Name}"
