from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
  # id = models.IntegerField(primary_key=True) # 장르id를 pk로 뒀음.
  name = models.CharField(max_length=100) # 장르 이름

  
class Movie(models.Model):
  # id = models.IntegerField(primary_key=True) # 영화id - pk
  title = models.CharField(max_length=100) # 제목
  original_title = models.CharField(max_length=100) # 원제목
  # genres = models.CharField(max_length=100)
  overview = models.TextField(null=True, blank=True) # 없을수도 있음.
  release_date = models.CharField(max_length=100, null=True)
  vote_average = models.FloatField()
  vote_count = models.IntegerField()
  poster_path = models.CharField(max_length=100)
  backdrop_path = models.CharField(max_length=100, null=True)

  # 이하 manytomany 중개테이블
  genres = models.ManyToManyField(Genre, related_name='movies')
  like_movie_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
  # genre_check = models.ManyToManyField(Genre, related_name='genre_movies')



class Rate(models.Model): # 내 프로필에 내가 준 별점순을 나열하기 위한 중개모델
  rate_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  rate_movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  content = models.CharField(max_length=200) # 한줄평
  rate_score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)]) # 0~5로 받고
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)





# 임시로 판 모델. popular 저장해서 뿌려주는 용도
class Popular(models.Model): 
  title = models.CharField(max_length=100) # 제목
  original_title = models.CharField(max_length=100) # 원제목
  overview = models.TextField(null=True, blank=True) # 없을수도 있음.
  poster_path = models.CharField(max_length=100)
  release_date = models.CharField(max_length=100)
  vote_count = models.IntegerField()
  vote_average = models.FloatField()
  backdrop_path = models.CharField(max_length=100, null=True)

#