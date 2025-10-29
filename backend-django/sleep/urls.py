# sleep/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SleepSessionViewSet, JournalEntryViewSet

router = DefaultRouter()
router.register(r'sleep-sessions', SleepSessionViewSet, basename='sleep-session')
router.register(r'journal-entries', JournalEntryViewSet, basename='journal-entry')

urlpatterns = [
    path('', include(router.urls)),
]
