from django.db import models

class Job(models.Model):
    STATUS_CHOICES = (
        ('applied', 'Applied'),
        ('interview', 'Interviewing'),
        ('offer', 'Offer'),
        ('rejected', 'Rejected'),
    )
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    application_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.company} - {self.position}"

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name