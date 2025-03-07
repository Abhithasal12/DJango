from django.db import models

#makemigration- create change and store in a file
    #migrate - apply the pending changes created by makemigration

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField(null=True, blank=True)
    date = models.DateField()

    def __str__(self):
        return self.name