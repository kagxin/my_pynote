from django.conf.urls import url, include
from app import views

urlpatterns = [
    url(r'^test', views.TestView.as_view())
]
