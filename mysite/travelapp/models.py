from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    des=models.TextField()

    def __str__(self):
        return self.name


class team(models.Model):
    name1=models.CharField(max_length=100)
    img1=models.ImageField(upload_to='pics')
    des1=models.TextField()


    def __str__(self):
        return self.name1
