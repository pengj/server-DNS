from django.db import models

# Create your models here.
class dsmapping(models.Model):
    pname = models.CharField(max_length=50)
    sip = models.CharField(max_length=20)
    cdate = models.DateTimeField('date created')

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.pname