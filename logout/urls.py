from django.urls import path
from . import views

urlpatterns = [
    path('', views.logout_request, name="logout"),
]
