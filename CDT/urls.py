from django.urls import include, re_path
from CDT import view

urlpatterns = [
    re_path('^index/$', view.index),
    re_path('^sketch/$', view.sketch),
    re_path('^save/$', view.save),
]
