from django.db import models

# Create your models here.
class Reel(models.Model):
    name = models.CharField(max_length=20,null=True)
    location = models.CharField(max_length=20,null=True)
    quantity = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self) -> str:
        return self.name