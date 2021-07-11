"""Project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.views import serve
from django.urls import re_path
from .settings import STATIC_ROOT
from app1.views import hello
# xadmin的依赖
import xadmin

# xversion模块自动注册需要版本控制的 Model
from xadmin.plugins import xversion

xadmin.autodiscover()

xversion.register_models()

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/', xadmin.site.urls),
    path('', hello),
    # path(r'^static/(?P<path>.*)$', serve, {"document_root": STATIC_ROOT}),
]