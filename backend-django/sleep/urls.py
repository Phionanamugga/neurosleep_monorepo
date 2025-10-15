from django.urls import path
from .views import last_night, nights, journal

urlpatterns = [
    path("metrics/last-night", last_night),
    path("metrics/nights", nights),
    path("journal", journal),
]