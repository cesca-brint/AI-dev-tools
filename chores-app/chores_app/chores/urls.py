from django.urls import path
from . import views
from .forms_chores import AssignmentForm, ChoreForm

urlpatterns = [
       path('', views.home, name='home'),
       path('chores/', views.chores_list, name='chores_list'),
       path('chores/add/', views.add_chore, name='add_chore'),
       path('chores/update/<int:assignment_id>/', views.update_reminders, name='update_reminders'),
       path('calendar/', views.calendar, name='calendar'),
       path('settings/', views.settings, name='settings'),
       path('leaderboard/', views.leaderboard, name='leaderboard'),
   ]