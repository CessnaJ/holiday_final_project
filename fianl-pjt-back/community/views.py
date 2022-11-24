# from django.shortcuts import render, redirect, get_object_or_404
# from .models import *
# from rest_framework.views import Response
# from rest_framework.decorators import api_view
# from .serializers import *
# from rest_framework import status
# # permission 어쩌고 추가

# # Create your views here.
# # 모든 게시글 조회
# @api_view(['GET'])
# def index(request):
#     articles = Article.objects.all()
#     # 단일조회가 아닌 쿼리셋은 many=True 필수
#     serializer = ArticleSerializer(articles, many=True)
#     return Response(serializer.data)


# # 해당 게시글의 모든 댓글 조회
# @api_view(['GET'])
# def comment(request, article_id):
#     article = Article.objects.get(pk=article_id)
#     comments = article.comment_set.all()
#     serializer = CommentSerializer(comments, many=True)
#     return Response(serializer.data)

# 여기 위로 주석처리 했음.


# class PostViewSet(ModelViewSet):
#     queryset = Post.objects.all().order_by('-created_at')
#     serializer_class = PostSerializer
#     pagination_class = CustomResultsSetPagination
#     filter_backends = [DjangoFilterBackend]
#     filterset_class = PostFilter
#     permission_classes = [IsSuperUserOrReadOnly]
# # urls.py


####################################################### 아래부터 복붙
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
# from rest_framework.decorators import authentication_classes

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment



@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def article_list(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        print(serializer.data)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        if request.user == article.user:
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            if request.user == article.user:
                serializer.save()
                return Response(serializer.data)
            return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        # comments = Comment.objects.all()
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    


@api_view(['POST'])
def comment_create(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    
# # 게시글 생성
# @api_view(['POST'])
# def article_create(request):
#     # article = Article.objects.get(pk=article_pk)
#     # article = get_object_or_404(Article, pk=article_pk)
#     serializer = ArticleSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)



# #게시글 삭제 성공시 204 반환
# @api_view(['DELETE'])
# def article_delete(request, article_pk):
#     article = get_object_or_404(Article, pk=article_pk)
#     article.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)
