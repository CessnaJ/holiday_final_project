"""final_project_back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from . import views


app_name = 'community'
urlpatterns = [
    # path('', views.index),
    # path('<int:article_id>/', views.comment),
    # 이 아래부터는 복붙임.
    # path('articles/', views.article_list),
    # path('articles/<int:article_pk>/', views.article_detail),
    # path('comments/', views.comment_list),
    # path('comments/<int:comment_pk>/', views.comment_detail),
    # path('articles/<int:article_pk>/comments/', views.comment_create),
    path('', views.article_list),
    path('create/', views.article_create), # 새 글 생성
    path('delete/<int:article_pk>/', views.article_delete), # 글 삭제
    path('<int:article_pk>/', views.article_detail),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('<int:article_pk>/comments/', views.comment_create),
]



# router = routers.DefaultRouter()
# router.register(r'posts', PostViewSet)

# urlpatterns = [
#     path("", include(router.urls)),
# ]
