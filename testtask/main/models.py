from django.db import models

class Users(models.Model):
    
    name = models.CharField(blank=True, null=True, max_length=255)
    secondName = models.CharField(blank=True, null=True, max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'users'