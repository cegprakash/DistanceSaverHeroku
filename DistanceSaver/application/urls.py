# pages/urls.py
from django.urls import path

from .views import HomePageView
from .views import DistanceView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path(r'distance', DistanceView.as_view()),

]