from django.urls import path
from . import views
urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('job/new/', views.job_create, name='job_create'),
    path('job/<int:pk>/', views.job_detail, name='job_detail'),
    path('job/<int:pk>/edit/', views.job_update, name='job_update'),
    path('job/<int:pk>/delete/', views.job_delete, name='job_delete'),
    path('job/<int:pk>/apply/', views.apply_job, name='apply_job'),
    path('my-jobs/', views.my_jobs, name='my_jobs'),
    path('job/<int:pk>/applications/', views.job_applications, name='job_applications'),
    path('my-applications/', views.my_applications, name='my_applications'),
]