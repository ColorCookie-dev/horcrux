"""horcrux URL Configuration

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
from django.urls import path,include
from django.db.utils import OperationalError
from login.models import User


try:
    org_name = User.objects.filter(is_superuser=True)[0].org.name

    admin.site.site_header = "%s Admin" % org_name
    admin.site.site_title = "%s Admin Portal" % org_name
    admin.site.index_title = "Welcome to %s Portal" % org_name
except OperationalError:
    pass

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
]
