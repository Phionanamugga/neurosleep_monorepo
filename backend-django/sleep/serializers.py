# sleep/serializers.py
from rest_framework import serializers
from .models import SleepSession, JournalEntry

class SleepSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SleepSession
        fields = "__all__"  # serialize all fields in the model


class JournalEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalEntry
        fields = "__all__"
