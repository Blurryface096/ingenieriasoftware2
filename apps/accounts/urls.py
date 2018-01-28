from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^singup/$', views.signup, name="signup"),
    url(r'^login/$', views.login, name="login"),
    url(r'^logout/$', views.logout, name="logout"),
    ]
