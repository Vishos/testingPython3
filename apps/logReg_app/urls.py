from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$', views.index),
    url(r'^processLogReg$', views.processLogReg),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout)
]