from django.conf.urls import url, include
from visitor import views

app_name = "visitor"

urlpatterns = [
    # url(r'^$', views.index, name="index"),
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^comment/$', views.post_comment, name="comment")
]