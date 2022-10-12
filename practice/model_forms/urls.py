from django.urls import path
from . import views

app_name = "model_forms"
urlpatterns = [
    path("register/", views.register, name="register"),
]