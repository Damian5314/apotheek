from django.contrib import admin
from .models import Profile, Medicine, Collection

# Register your models here.
admin.site.register(Profile)
admin.site.register(Medicine)
admin.site.register(Collection)