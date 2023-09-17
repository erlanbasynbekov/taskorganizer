from django.contrib import admin
from django.urls import path,include
from task_group import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('task_group.urls')),
]
