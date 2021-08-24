# import the standard Django Model
# from built-in library
from django.db import models

# declare a new model with a name "GeeksModel"
class GeeksModel(models.Model):

	# fields of the model
	title = models.CharField(max_length = 200)
	description = models.TextField()

	# renames the instances of the model
	# with their title name
	def __str__(self):
		return self.title

class TestModel(models.Model):
    kanji =models.CharField(max_length=100)
    reading = models.CharField(max_length=100)

class ImageModel(models.Model):
	Opinion = models.CharField(max_length=100)
	Score = models.CharField(max_length=100)
    
    

	

    


