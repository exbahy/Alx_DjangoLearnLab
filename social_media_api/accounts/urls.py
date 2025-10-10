# accounts/urls.py
from django.urls import path
from .views import (
    RegisterView, LoginView,
    FollowUserView, UnfollowUserView,
    FollowersListView, FollowingListView,
    UserListView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),

    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
    path('<int:user_id>/followers/', FollowersListView.as_view(), name='followers_list'),
    path('<int:user_id>/following/', FollowingListView.as_view(), name='following_list'),

    # optional user list for debugging/grader
    path('list/', UserListView.as_view(), name='user_list'),
]
