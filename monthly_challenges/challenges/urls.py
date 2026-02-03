from django.urls import path
from . import views
urlpatterns = [
    # this tells django which view corresponds to which path (means if the path is january it will call the view index)
    path("<int:aaa>", views.month_by_number),
    path("<str:aaa>", views.month),
    path("", views.index),


    # path("january", views.janview),
    # path("february", views.febview),
    # path("march", views.marview),
    # path("april", views.aprview),
    # path("may", views.mayview),
    # path("june", views.junview),
    # path("july", views.julview),
    # path("august", views.augview),
    # path("september", views.sepview),
    # path("october", views.octview),
    # path("november", views.novview),
    # path("december", views.decview),
]
