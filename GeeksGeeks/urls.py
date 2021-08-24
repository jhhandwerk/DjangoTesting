"""GeeksGeeks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from geeks.views import create_view
from geeks.views import test_view
from geeks.views import button_view
from geeks.views import image_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/', create_view ),
    path('test/', test_view ),
   #the code below printed in the log... and the return kept us on the home page (which is 
   # nothing) like in the video)
    path('button/', button_view),
    path('image/', image_view)
    



]
