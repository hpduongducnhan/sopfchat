from django.db import models

# Create your models here.

class FchatWebsite(models.Model):
    ENVIRONMENT_CHOICES = (
        ('DEV', 'Development'),
        ('STG', 'Staging'),
        ('UAT', 'UAT'),
        ('PRO', 'Production'),
    )

    name = models.CharField(max_length=100)
    description = models.TextField()
    environment = models.CharField(max_length=3, choices=ENVIRONMENT_CHOICES)
    scripts = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    