from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('clock-in', views.clock_in, name='clock_in'),
    path('clock-out', views.clock_out, name='clock_out'),
    path('timesheet', views.timesheet, name='time_sheet'),
    path('timeclock/update/<int:pk>/', views.UpdateTimeClock, name='update_timeclock')
]
