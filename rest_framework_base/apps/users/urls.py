from django.conf.urls import url

from . import views

app_name = "users"

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.UserDetailView.as_view(), name="user_detail"),
    url(r'^(?P<pk>\d+)/update/$', views.UserUpdateView.as_view(), name="user_update"),
    url(r'^register/$', views.UserRegisterView.as_view(), name="user_register"),
    url(r'^smscode/$', views.SmsCodeView.as_view(), name="sms_code"),
]
