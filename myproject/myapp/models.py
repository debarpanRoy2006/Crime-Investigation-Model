

from django.db import models

class Passenger(models.Model):
    pclass = models.IntegerField()
    sex = models.IntegerField()  # 0 for male, 1 for female
    age = models.FloatField()
    sibsp = models.IntegerField()
    parch = models.IntegerField()
    fare = models.FloatField()
    embarked_c = models.IntegerField()
    embarked_q = models.IntegerField()
    embarked_s = models.IntegerField()
    survived = models.IntegerField()
    
    def __str__(self):
        return f"Passenger {self.id}"
