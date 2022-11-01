from django.db import models
# from django.contrib.auth.models import User

class Username(models.Model):
    name = models.CharField(max_length=100)
    password = models.IntegerField()

    def __str__(self):
        return self.name

class Usertask(models.Model):
    user = models.ForeignKey(Username, on_delete=models.CASCADE, related_name='task')
    name = models.CharField(max_length=100)
    isDone = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-id']

    def __str__(self) -> str:
        return self.name

