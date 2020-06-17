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
from . import views,testdb,search,search2,submit
from django.contrib import admin
from CurriculumDesign import MyEcharts
from CurriculumDesign import votes
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^search-form$', search.search_form),
    # url(r'^search$', search.search),
    # url(r'^search-post$', search2.search_post),
    url(r'^submit$', submit.submit_form, name='submit'),
    url(r'^submit-info$', submit.submit_to_mysql),
    url(r'^index$', views.index),
    url(r'^rank$', MyEcharts.index, name='index'),
    url(r'^votes$', votes.submit_votes),
    url(r'^votes-info$', votes.get_info),
]