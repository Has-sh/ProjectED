from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login, name='login'),
    path('student/signup/', views.student_signup, name='student-signup'),
    path('sign-out', views.sign_out, name='sign_out'),
    path('auth-receiver', views.auth_receiver, name='auth_receiver'),
    path('tutor/signup/', views.tutor_signup, name='tutor-signup'),

]