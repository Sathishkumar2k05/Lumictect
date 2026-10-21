from django.urls import path
from .views import *


urlpatterns = [
    path('dashboard/', dashboard, name="dashboard"),
    path('check_in/', check_in, name='check_in'),
    path('check_out/', check_out, name='check_out'),
]