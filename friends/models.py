from django.db import models

# Create your models here.

class Friend(models.Model):
    firstname = models.CharField(max_length = 20)
    lastname = models.CharField(max_length = 20)
    date_of_birth = models.DateField(help_text = "DD/MM/YYYY")
    mobile_no = models.CharField(max_length = 10)
    address = models.TextField(max_length = 255)
    OCCUPTION_CHOICE = (
        ('private_job', 'Private Job'),
        ('gov_job', 'Goverment Job'),
        ('businessman', 'Businessman')
    )
    occupation = models.CharField(max_length = 20,choices = OCCUPTION_CHOICE)
