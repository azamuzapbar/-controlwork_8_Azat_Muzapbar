from django.urls import path

from accounts.views import LoginView, logout_view, RegisterView, ProfileView, UserChangeView

from accounts.views import UserPasswordChangeView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/change', UserChangeView.as_view(), name='change'),
    path('logout/', logout_view, name='logout'),
    path('<int:pk>/password_change', UserPasswordChangeView.as_view(), name='password_change')
]