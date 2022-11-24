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
from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index), # 이거 쓸 일 없음. 6600개 조회될것임. 검색위해서 제거.
    path('<int:movie_id>/', views.detail), # 영화 상세페이지
    path('rating/<int:movie_id>/', views.rating), # 평점/댓글 먹이기
    path('like/<int:movie_id>/', views.like), # 영화 좋아요
    path('popular/', views.popular), # 유명한 영화 10개 받아오기.
    path('latest/', views.latest), # 개봉일최근순, 평점 7점이상
    path('randomyear/<int:year>/', views.randomyear),
    path('search/', views.search, name='search'), # 검색창에 input먹을때마다 get요청보내서 받아오기.
    #  path('movies/genre/<int:genre_id>/', views.movie_genre),

]

