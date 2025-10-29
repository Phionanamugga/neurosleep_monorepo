from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import SleepSession, JournalEntry
from .serializers import SleepSessionSerializer, JournalEntrySerializer

from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

class SleepSessionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing sleep sessions.
    Supports GET, POST, PUT, PATCH, DELETE.
    """
    queryset = SleepSession.objects.all().order_by('-created_at')
    serializer_class = SleepSessionSerializer


class JournalEntryViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing journal entries.
    Supports GET, POST, PUT, PATCH, DELETE.
    """
    queryset = JournalEntry.objects.all().order_by('-created_at')
    serializer_class = JournalEntrySerializer


@api_view(['GET'])
def api_overview(request):
    """
    Simple endpoint to display all available API routes.
    """
    api_urls = {
        'List Sleep Sessions': '/api/sleep-sessions/',
        'Add Sleep Session': '/api/sleep-sessions/',
        'Get/Update/Delete Sleep Session': '/api/sleep-sessions/<id>/',
        'List Journal Entries': '/api/journal-entries/',
        'Add Journal Entry': '/api/journal-entries/',
        'Get/Update/Delete Journal Entry': '/api/journal-entries/<id>/',
    }
    return Response(api_urls)



