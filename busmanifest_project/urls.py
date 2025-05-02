from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from manifest.views import homepage_view

urlpatterns = [
    path('', homepage_view, name='homepage'),
    path('admin/', admin.site.urls),
    path('home/', homepage_view, name='home'),  # Enables /home  # Home page view
    path('manifest/', include('manifest.urls')),  # Routes like /manifest/list/
    path('login/', auth_views.LoginView.as_view(template_name='manifest/login.html'), name='login'),
]
