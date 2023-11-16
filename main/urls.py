from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.ChallengeListView.as_view(), name='home'),
    path('running', views.ChallengeListView.as_view(), name='running'),
    path('upcoming/', views.challenge_list_view_upcoming, name='upcoming'),
    path('expired/', views.challenge_list_view_expired, name='expired'),
    path('search/', views.challenge_list_view_searching, name='search'),
    # path('challenge', views.challenge, name="challenge"),
    path('calendar', views.calendar, name="calendar"),
    path('login', views.userLogin, name="login"),
    path('user_logout', views.user_logout, name="logout"),
]
