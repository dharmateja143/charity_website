from django.db import models

class Visit(models.Model):
    name = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.EmailField()
    time = models.TimeField()
    date = models.DateField()
    purpose = models.TextField()
    def __str__(self):
        return self.name
