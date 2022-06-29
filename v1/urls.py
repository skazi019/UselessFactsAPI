from django.urls import path

from .views import FactView, FactIDView, homepage

urlpatterns = [
    path("", homepage, name="home"),
    path("v1/random-fact/", FactView.as_view()),
    path("v1/fact/<int:id>/", FactIDView.as_view()),
]
