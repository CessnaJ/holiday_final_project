from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from rest_framework.views import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import *
from rest_framework import status
from django.db.models import Q, Avg

# permission 어쩌고 추가


# Create your views here.
# 모든 영화 목록 조회
# 이거를 쓸 일은 없음.
@api_view(['GET'])
def index(request):
    movies = Movie.objects.all()
    # movies = Movie.objects.filter().orde
    # 단일조회가 아닌 쿼리셋은 many=True 필수
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)



# 단일 영화 조회
@api_view(['GET'])
def detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    # 단일 조회니까 many 생략
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


# 평점 매기기
# movie id는 url에 담아서 주고, request에는 몇 점 줬는지, 댓글 내용 포함해서 vue에서 줘야함
@api_view(['GET', 'POST'])
def rating(request, movie_id):
    
    serializer = RateSerializer(data={
        'rate_user': request.user.pk,
        'rate_movie': movie_id,
        'content': request.data['content'],
        'rate_score': request.data['rate_score'],
        })
    
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)



# 영화 좋아요
# vue에서 좋아요 숫자 알고 싶으면, movie의 like_movie_users의 length로 확인 가능
@api_view(['POST'])
def like(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if movie.like_movie_users.filter(id=request.user.id).exists():
        movie.like_movie_users.remove(request.user)
    else:
        movie.like_movie_users.add(request.user)
    return Response(status=status.HTTP_200_OK)


# 최근 영화중에 인기순으로 10개 내림차순 반환.
@api_view(['GET'])
def popular(request):
    # populars = Popular.objects.all()
    populars = Popular.objects.all().order_by('-vote_count')[:5]
    serializer = PopularSerializer(populars, many=True)
    return Response(serializer.data)



# 검색해서 영화들중에 parameter='keyword'에 포함하는것들 인기도순으로 5개 뽑아서 보내줌.
@api_view(['GET'])
# @permission_classes(['AllowAny'])
def search(request):
    keyword = request.GET.get('keyword')
    print(keyword)
    movies = Movie.objects.filter(
        Q(title__contains=keyword)
        #  |
        # Q(actors__actor__contains=keyword) |
        # Q(directors__director__contains=keyword)
    ).order_by('-vote_average')[:5]
    # order_by('-vote_count')[:5]
    print(movies)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


# @api_view(['GET'])
# def popular(request)
