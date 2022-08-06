from django.urls import path, include
from .router import router
from django.contrib import admin

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls)

]
