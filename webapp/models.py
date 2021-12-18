from django.db import models

class tache (models.Model):
    name_tache= models.CharField(max_length=5)
    time_tache=models.IntegerField()
    predecesseur= models.CharField(max_length=5,blank=True)

    def __str__(self):
        return self.name_tache
