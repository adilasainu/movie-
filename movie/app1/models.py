from django.db import models

# Create your models here.
from django.db import models

class Movie(models.Model):   #table definition
    title=models.CharField(max_length=20)
    description=models.TextField()
    year=models.IntegerField()
    language=models.CharField(max_length=20)
    image=models.ImageField(upload_to='img',blank=True,null=True)

    def _str_(self):
        return self.title
