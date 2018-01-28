from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include ('apps.accounts.urls'),
    path('login/',include ('apps.login.urls', namespace="login")),
    path('home/', include ('apps.home.urls', namespace="home")),
    path('', login, {'template_name' : 'login/login.html'}, name="login"),
    url(r'^accounts/', include('apps.accounts.urls')),
]
