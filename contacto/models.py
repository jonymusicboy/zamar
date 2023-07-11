from django.db import models

# Create your models here.

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=30, null=True)
    asunto = models.CharField(max_length=100, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    contactado = models.BooleanField(default=False)

    def __str__(self):
        return self.name
