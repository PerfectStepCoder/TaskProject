from django.db import models


class User(models.Model):
    name = models.CharField(max_length=512, unique=True)
    email = models.EmailField()
    type = models.CharField(max_length=512)
    password = models.CharField(max_length=1024)
    authenticated = models.BooleanField(default=False)

    class Meta(object):
        ordering = ['name', 'email']

    def __str__(self):
        return ";".join([self.name, self.email, self.type])

