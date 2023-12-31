from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.decorators.cache import never_cache

from main.views import set_is_active
from users.apps import UsersConfig
from users.views import ProfileUpdateView, RegisterView, activate_user, page_after_registration, generate_new_password

app_name = UsersConfig.name


urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', never_cache(ProfileUpdateView.as_view()), name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('activate/<str:token>/', activate_user, name='activate'),
    path('page_after_registration/<str:token>/', page_after_registration, name='page_after_registration'),
    path('profile/genpassword', generate_new_password, name='generate_new_password')
]
