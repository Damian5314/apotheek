from django.db import models


# Create your models here.
class Profile(models.Model):
    #User = models.OneToOneField(User, on_delete=models.CASCADE)
    BioText = models.TextField()
    City = models.CharField(max_length=100)
    DateOfBirth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.User.username
    
#class Medicine(models.Model):
    #Name = 
    #Manufacturer = 
    #Cures = 
    #SideEffects = 

#class Collection(models.Model):
    #Medicine = 
    #User = 
    #Date = 
    #Collected = 
    #CollectedApproved = 
    #CollectedApprovedBy = 