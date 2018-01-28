from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^singup/$', views.signup_view, name="signup"),
    url(r'^$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    ]
