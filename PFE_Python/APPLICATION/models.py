from django.db import models
class utilisateur(models.Model):
    username = models.CharField(max_length=50)
    mdp = models.CharField(max_length=50)


