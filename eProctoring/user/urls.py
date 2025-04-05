from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("home/", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path('accounts/', include('django.contrib.auth.urls')),
    path("demo/", views.demo_view, name="demo"),
    # path("profile_page/", views.profile_view, name="profile_page", kwargs={'username': 'username'}),
    path("profile/", views.profile_view, name="profile"),
    path("logout/", views.logout_view, name="logout"),
]