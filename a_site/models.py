from django.db import models

# Create your models here.


class Wishes(models.Model):
	name = models.CharField(max_length=50)
	w_text = models.CharField(max_length=1000)	
	idate = models.DateTimeField('insertedtime')
	def __str__(self):
		return self.w_text

class Questions(models.Model):
	question=models.CharField(max_length=50)

class Answer(models.CharField):
	ans = models.CharField(max_length=200)
	qn = models.ForeignKey('Question',on_delete=models.DO_NOTHING,default="")

