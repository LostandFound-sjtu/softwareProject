from django.urls import path
from . import views

urlpatterns = [

    # Lost
    path('lost/', views.lost, name="lost"),
]
