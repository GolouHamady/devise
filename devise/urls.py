from django.contrib import admin
from django.urls import path

from blog.views import dashboard, redirect_index

urlpatterns = [
    path("", redirect_index),
    path("days=<int:days_range>&currencies=<str:currencies>", dashboard, name='home'),
    path('admin/', admin.site.urls),
]