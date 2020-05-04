from django.db import models


class Feedback(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField(default=5)

    company = models.CharField(max_length=100,null=False)
    Product = models.IntegerField(default=1)
    Service = models.IntegerField(default=1)
    Employee = models.IntegerField(default=1)
    Value = models.IntegerField(default=1)
    Recommendable = models.IntegerField(default=1)
    review = models.TextField(blank=True)

    def __str__(self):
        return self.company

# Create your models here.
