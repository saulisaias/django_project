from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_request, name="signin"),
]
