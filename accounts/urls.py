from django.urls import include, path
from django.contrib.auth.views import LoginView
from . import views


urlpatterns = [
    path('login-custom/', LoginView.as_view()),
    path('', include('django.contrib.auth.urls')),
    path("register/", views.register_request, name="register")

]