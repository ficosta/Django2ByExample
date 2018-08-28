from django.urls import path
form . import views

urlpatterns = [
	path('login/', views.user_login, name='login'),
]