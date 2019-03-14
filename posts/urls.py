from django.urls import path
from . import views
from posts.viewsfolder.login_reg_view import RegistrationPageView, LoginPageView
from .views import AdminUserView
from .views import UserView, PostView, PostViewID, CommentViewList, FriendRequestView, FriendListView, AreFriendsView, \
    FollowView, FollowReqListView, FrontEndPostViewID, FrontEndCommentView, PostCreateView 
from .viewsfolder.login_reg_view import RegistrationPageView, LoginPageView

urlpatterns = [
    path('users/', UserView.as_view(), name='users'),
    path('author/<pk>/friends', FriendListView.as_view(), name='friendslist'),
    path('followreqs/', FollowReqListView.as_view(), name='followereqlist'),
    # path('author/<authorid1>/friends/<service2>/author/<authorid2>', AreFriendsView.as_view(), name='arefriends'),
    path('author/<authorid1>/friends/<authorid2>', AreFriendsView.as_view(), name='arefriends'),
    path('friendrequest/', FriendRequestView.as_view(), name='friendrequest'),
    path('follow/<authorid>', FollowView.as_view(), name='follow'),
    path('posts/', PostView.as_view(), name='posts'),
    path('frontend/posts/<pk>', FrontEndPostViewID.as_view(), name='frontpostid'),
    path('posts/<pk>', PostViewID.as_view(), name='postid'),
    path('posts/<post_id>/comments/', CommentViewList.as_view(), name='comments'),
    path('frontend/posts/<post_id>/comments/', FrontEndCommentView.as_view(), name='frontcomments'),
    path('users/', UserView.as_view(), name='users'),
    path('approve/', AdminUserView.as_view(), name='admin-users'),
    path('frontend/register/', RegistrationPageView.as_view(), name='register-users'),
    path('frontend/login/', LoginPageView.as_view(), name='login-user'),
    path('frontend/posts/create/', PostCreateView.as_view(), name="create_post"),
]
