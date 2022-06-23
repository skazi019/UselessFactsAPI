from django.urls import path

from .views import FactView, FactIDView

urlpatterns = [
    path("random-fact/", FactView.as_view()),
    path("fact/<int:id>/", FactIDView.as_view()),
]
