from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),           # Home page
    path('signup/', views.signup, name='signup'), # Signup page
    path('login/', views.login_view, name='login'), # Login page
    path('logout/', views.logout_view, name='logout'),

]

