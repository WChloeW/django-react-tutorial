from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    # 这里是主路由
]