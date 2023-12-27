from django.db import models

# Create your models here.


class News(models.Model):

    title = models.CharField(max_length=150)
    date = models.DateTimeField()
    image = models.ImageField(default="default.png",upload_to="uploads/")  #file will be uploaded to media root /uploads
    username = models.CharField(max_length=20)
    description = models.CharField(max_length=2000)

    def __str__(self):
        return self.title
