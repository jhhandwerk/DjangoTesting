from django.contrib import admin

from .models import GeeksModel
from .models import TestModel
from .models import ImageModel



# Register your models here.
admin.site.register(GeeksModel)
admin.site.register(TestModel)
admin.site.register(ImageModel)
