from django.conf.urls import url

from . import views

app_name = "operation"

urlpatterns = [
    url(r'^userfav/$', views.UserFavListView.as_view(), name="userfav_list"),
    url(r'^userfav/(?P<goods_id>\d+)/$', views.UserFavDetailView.as_view(), name="userfav_detail"),
    url(r'^message/$', views.LeavingMessageListView.as_view(), name="message_list"),
    url(r'^message/create/$', views.LeavingMessageCreateView.as_view(), name="message_create"),
    url(r'^message/remove/(?P<pk>\d+)/$', views.LeavingMessageRemoveView.as_view(), name="message_remove"),
    url('^address/$', views.AddressListView.as_view(), name="address_list"),
    url('^address/create/$', views.AddressCreateView.as_view(), name="address_create"),
    url('^address/(?P<pk>\d+)/$', views.AddressDetailView.as_view(), name="address_detail"),
    url('^address/update/(?P<pk>\d+)/$', views.AddressUpdateView.as_view(), name="address_update"),
    url('^address/remove/(?P<pk>\d+)/$', views.AddressRemoveView.as_view(), name="address_remove"),
]
