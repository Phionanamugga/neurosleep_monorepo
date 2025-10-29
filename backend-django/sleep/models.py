from django.db import models

class SleepSession(models.Model):
    duration_min = models.IntegerField()
    efficiency = models.FloatField()
    latency = models.FloatField(help_text="Minutes to fall asleep")
    rem_hours = models.FloatField()
    deep_hours = models.FloatField()
    hrv = models.FloatField(help_text="Heart rate variability")
    rhr = models.FloatField(help_text="Resting heart rate")
    score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SleepSession on {self.created_at.date()} (Score: {self.score})"


class JournalEntry(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Journal entry {self.id} on {self.created_at.date()}"
