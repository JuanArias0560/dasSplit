from django.urls import path
from . import views

app_name="split"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register/",views.register_request, name="register"),
]