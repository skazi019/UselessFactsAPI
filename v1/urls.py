from django.urls import path

from .views import FactView, FactIDView, HomepageView

urlpatterns = [
    path("", HomepageView.as_view(), name="home"),
    path("random-fact/", FactView.as_view()),
    path("fact/<int:id>/", FactIDView.as_view()),
]
