"""nethragunti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from about.views import home, sections, ssl

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('sections/',sections, name='sections'),
    path('.well-known/acme-challenge/Ic_uyTPJhB9Q8Vqv2OIm_QV94tlJo-D59n9pWof4lzc', ssl, name="ssl")
]
