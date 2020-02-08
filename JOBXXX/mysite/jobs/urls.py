from django.urls import path
from. import views
urlpatterns = [
    path('<int:job_id>/', views.detail, name='detail'),
    path('apply/', views.getJob, name='getjob'),
    path('add/', views.addjob, name='addjob'),
    path('dash/', views.dash, name='dash'),
]
