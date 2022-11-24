from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.conf import settings

from django.db import transaction
from dj_rest_auth.registration.serializers import RegisterSerializer

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
			# 여기 선택으로 되어있는데 all로 바꾼다. 😀
			# fields = ('pk', 'username')
			fields = ('pk', 'username', 'image_select')
			# fields = '__all__'
                        
	like_movies = MovieSerializer(many=True)
	# review_set = ReviewSerializer(many=True, read_only=True)
	followings = UserSerializer(many=True)
	followers = UserSerializer(many=True)
	following_count = serializers.IntegerField(source='followings.count', read_only=True)
	followers_count = serializers.IntegerField(source='followers.count', read_only=True)

	class Meta:
		model = get_user_model()
		fields = ('pk', 'username', 'like_movies', 'followings', 'followers', 'following_count', 'followers_count', 'image_select', 'nickname')




class CustomRegisterSerializer(RegisterSerializer):

    image = serializers.CharField()

    # Define transaction.atomic to rollback the save operation in case of error
    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.nickname = request.data.get('nickname')
        user.image_select = request.data.get('image_select')
        print(user.image_select)
        print(user.nickname)
        # print(request.FILES['image'])
        # user.image = self.data.get('image')
        # user.image = request.data['image']
        user.save()
        return user

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
