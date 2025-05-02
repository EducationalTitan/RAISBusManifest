from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.manifest_form, name='manifest_form'),
    path('home/', views.home, name='home'),
    path('list/', views.manifest_list, name='manifest_list'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='manifest/login.html'), name='login'),

    # other paths...
]
