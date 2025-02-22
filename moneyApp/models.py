from django.db import models

# Create your models here.
class Statement(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()

    choice = (
        ('income','รายรับ'),
        ('expense','รายจ่าย')
    )

    catagory = models.CharField(max_length=10,choices=choice,default=1)
    
    def __str__(self):
        return self.name + "|" + str(self.amount) + "|" + self.catagory