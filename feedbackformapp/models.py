from django.db import models

class feedback(models.Model):
    name = models.CharField(max_length=100,null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Create your models here.
