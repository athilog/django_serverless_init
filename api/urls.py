

from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from . import views
import inspect


urlpatterns = [
    # 동사형태 api
    path("", views.UserAPIView.as_view()),
    path("user/", views.UserAPIView.as_view()),
]

