from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from .models import CustomUser
from .serializers import (
	RegisterSerializer,
	LoginSerializer,
	UserSerializer,
	UserBriefSerializer,
	FollowActionSerializer,
)

User = get_user_model()


class RegisterView(generics.CreateAPIView):
	serializer_class = RegisterSerializer

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.save()
		token, _ = Token.objects.get_or_create(user=user)
		return Response({
			"user": UserSerializer(user).data,
			"token": token.key
		}, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
	serializer_class = LoginSerializer

	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data
		token, _ = Token.objects.get_or_create(user=user)
		return Response({
			"user": UserSerializer(user).data,
			"token": token.key
		})


class ProfileView(generics.RetrieveUpdateAPIView):
	serializer_class = UserSerializer
	permission_classes = [IsAuthenticated]

	def get_object(self):
		return self.request.user


class FollowUserView(APIView):
	permission_classes = [permissions.IsAuthenticated]

	def post(self, request, user_id):
		target = get_object_or_404(User, id=user_id)
		if target == request.user:
			return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

		request.user.following.add(target)
		request.user.save()
		return Response({"detail": f"You are now following {target.username}."}, status=status.HTTP_200_OK)


class UnfollowUserView(APIView):
	permission_classes = [permissions.IsAuthenticated]

	def post(self, request, user_id):
		target = get_object_or_404(User, id=user_id)
		if target == request.user:
			return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

		request.user.following.remove(target)
		request.user.save()
		return Response({"detail": f"You have unfollowed {target.username}."}, status=status.HTTP_200_OK)


class FollowersListView(generics.ListAPIView):
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = UserBriefSerializer

	def get_queryset(self):
		user = get_object_or_404(User, id=self.kwargs.get('user_id'))
		return user.followers.all()


class FollowingListView(generics.ListAPIView):
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = UserBriefSerializer

	def get_queryset(self):
		user = get_object_or_404(User, id=self.kwargs.get('user_id'))
		return user.following.all()
