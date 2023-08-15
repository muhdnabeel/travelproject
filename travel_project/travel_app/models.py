from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

class team(models.Model):
    name2=models.CharField(max_length=200)
    img2=models.ImageField(upload_to='pics')
    desc2=models.TextField()
    
    

