from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.accounts.urls',namespace="accounts")),
    url(r'^login', include('apps.login.urls', namespace="login")),
    url(r'^home/', include('apps.home.urls', namespace="home")),
]


#url('', login, {'template_name' : 'login/login.html'}, name="login"),
