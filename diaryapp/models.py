from django.db import models

# Create your models here.

class Diary(models.Model):
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    body=models.TextField()

    def __str__(self):
        return self.title

    def slice(self):
        return self.body[:50]