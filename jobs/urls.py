from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('detail/<int:id>', views.job_detail, name='job_detail'),
]