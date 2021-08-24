from django import forms
from .models import GeeksModel
from .models import TestModel
from .models import ImageModel

# creating a form
class GeeksForm(forms.ModelForm):

	# create meta class
	class Meta:
		# specify model to be used
		model = GeeksModel

		# specify fields to be used
		fields = [
			"title",
			"description",
		]

class TestForm(forms.ModelForm):

	# create meta class
	class Meta:
		# specify model to be used
		model = TestModel

		# specify fields to be used
		fields = [
			"kanji",
			"reading",
		]
	
class ImageForm(forms.ModelForm):

	# create meta class
	class Meta:
		# specify model to be used
		model = ImageModel

		# specify fields to be used
		fields = [
			"Opinion",
			"Score",
		]

