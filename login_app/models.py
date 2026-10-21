from django.db import models
from django.conf import settings

class Attendance(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20)
    date = models.DateField()
    check_in = models.DateTimeField(null=True, blank=True)
    check_out = models.DateTimeField(null=True, blank=True)
    total_working_hours = models.CharField(max_length=20, null=True, blank=True)