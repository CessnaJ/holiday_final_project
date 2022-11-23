from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.conf import settings

import base64
from movies.models import Movie
# from movies.serializers.review import ReviewSerializer
from .models import *

# 유저 정보를 넘겨줄때, 영화에서 파생된 정보까지 같이 넘겨주기떄문에 다시 보고 논리흐름 파악이 필요하다
# count는 부분은 어떻게 저렇게 되는건지 좀 봐야겠음.





class ProfileSerializer(serializers.ModelSerializer):
	#프로필 담아줄때 좋아요한 영화 담아오기
	class MovieSerializer(serializers.ModelSerializer):
        
		class Meta:
			model = Movie
			fields = '__all__'
    #팔로우한 유저도 담아오기         
	class UserSerializer(serializers.ModelSerializer):
            
		class Meta:
			model = User
			fields = ('pk', 'username')
                        
	like_movies = MovieSerializer(many=True)
	# review_set = ReviewSerializer(many=True, read_only=True)
	followings = UserSerializer(many=True)
	followers = UserSerializer(many=True)
	following_count = serializers.IntegerField(source='followings.count', read_only=True)
	followers_count = serializers.IntegerField(source='followers.count', read_only=True)

	class Meta:
		model = get_user_model()
		fields = ('pk', 'username', 'like_movies', 'review_set', 'followings', 'followers', 'followings_count',)






# class DecodeSerializer(serializers.ModelSerializer) :


#     def create(self, validated_data):
#         product = User.objects.create(**validated_data)

# 		#이미지 디코딩하기 
#         bulk_list = []
#         num = 1
#         for image_string in self.context.get("images"): #base64로 인코딩된 이미지들을 불러온다.
#             header, data = image_string.split(';base64,')
#             data_format, ext = header.split('/')
#             try:
#                 image_data = base64.b64decode(data)
#                 image_root = settings.MEDIA_ROOT + '\\' + str(product.id) + "_" + str(num) + "." + ext
#                 with open(image_root, 'wb') as f:
#                     f.write(image_data)
#                     bulk_list.append(UserImg(product=product, image=f'{product.id}_{num}.{ext}'))
#                 num += 1
#             except TypeError:
#                 self.fail('invalid_image')

#         images = UserImg.objects.bulk_create(bulk_list)

#         return product

#     class Meta:
#         model = User
#         fields = '__all__'
