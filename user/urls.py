from django.urls import path
from .views import RegisterView, LoginView, ChangePasswordView, ProfileView, ChangeUserRoleView, LogoutView, CheckAuthView




urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('change-role/<int:user_id>/', ChangeUserRoleView.as_view(), name='change-user-role'),
    path('status/', CheckAuthView.as_view(), name='status'),
    path('logout/', LogoutView.as_view(), name='logout'),

]





