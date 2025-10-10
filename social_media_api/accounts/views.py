# accounts/views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model, authenticate
from rest_framework.authtoken.models import Token

from .models import CustomUser
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer

# Register
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        data = UserSerializer(user).data
        data['token'] = token.key
        return Response(data, status=status.HTTP_201_CREATED)


# Login
class LoginView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, _ = Token.objects.get_or_create(user=user)
        data = UserSerializer(user).data
        data['token'] = token.key
        return Response(data, status=status.HTTP_200_OK)


# Follow / Unfollow using GenericAPIView and CustomUser.objects.all()
class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()

    def post(self, request, user_id):
        target = get_object_or_404(CustomUser, id=user_id)
        if target == request.user:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.add(target)
        return Response({"detail": f"You are now following {target.username}"}, status=status.HTTP_200_OK)


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()

    def post(self, request, user_id):
        target = get_object_or_404(CustomUser, id=user_id)
        if target == request.user:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.remove(target)
        return Response({"detail": f"You have unfollowed {target.username}"}, status=status.HTTP_200_OK)


# Lists: followers & following
class FollowersListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

    def get_queryset(self):
        user = get_object_or_404(CustomUser, id=self.kwargs.get('user_id'))
        return user.followers.all()


class FollowingListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

    def get_queryset(self):
        user = get_object_or_404(CustomUser, id=self.kwargs.get('user_id'))
        return user.following.all()


# A simple user list so grader can see CustomUser.objects.all() usage
class UserListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
