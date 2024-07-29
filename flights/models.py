from django.db import models

class FlightStatus(models.Model):
    flight_number = models.CharField(max_length=10)
    status = models.CharField(max_length=50)
    gate = models.CharField(max_length=10)
    scheduled_time = models.DateTimeField()
    estimated_time = models.DateTimeField()
    notification_sent = models.BooleanField(default=False)

    def __str__(self):
        return f"Flight {self.flight_number}: {self.status}"


