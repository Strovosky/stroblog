"""stroblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from security import views as security_views
from django.contrib.auth import views as auth_views # We need to import the views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog.urls")),
    path("register/", view=security_views.register, name="signup"),
    # We import each view at a time.
    path("login/", view=auth_views.LoginView.as_view(template_name="security/login.html"), name="login"),
    path("logout/", view=auth_views.LogoutView.as_view(template_name="security/logout.html"), name="logout"),
    path("password-reset/",
    auth_views.PasswordResetView.as_view(template_name="security/password_reset.html"),
    name="reset_password"),
    path("password-reset/done/",
    auth_views.PasswordResetDoneView.as_view(template_name="security/password_reset_done.html"),
    name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/",
    auth_views.PasswordResetConfirmView.as_view(template_name="security/password_reset_confirm.html"),
    name="password_reset_confirm"),
    path("password-reset-complete/",
    auth_views.PasswordResetCompleteView.as_view(template_name="security/password_reset_complete.html"),
    name="password_reset_complete"),
    path("profile/", view=security_views.profile, name="profile")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
