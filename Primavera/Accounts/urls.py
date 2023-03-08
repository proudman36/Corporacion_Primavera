from django.urls import path

from django.contrib.auth import views as auth_views

from django.contrib.auth.views import LoginView,LogoutView

from . import views

app_name = 'Accounts'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',LoginView.as_view(template_name='registration/login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='exit/logout.html'),name='logout'),
    path('reset_password/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete')
]


