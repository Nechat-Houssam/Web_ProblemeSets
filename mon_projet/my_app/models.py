from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Quote(models.Model):
    content = models.TextField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.content