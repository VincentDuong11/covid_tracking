"""[Author: Chanh Duong. Student number: 040-681-356]
    """
from django.db import models

"""[Config Object model to be store in db]
    """


class Record(models.Model):
    pruid = models.IntegerField()
    prname = models.CharField(max_length=150)
    prnameFR = models.CharField(max_length=150)
    date = models.DateField(null=True)
    numconf = models.IntegerField()
    numprob = models.IntegerField()
    numdeaths = models.IntegerField()
    numtotal = models.IntegerField()
    numtoday = models.IntegerField()
    ratetotal = models.FloatField()

    # def __str__(self):
    #     template = ' {0.pruid} {0.prname}'
    #     return template.format(self)
    def __str__(self):
        return  self.prname