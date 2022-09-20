from django.db import models
# from django.contrib.auth.models import User

class Usertask(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    isDone = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-id']

    def __str__(self) -> str:
        return self.name

# class Username(models.Model):
#     name = models.CharField(max_length=100)
#     password1 = models.CharField(max_length=100)
#     password2 = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name
