from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from rest_framework import status 
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from .serializers import *

User = get_user_model()

# Create your views here.

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request, username):
    # username 받아서 profile 띄워줌.
    user = get_object_or_404(User, username=username)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
def follow(request, user_pk):
    # follow기능
    target = get_object_or_404(User, pk=user_pk)
    me = request.user

    if me != target: # 내가 나를 팔로우 못하게
        if target.followers.filter(pk=me.pk).exists(): # 이미 팔로우중이면
            target.followers.remove(me) # 언팔
            return Response(serializer.data)  # 직렬화된 json 보내줌
        
        else:  # 안되어있으면
            target.followers.add(me) # 팔로우
            serializer = ProfileSerializer(target)
            return Response(serializer.data) # 직렬화된 json 보내줌
        

        




# 이거 그냥 안넣는게 좋을거같음.
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_follow(request):
    # 나와 맞팔인 사람들이 좋아요를 누른 영화 추천

    user = get_object_or_404(User, pk=request.user.pk)
    serializer = ProfileSerializer(user)
    followings = serializer.data.get('followings')  # 내가 팔로잉 하는 사람들

    me = {
        "pk": request.user.pk,
        "username": request.user.username
    }

    follow_back = []  # 맞팔유저
    for following in followings:
        following_pk = following.get('pk')
        following_user = get_object_or_404(User, pk=following_pk)
        following_serializer = ProfileSerializer(following_user)
        following_following = following_serializer.data.get('followings')  # 내가 팔로잉 하는 사람의 팔로잉 하는 사람

        if me in following_following:  # 서로 팔로우 하는 상태 = 맞팔
            follow_back.append(following_pk)  
            # 인자로 following을 append하면 pk와 username 키를 가진 객체 추가, 여기서는 간단히 pk만 추가했음

    # return Response(follow_back)

    fb_like_movies = []  # 맞팔이 좋아하는 영화
    for fb_user_pk in follow_back:
        fb_user = get_object_or_404(User, pk=fb_user_pk)
        serializer = ProfileSerializer(fb_user)
        like_movies = serializer.data.get('like_movies')

        for like_movie in like_movies:  # 중복 추천 방지 위함
            if like_movie not in fb_like_movies:
                fb_like_movies.append(like_movie)

    return Response(fb_like_movies)




# class APITest(APIView):

#     def post(self, request) :

#         data = request.data
#         #serializer 직렬화
#         serializer = DecodeSerializer(data=data, context={'request': request, 'images':data.get("images")})

#         # 데이터 유효성 검사
#         if serializer.is_valid():
#             # DB에 저장
#             serializer.save()
#             return Response(get_successCode(serializer.data), status=status.HTTP_201_CREATED)

#         return Response(get_failCode(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
