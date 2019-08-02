"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth.views import LoginView
from django.urls import path, include

from core.views import HomeView, CartazView, ReservarView, SelectReservaView, logoutView, CreateUserView

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name=HomeView.name),
    path('cartaz/<str:data>/', CartazView.as_view(), name=CartazView.name),
    path('reservar/<int:pk>/', ReservarView.as_view(), name=ReservarView.name),
    path('reservar/<int:pk>/horario/<int:pk_time>/poltrona/<str:seat>/', SelectReservaView.as_view(), name=SelectReservaView.name),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logoutView, name='logout'),
    path('create-user/', CreateUserView.as_view(), name=CreateUserView.name),
]
