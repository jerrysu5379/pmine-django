"""
URL configuration for pmine project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.i18n import i18n_patterns 
from django.urls import path, include 

urlpatterns = [ 
    path('admin/', admin.site.urls), 

    # Index pages 
    path('', include("index.urls")), 
    path('index/', include("index.urls")), 

    # Static operations 
    path('static/', include("op.urls")), 
    path('op/', include("op.urls")), 

    # Apps 
    path('skincomp/', include("peskincomp.urls")), 
    path('skinview/', include("skinview.urls")), 
    path('bbcode/', include("bbcodetemp.urls")), 
    path('uuid/', include("uuidgen.urls")), 
    path('maths/', include("maths.urls")), 
    path('viewmd/', include("viewmarkdown.urls")), 
] 

localized_patterns = [
    # Index pages 
    path('', include("index.urls")), 
    path('index/', include("index.urls")), 

    # Static operations 
    path('static/', include("op.urls")), 
    path('op/', include("op.urls")), 

    # Apps 
    path('skincomp/', include("peskincomp.urls")), 
    path('skinview/', include("skinview.urls")), 
    path('bbcode/', include("bbcodetemp.urls")), 
    path('uuid/', include("uuidgen.urls")), 
    path('maths/', include("maths.urls")), 
    path('viewmd/', include("viewmarkdown.urls")), 
] 

urlpatterns += i18n_patterns(*localized_patterns) 