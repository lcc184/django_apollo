from apollo import views
from django.urls import path

urlpatterns = [
    path('index/', views.index), # 配置访问首页的路径
    path('safe_a/', views.safe_a), # 配置访问a等级安全的路由配置路径
]
