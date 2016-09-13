from django.db import models

# Create your models here.
class Complaint(models.Model):
	GENDER_CHOICES = (('Admit','admit'),('Staff','staff'),('Facilities','facilities'),('Other','other'))
	id = models.AutoField(primary_key = True)
	title = models.CharField(max_length=233,blank=True)
	body = models.TextField()
	category = models.CharField(max_length=34,blank=True, choices=GENDER_CHOICES)
	user_name = models.CharField(max_length=40,blank=True)
	emailid  = models.CharField(max_length=40,blank=True)



	def __str__(self):
		return self.title
		