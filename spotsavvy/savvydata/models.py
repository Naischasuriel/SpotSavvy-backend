from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
    
class Review(models.Model):
    user = models.ForeignKey(Userprofile, on_delete=models.CASCADE)
    rating = models.IntegerField()
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  f"Review by {self.user.user.username} at {self.timestamp}"