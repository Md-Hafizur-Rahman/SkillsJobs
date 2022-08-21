from django.urls import path

from apps.frontend import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]