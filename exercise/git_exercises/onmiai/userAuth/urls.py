from django.conf.urls import url
from .views import login, logout

app_name = "userAuth"

urlpatterns = [
    url(r'^login/$', login, name="login"),
    url(r'^logout/$', logout, name="logout"),
]