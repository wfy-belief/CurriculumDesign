"""mysite URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from CurriculumDesign import MyEcharts,Submit,Votes
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^submit$', Submit.submit_form,),
    url(r'^submit-info$', Submit.submit_to_mysql),
    url(r'^rank$', MyEcharts.index,),
    url(r'^votes$', Votes.submit_votes),
    url(r'^votes-info$', Votes.get_info),
]