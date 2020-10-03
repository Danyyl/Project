"""BackEnd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from Server import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('api/registration/', views.Register.as_view(), name='Registretion'),
    path('api/profile/', views.ProfileView.as_view(), name='Profile'),
    path('api/session/', views.SessionView.as_view(), name='Session'),
    path('api/specialization/', views.SpecializationView.as_view(), name='Specialization'),
    path('api/all_session/', views.SessionListView.as_view(), name='SessionList'),
    path('api/message/', views.MessageView.as_view(), name='Message'),
    path('api/messages/', views.MessageListView.as_view(), name='Messages'),
    path('api/task/', views.TaskView.as_view(), name='Task'),
    path('api/tasks/', views.AllTaskView.as_view(), name='All_tasks'),
    path('api/tasklist/', views.TaskListView.as_view(), name='TaskList'),
    path('api/candidates/', views.CandidateView.as_view(), name='Candidate'),
    path('api/candidatesession/', views.SessionCandidateListView.as_view(), name='Candidate_session'),
    path('api/candidatetask/', views.CandidateTaskView.as_view(), name='Candidate_session'),
    path('api/getsession/', views.GETSessionView.as_view(), name='Get_session'),



]
