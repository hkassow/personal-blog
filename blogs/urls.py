from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('emailFunc', views.emailFunction, name='emailTrial'),
]