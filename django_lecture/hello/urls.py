from django.urls import path
from . import views

urlpatterns = [ 
    path("", views.index, name="index"),
    path("monique", views.monique, name="monique"),
    path("<str:name>", views.greet, name="greet")
]
