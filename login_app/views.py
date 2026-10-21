from django.shortcuts import render, redirect
from .models import Attendance
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.decorators import login_required



@login_required
def dashboard(request):

    today = datetime.now().date()

    attendance = Attendance.objects.filter(
        user = request.user, 
        date = today
    ).first()

    return render(request, "dashboard.html", {'attendance':attendance})

@login_required
def check_in(request):

    if request.method == "POST":

        attendance = Attendance.objects.filter(
            user = request.user,
            date = datetime.now().date()).first()

        if attendance is None:

            Attendance.objects.create(
                user = request.user,
                employee_id = request.user.username,
                date = datetime.now().date(), 
                check_in = timezone.now()
            )
    
        return redirect('dashboard')

@login_required
def check_out(request):

    if request.method == "POST":

        attendance = Attendance.objects.filter(
            user = request.user,
            date = datetime.now().date(), 
            check_out__isnull = True).first()

        if attendance:

            attendance.check_out = datetime.now()

            duration = attendance.check_out - attendance.check_in

            hours = duration.seconds // 3600
            minutes = (duration.seconds % 3600) // 60

            attendance.total_working_hours = f"{hours} hours {minutes} minutes"

            attendance.save()

        return redirect('dashboard')