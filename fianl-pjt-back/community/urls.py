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
    path('', views.article_list), # get이면 리스트보여줌(article list), post면 새 글 생성(article create)
    # path('create/', views.article_create), # 새 글 생성
    # path('delete/<int:article_pk>/', views.article_delete), # 글 삭제
    path('<int:article_pk>/', views.article_detail), # get이면 글정보 보여줌, put이면 수정요청. delete면 글 삭제
    path('comments/', views.comment_list), # get으로 다 보내기
    path('comments/<int:comment_pk>/', views.comment_detail), # get으로 해당 댓글만, delete로 댓글삭제, put으로 수정완료요청
    path('<int:article_pk>/comments/', views.comment_create), # article_pk 달아서 post보내면 코멘트 생성됨.
]



# router = routers.DefaultRouter()
# router.register(r'posts', PostViewSet)

# urlpatterns = [
#     path("", include(router.urls)),
# ]
