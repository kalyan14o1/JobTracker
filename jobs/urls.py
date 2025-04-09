from django.urls import path
from . import views

app_name = 'jobs'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:job_id>/', views.show, name='show'),
    path('add/', views.create, name='create'),
    path('edit/<int:job_id>/', views.update, name='update'),
    path('delete/<int:job_id>/', views.delete, name='delete'),
    path('profile/', views.profile, name='profile'), 
]