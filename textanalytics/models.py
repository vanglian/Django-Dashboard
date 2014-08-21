from django.db import models

# Create your models here.
class POStagged(models.Model):
    word = models.CharField(max_length=50)
    pos_tagged = models.CharField(max_length=150)
    def __str__(self):
        return self.word
    
