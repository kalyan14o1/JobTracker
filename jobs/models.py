from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    application_date = models.DateField('application date')
    status = models.CharField(max_length=50, choices=[
        ('Applied', 'Applied'),
        ('Interview', 'Interview'),
        ('Offer', 'Offer'),
        ('Rejected', 'Rejected')
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company + " - " + self.position
        
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name