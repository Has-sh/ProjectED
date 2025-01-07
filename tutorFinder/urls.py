from django.urls import path
from . import views
urlpatterns = [
    path('', views.find_tutors, name='find_tutors'),
    path('tutor-matcher', views.tutor_matcher, name='tutor_matcher'),
]